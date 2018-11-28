#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <map>
#include "ttmath/ttmath.h"
#include <math.h>

using namespace std;

bool isPerfectSquare(long n)
{
    long tst;
    if (n < 0)
        return false;

    switch((int)(n & 0xF))
    {
    case 0:
        tst = (long)sqrt(n);
        return tst*tst == n;
        break;

    case 1:
        tst = (long)sqrt(n);
        return tst*tst == n;
        break;
    case 4:
        tst = (long)sqrt(n);
        return tst*tst == n;
        break;
    case 9:
        tst = (long)sqrt(n);
        return tst*tst == n;
        break;

    default:
        return false;
    }
}


bool isPal(long broj)
{
    stringstream ss;
    ss<<broj;
    string normal = "";
    ss>>normal;
    if(normal == string(normal.rbegin(),normal.rend()))
    {
        return true;
    }
    return false;
}

long testiraj(long  pocetak, long  kraj)
{
    //cout<<pocetak<<"->"<<kraj<<endl;
    long rez = 0;
    long tst = 0;
    bool palindrom = false;
    for(long i = pocetak; i<=kraj;i++)
    {
        palindrom = isPal(i);
        if(!palindrom)
        {
            continue;
        }
        if(isPerfectSquare(i))
        {
            tst = (long)sqrt(i);
            if(isPal(tst))
            {
                //cout<<"b: "<<i<<"sq: "<<tst<<endl;
                rez++;
                for(long j = 1;j<=kraj-i;j++)
                {
                    long novi = tst +j;
                    if(novi*novi > kraj)
                    {
                        i= kraj+1;
                        break;
                    }
                    if(isPal(novi))
                    {
                        i=novi*novi-1;
                        break;
                    }
                }
            }
        }

    }

    //cout<<rez<<endl;
    //system("pause");
    return rez;
}



int main()
{
    ifstream ifs("C-small-attempt4.in");
    ofstream ofs;
    ofs.open("output1.out", fstream::app | fstream::out);
    int broj_testa;
    int kraj = 0;
    string line;
    if(ifs.is_open())
    {
        getline(ifs, line);
        broj_testa = 1;
        string buf = "";
        while(ifs.good())
        {
            //INPUT
            getline(ifs, line);
            if(line.compare("")==0){break;}
            string prviBroj= "";
            string drugiBroj = "";
            vector<string> splitLine;
            stringstream ss1(line);

            while(ss1 >> buf)
            {
                splitLine.push_back(buf);
            }
            stringstream prvi(splitLine[0]);

            stringstream drugi(splitLine[1]);

            long  a,b;
            prvi>>a;
            drugi>>b;
            long result = testiraj(a, b);
            ofs<<"Case #"<<broj_testa<<": " << result<<endl;
            broj_testa++;
        }
        ifs.close();
        ofs.close();
    }
}

