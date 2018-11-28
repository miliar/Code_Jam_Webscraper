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

           /* strList.removeAll("\n");
            strList.removeAll("\r");
            strList.removeAll("\r\n");
            strList.removeAll(" ");
            strList.removeAll("");*/
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


/**
 Functions
**/

static ZInt r, t, T;
/*
static int T = 0, E, R, N;
static QList<int> V;

int nbTotal()
{
    int t = 0, e = E;
    sort(V, false);
    for(int i = 0; i < V.size(); i++) {
        int nb = e;
        t += nb*V[i];
        e -= nb;

        e += R;
        if(e > E) e = E;
    }

    return t;
}*/

ZInt nbTotal()
{
    ZInt nb = 0, currT = 0;
    ZInt i = r-1;

    while(currT <= t) {
        i += 2;

        currT = i*i-((i-1)*(i-1))+currT;

        nb++;
    }std::cout << currT << " : " << currT << "\n\\n\n\n\n\n";
    nb--;

    return nb;
}

int main(int argc, char** argv)
{
    QFile *file = new QFile("in.txt");
    if(!file->open(QIODevice::ReadOnly)) return 1;

    GString in = QString(file->readAll());
    file->close();

    file = new QFile("out.txt");
    if(!file->open(QIODevice::WriteOnly | QIODevice::Truncate)) return 2;
    QTextStream out(file);

    in >> T;
    for(int i = 1; i <= T; i++) {
        in >> r >> t;
        std::cout << r << " " << t << "\n";
      /*  in >> E >> R >> N;
        V.clear();
        for(int i = 0; i < N; i++) {
            V.push_back(0);
            in >> V[i];
        }*/
        /**
            Code
        **/

      //  out << "Case #" << i << ": " << nbTotal() << "\r\n";
        out << "Case #" << i << ": " << nbTotal().getStr() << "\r\n";

    }

    file->close();

    system("out.txt");
}
