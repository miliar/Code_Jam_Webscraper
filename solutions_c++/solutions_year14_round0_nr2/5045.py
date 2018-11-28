#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

double c,f,x;
int T;
double ck(int m)
{
    double ans=0;
    for(int i=0;i<m;i++)
        ans+=1/(2+i*f);
    ans=ans*c+x/(2+m*f);
    return ans;
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);    
    int cs=0;
    long long N,S;
    while(T--){
        cin>>c>>f>>x;
        int l=0,r=10000000;
        while(r-l>3)
        {
            int lx=(l+r)/2,rx=lx+1;
            if (ck(lx)>ck(rx)) l=lx+1;
            else r=rx; 
        }
        // cout<<l<<" "<<r<<endl;
        cout<<"Case #"<<++cs<<": "; 
        double ans=1E99;
        for (int i=l;i<=r;i++) ans=min(ans,ck(i));
        printf("%.7f\n",ans);
    }
    return 0;
} 