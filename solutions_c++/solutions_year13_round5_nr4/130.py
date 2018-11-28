#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

double DP[1<<20];
double P[1<<20];

int main()
{
    freopen("D-small1.in","r",stdin);
    freopen("D-small1.out","w",stdout);

    int tc;
    cin >> tc;
    for(int nt=1; nt<=tc; nt++)
    {
        string oc;
        cin >> oc;
        int n = oc.size();
        long long b=0;
        for(int i=0; i<n; i++)
        {
            if(oc[i]=='X')
                b+=(1<<i);
        }

        for(int i=0; i<(1<<n); i++)
        {
            DP[i]=0;
            P[i]=0;
        }
        DP[b]=0;
        P[b]=1;
        int k[20];
        for(int i=0; i<(1<<n)-1; i++)
        {
            for(int j=0; j<n; j++)
            {
                //cout << (i&(1<<j)) << endl;
                if( (i&(1<<j))==0)
                {
                    k[j]=j;
                    int p=j-1;
                    if(p==-1) p=n-1;
                    while(i&(1<<p))
                    {
                        k[p]=j;
                        p--;
                        if(p==-1) p=n-1;
                    }
                }
            }
            //for(int asd=0; asd<n; asd++) cout << k[asd] << " ";
            //cout << endl;
            for(int j=0; j<n; j++)
            {
                P[i|(1<<(k[j]))]+= P[i]/n;
                DP[i|(1<<(k[j]))]+= (DP[i])/n+(n-(k[j]-j+n)%n)*P[i]/n;
                //cout << (DP[i]+n-(k[j]-j+n)%n)*P[i]/n << endl;
            }
            //cout << P[i] << endl;
            //cout << DP[i] << endl;
        }
        //cout << P[(1<<n)-1] << endl;
        cout << "Case #" << nt << ": ";
        printf("%9.9Lf\n", DP[(1<<n)-1]);
    }
}
