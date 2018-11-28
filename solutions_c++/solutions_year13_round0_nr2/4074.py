#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int t;
int N, M;
short tab[100][100];
short maxN[100];
short maxM[100];
//bool tabodp[100][100];
inline void odp(int t, bool b)
{
    cout << "Case #"<<t<<": ";
    if(b)
        cout << "YES\n";
    else
        cout << "NO\n";
}
int main()
{

    cin >> t;
    for(int i =0;i<t;i++)
    {
       cin >>N>>M;

       for(int n=0;n<N;n++)
            for(int m=0;m<M;m++)
            {
                cin >> tab[n][m];
  //              tabodp[n][m]=false;
            }
        for(int n=0;n<N;n++)
        {
            maxN[n]=0;
            for(int m=0;m<M;m++)
            {
                if(tab[n][m]>maxN[n])
                    maxN[n]=tab[n][m];
            }
        }

        for(int m=0;m<M;m++)
        {
            maxM[m]=0;
            for(int n=0;n<N;n++)
            {
                if(tab[n][m]>maxM[m])
                    maxM[m]=tab[n][m];
            }
        }
        bool end=false;
        for(int m=0;(m<M)&&(!end);m++)
        {
            for(int n=0;(n<N)&&(!end);n++)
            {
                if(tab[n][m]<maxM[m]&&tab[n][m]<maxN[n])
                {
                    odp(i+1,false);
                    end=true;
                }
            }
        }
        if(!end)
            odp(i+1,true);
    }
    return 0;
}
