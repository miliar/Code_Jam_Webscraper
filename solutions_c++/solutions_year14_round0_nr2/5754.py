#include <iostream>
using namespace std;
int main()
{
    freopen("B-small-attempt.in","r",stdin);
    freopen("B-small-attempt.out","w",stdout);
    int t,i,j,k,l,n,m;
    cin>>t;
    double c,cc,f,min,tt,time,x;
    for(l=0;l<t;l++)
        {
                cc=2;
                min=100000000;
                time=0;
                cin>>f>>c>>x;
                for(i=0;i<2*x/f+1;i++)  
                {
                tt=time+x/cc;
              //  cout<<tt<<' '<<i<<endl;
                if (tt<min)min=tt;
                time=time+f/cc;
                cc=cc+c ;   
                }  
                cout<<"Case #"<<l+1<<": ";
                printf("%.7lf\n",min);
        }    
       // cin>>n;
}
