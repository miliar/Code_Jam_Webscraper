#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.in","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        int k=1;
        double e=0.0,z=0.0,l=2.0;
        //memset(d,0,sizeof(d));
        e=x/l;
        z=c/l+x/(l+f);
        l=l+f;
        while(e>z){
            e=z;
            z=z-(x/l)+(c/l)+(x/(l+f));
            l=l+f;
        }
        printf("Case #%d: %.7lf\n",i,e);
        e=0.0;z=0.0;
    }
    return 0;
}
