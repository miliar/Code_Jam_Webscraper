#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std ;
int main()
{
    int t,t1=1;
    FILE *p ;
    p=fopen("output.txt","w") ;
    cin>>t ;
    while(t1<=t)
    {
        double c,f,x ;
        double rate=2.00 ;
        cin>>c>>f>>x;
        double ans=0.0,a1,a2;
        while(1)
        {
            a1=(x/rate);
            a2=(c/rate)+(x/(rate+f)) ;
            if(a1<=a2)
            {
                ans+=a1 ;
                break ;
            }
            else
            {
                ans+=(c/rate) ;
                rate+=f;
            }
        }
        //cout<<ans<<"\n" ;
        //printf("%.7f\n",ans) ;
        fprintf(p,"Case #%d: %.7f\n",t1,ans) ;
        t1++ ;
    }
    return 0 ;
}
