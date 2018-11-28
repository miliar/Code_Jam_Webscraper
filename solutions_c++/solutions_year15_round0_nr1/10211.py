#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int T,i,N,s,k,j;
    ifstream InFile;
    ofstream OuFile;
    InFile.open("A-small-attempt4.in");
    OuFile.open("Standing Ovation.txt");
    char a[1001];
    if(InFile.is_open()&&OuFile.is_open())
    {
        InFile>>T;
        j=T;
        while(T)
        {
            s=k=0;
            InFile>>N;
            InFile>>a;
            for(i=0;i<=N;i++)
            {
                if(s>=i&&a[i]>0)
                {
                    s+=(a[i]-48);
                }
                else
                {
                    if(a[i]>0)
                    {
                        k+=(i-s);
                        s=i;
                        s+=(a[i]-48);
                    }
                }
            }
            OuFile<<"Case #"<<j-T+1<<": "<<k<<'\n';
            T--;
        }
    }
}
