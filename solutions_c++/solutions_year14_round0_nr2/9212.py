#include<bits/stdc++.h>
#define  mp make_pair
#define MOD 1000000007
#define sc(n) scanf("%d",&n);
#define p(n)   printf("%d",n);
#define nl      printf("\n");

using namespace std;
long long   t,moves,i,k;
 double c,f,x,tim;
int main()
{
   
   freopen("C:\\Users\\Chandan\\Desktop\\input.txt","r",stdin) ;
   freopen("C:\\Users\\Chandan\\Desktop\\output.txt","w",stdout);
   
    k=1;
    cin>>t;
while(t--)
 {
        cin>>c>>f>>x;
   moves=(long long )(((x*f)/c -2.0)*(1.0/f));
        if(moves<0){ tim=x/2.0; printf("Case #%lld: %.7lf\n",k,tim);continue;}
       tim=0.0;
       for(i=0;i<moves;i++)
        {
               tim+=c/(2.0+(double)i*f);
        }
        tim+=x/(2.0+(double)(moves)*f);
    printf("Case #%lld: %.7lf\n",k,tim);
        k++;
    }

}


