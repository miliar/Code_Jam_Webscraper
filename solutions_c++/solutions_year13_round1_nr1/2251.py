#include<iostream>
using namespace std;
int V(int x)
{return (((x)*((x)+1)*((2*(x))+1))/6);}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A2.in","w",stdout);
    
    long long int T,k=1,i,y,z,c,j=0,t,w,lit,sum,r;
    cin>>T;    
    do
    {            sum=0;
                 j=0;
                 cin>>r>>t;
                 for(i=(2*r+1);sum<=t;i+=4)
                 {
                                    if(sum+i<=t)
                                      {sum+=i; j++;}
                                     else
                                       break;
                 }    
                 cout<<"Case #"<<k<<": "<<j<<"\n";
    }while(k++!=T);
    return 0;
}
