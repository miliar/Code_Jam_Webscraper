#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
double blo[2][10000];
int main()
{
    int T;cin>>T;
    for(int cases=1;cases<=T;cases++)
    {
        int y=0,z=0;
        int n;cin>>n;
        for(int i=0;i<n;i++) cin>>blo[0][i];
        for(int i=0;i<n;i++) cin>>blo[1][i]; 
        sort(blo[0],blo[0]+n);   
        sort(blo[1],blo[1]+n);
        int p[2]={0,0};
        while(p[1]<n)
        {
            while(p[1]<n && blo[0][p[0]] > blo[1][p[1]]) p[1]++;
            if(p[1]<n) 
            {
                p[0]++;
                p[1]++;
            }
        }
        z=n-p[0];
        p[0]=0;p[1]=n-1;
        while(blo[0][p[0]]<blo[1][p[1]])
        {
            int ok=1;
            for(int i=0;i<=p[1] && ok;i++)
            {
                if(blo[0][n-1-i] < blo[1][p[1]-i]) ok=0;
            }
            if(ok) break;
            p[0]++;
            p[1]--;
        }
        y=n-p[0];
        printf("Case #%d: %d %d\n",cases,y,z);
    }    
    return 0;
}