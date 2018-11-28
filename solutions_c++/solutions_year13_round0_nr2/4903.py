#include <iostream>
#include <fstream>
using namespace std;

int tren;

void displej(int stat,int uk)
{
    int perc=(double)stat/(double)uk*100.0;
    for (int i=tren;i<perc/10;i++)
        cout << ".";
    tren=perc/10;
}
        int niz[200][200];
        int n,m; //y,x

bool ok(int x, int y)
{
    bool a=true,b=true,c=true,d=true;
    for (int xx=x;xx<m;xx++)
    {
        if (niz[xx][y]>niz[x][y]) a=false;
    }
    for (int xx=x;xx>=0;xx--)
    {
        if (niz[xx][y]>niz[x][y]) b=false;
    }
    for (int yy=y;yy<n;yy++)
    {
        if (niz[x][yy]>niz[x][y]) c=false;
    }
    for (int yy=y;yy>=0;yy--)
    {
        if (niz[x][yy]>niz[x][y]) d=false;
    }
    return ((a&&b)||(c&&d));
}

int main()
{
    string str;
    getline(cin,str);
    ifstream in(str.c_str());
    //ifstream in("in.txt");
    ofstream out("izlaz.txt");
    int tests;
    in >> tests;
    cout << "working ";
    tren=0;
    for (int t=0;t<tests;t++)
    {
        in >> n >> m;
        bool more=true;
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                in >> niz[j][i];
            }
        }
        bool rez=true;
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                if (!ok(j,i)) {rez=false;i=n;break;}
            }
        }
        /*for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                out << niz[j][i] << " ";
            }
            out << endl;
        }
        out << "\n";
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                out << ok(j,i) << " ";
            }
            out << endl;
        }*/
        displej(t,tests);
        out << "Case #" << t+1 << ": ";
        if (rez) out << "YES"; else out << "NO";
        //out << "\n--------------------";
        out << endl;
    }
    return 0;
}
