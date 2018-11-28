#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
main()
{

    double current,ans,x,c,f;
    int i,j,k,n,m,t;

    FILE *fin  = fopen ("input.in", "r");
    FILE *fout = fopen ("output.txt", "w");
    fscanf(fin,"%d",&t);
    //cin>>t;
    for(i=1;i<=t;i++)
    {
        fscanf(fin,"%lf %lf %lf",&c,&f,&x);
        //cin>>c>>f>>x;
        ans=0;
        current=2;
        while((c/current)+(x/(current+f))<(x/current))
        {
            ans+=c/current;
            current=current+f;
            //printf("%lf %lf\n",ans,current);
        }
        ans+=(x/current);
        fprintf(fout,"Case #%d: %lf\n",i,ans);
        //cout<<ans<<endl;

    }
    return 0;
}
