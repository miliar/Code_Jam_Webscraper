#include <iostream>
#include <stdlib.h>
#include <vector>
#include <QtCore/QFile>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QTextStream>
#include "../../ZKR4X/lib/zstring.h"

class GString : public QString
{
    public:
        GString(QString _str) : QString(_str)
        {
            _str.replace(" ", "\n");
            strList = _str.split("\n");

            strList.removeAll("\n");
            strList.removeAll("\r");
            strList.removeAll("\r\n");
            strList.removeAll(" ");
            strList.removeAll("");
        }


        GString& operator>>(QString& _str)
        {
            if(strList.size()) {
                _str = strList[0];
                strList.removeFirst();
            }

            return *this;
        }

        GString& operator>>(ZInt& _str)
        {
            if(strList.size()) {
                _str = strList[0];
                strList.removeFirst();
            }

            return *this;
        }

        GString& operator>>(int& _str)
        {
            if(strList.size()) {
                _str = strList[0].toInt();
                strList.removeFirst();
            }

            return *this;
        }

        QStringList strList;
};

void permute(QList<ZInt> &_list, int a, int b)
{
    ZInt c = _list[a];
    _list[a] = _list[b];
    _list[b] = c;
}

void sort(QList<ZInt> &_list, bool _sens = true)
{
    bool bKeep = true;
    while(bKeep) {
        bKeep = false;
        for(int i = 1; i < _list.size(); i++)
        {
            if(_sens && _list[i-1] > _list[i] || ! _sens && _list[i-1] < _list[i])
            {
                permute(_list, i-1, i);
                bKeep = true;
            }
        }
    }
}

bool isPalin(ZInt _a, ZInt _b)
{
    std::cout << "#" << _a << " " << _a.reverse() << "\n";
    if(_a != _a.reverse()) return false;
    if(_b != _b.reverse()) return false;
    return true;
}

bool check(int **A, int n, int m)
{
    QList<int> list;
    QList<int*> pos;
    int f = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            int newId = A[j][i], x = 0;
            if((list.contains(newId))) {
                bool b = false;
                for(int k = 0; k < list.size(); k++)
                    if(list[k] == newId && (i == pos[k][0] || j == pos[k][1])) {
                        b = true;
                        list.append(newId);
                    pos.append(new int [2]{i, j});
                        break;
                    }
                    if(!b) { std::cout << newId <<  "# " << i << " " << j << "\n";f++;}
                if(f>1) return false;
            }
            else {
                list.append(newId);
                pos.append(new int [2]{i, j});
            }
        }
    }

    return true;
}

int main(int argc, char** argv)
{
    int T = 0;
    int **A;
    int a, b;

    QFile *file = new QFile("in.txt");
    if(!file->open(QIODevice::ReadOnly)) return 1;

    GString in = QString(file->readAll());
    file->close();

    file = new QFile("out.txt");
    if(!file->open(QIODevice::WriteOnly | QIODevice::Truncate)) return 2;
    QTextStream out(file);

    /*in >> T;
    for(int i = 1; i <= T; i++) {
        in >> n >> m;
        std::cout << T << " " << m <<  " " << n << "\n";
        A = new int*[n];
        for(int j = 0; j < n; j++)
            A[j] = new int[m];
        for(int j = 0; j < n; j++) {
            for(int k = 0; k < m; k++)
            {
                in >> A[j][k];
            }
        }

        bool r = check(A, m, n);
        if(r)
            out << "Case #" << i << ": YES\r\n";
        else
            out << "Case #" << i << ": NO\r\n";

    }*/

    in >> T;
    for(int i = 1; i <= T; i++) {
        in >> a >> b;
        ZInt nb = 0;
        ZInt s = 1;
        for(ZInt j = 1; s <= b; j++) {
            if(s >= a && isPalin(s, j)) {
                std::cout << s << " " << j << "\n";
                nb++;
            }
            s += 2*j+1;
        }

        out << "Case #" << i << ": " << nb.getStr() << "\r\n";

    }

    file->close();

    system("out.txt");
}
