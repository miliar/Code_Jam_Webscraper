#include<iostream>
#include<fstream>
using namespace std;

int os[1005];
fstream wejscie, wyjscie;

int main()
{
    wejscie.open("wejscie.txt", ios::in);
    wyjscie.open("wyjscie.txt", ios::out);
    int t;
    wejscie>>t;
    for(int i=1; i<=t; i++)
    {
        fill(os, os+1002, 0);
        int d, p, wynik=0;
        wejscie>>d;
        for(int j=0; j<d; j++)
        {
            wejscie>>p;
            os[p]++;
        }
        if(os[9]==1 && os[8]==0 && os[7]==0 && os[5]==0 && os[4]==0)
        {
            os[9]=0;
            wynik=1;
            os[6]++;
            os[3]++;
        }
        for(int j=9; j>0; j--)
        {
            if(os[j]!=0)
            {
                int x=0;
                bool da_rade=false;
                for(int k=j; k>(j+1)/2; k--)
                {
                    x+=os[k];
                    if(x<=j-k+1)
                    {
                        wynik+=x;
                        for(int h=j; h>=k; h--)
                        {
                            os[(h+1)/2]+=os[h];
                            os[h/2]+=os[h];
                            os[h]=0;
                        }
                        da_rade=true;
                        break;
                    }
                }
                if(!da_rade)
                {
                    wynik+=j;
                    break;
                }
            }
        }
        wyjscie<<"Case #"<<i<<": "<<wynik<<"\n";
    }
}
