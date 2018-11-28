#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

    int war(int n,double mass[],double smass[])
    {
        int i,j,k=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                if(smass[j]>mass[i])
                {
                    smass[j]=0;
                    k++;
                    break;
                }
            if(j==n+1)
                for(j=0;j<n;j++)
                    if(smass[j])
                    {
                        smass[j]=0;
                        break;
                    }
            mass[i]=0;
        }
        return k;
    }

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T,N;
    cin >>T;
    for(int x=1;x<=T;x++)
    {
        double na[1001],ke[1001],sna[1001],ske[1001];
        cin >>N;
        for(int i=0;i<N;i++)
        {
            cin >>na[i];
            sna[i]=na[i];
        }
        sort(sna,sna+N);
        for(int i=0;i<N;i++)
        {
            cin >>ke[i];
            ske[i]=ke[i];
        }
        sort(ske,ske+N);
        int y=war(N,ke,sna),z=N-war(N,na,ske);
        cout <<"Case #"<<x<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
