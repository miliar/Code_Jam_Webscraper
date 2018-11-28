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

int check(const QString tic[4][4], int x, int y, int a)
{
    bool full = true;
    for(int i = 0; i < 8; i++) {
        int nb = 1, dx = 0, dy = 0;
        if(a == 3) std::cout << i << " " << x << " " << y << " " << a << "\n";
        if(i == 0 && x == 0)
            dx = 1;
        else if(i == 1 && x == 0 && y == 0)
            dx = 1, dy = 1;
        else if(i == 2 && y == 0)
            dy = 1;
        else if(i == 3 && x == 3 && y == 0)
            dx = -1, dy = 1;
        else if(i == 4 && x == 3)
            dx = -1;
        else if(i == 5 && x == 3 && y == 3)
            dx = -1, dy = -1;
        else if(i == 6 && y == 3)
            dy = -1;
        else if(i == 7 && x == 0 && y == 3)
            dx = 1, dy = -1;
        else continue;
        for(int j = 1; j <= 3; j++) {
            if(a == 3 && i == 2) std::cout << "##" << tic[x+dx*j][y+dy*j].toStdString() << " " << x << " " << y << " " << x+dx*j << " " << y+dy*j << "\n";

            if(tic[x+dx*j][y+dy*j].left(1) == tic[x][y].left(1) || tic[x+dx*j][y+dy*j].left(1) == "T")
                nb++;
            else {if(i == 5)std::cout << nb << "\n";
                break;}
        }

        if(nb == 4) {
            if(tic[x][y] == "X")
                return 1;
            if(tic[x][y] == "O")
                return 2;
        }
    }



    if(x == 3 && y == 3) {for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(tic[i][j] == ".") return 4;
        }
    }return 3;} else
    return 0;
}

int main(int argc, char** argv)
{
    int T = 0;
    QString tic[4][4];
    QString a;

    QFile *file = new QFile("in.txt");
    if(!file->open(QIODevice::ReadOnly)) return 1;

    GString in = QString(file->readAll());
    file->close();

    file = new QFile("out.txt");
    if(!file->open(QIODevice::WriteOnly | QIODevice::Truncate)) return 2;
    QTextStream out(file);

    in >> T;
    for(int i = 0; i < T; i++) {
        for(int j = 0; j < 4; j++) {
            in >> a;
            for(int k = 0; k < 4; k++)
            {
                tic[k][j] = a[k];
            }
        }


bool keep = true;int x = 0;
            for(int j = 0; j < 4 && keep; j++) {
            for(int k = 0; k < 4 && keep; k++)
            {x++;
                std::cout << tic[k][j].toStdString() << "&$";
            }std::cout << "\n";}
            std::cout << " ***********"<< x;
        for(int j = 0; j < 4 && keep; j++) {
            for(int k = 0; k < 4 && keep; k++)
            {
                int r = check(tic, j, k, i);
                if(r == 1)
                    out << "Case #" << i+1 << ":" << " X won\r\n";
                else if(r == 2)
                    out << "Case #" << i+1 << ":" << " O won\r\n";
                else if(r == 3)
                    out << "Case #" << i+1 << ":" << " Draw\r\n";
                else if(r == 4)
                    out << "Case #" << i+1 << ":" << " Game has not completed\r\n";
                else
                    continue;
                keep = false;
            }
        }
    }

    file->close();

    system("out.txt");
}
