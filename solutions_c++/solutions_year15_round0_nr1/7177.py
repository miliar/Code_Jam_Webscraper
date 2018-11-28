#include<iostream>
using namespace std;

int main()
{
    
    freopen("A-large.in","r",stdin);

    freopen("output_standlarge.txt","w",stdout);
    
    
    int t,q,e,pcount=0,val=0,f=0,final=0,r=0;
    char w[1100];
    
    
    cin>>t;
    
    for(int i=1;i<=t;i++)
    {
            cin>>q>>w;
            
            //e=w[0]-48;
            
            pcount=0;
            f=0;
            final=0;
            r=0;
            
            for(int j=0;j<=q;j++)
            {
                    val=w[j]-48;
                    
                    pcount=pcount+val;
                    
                    if((pcount-1)<j)
                    {
                                    f=(j-pcount-1);
                                    if(f<0)
                                    r=f*(-1);
                                    else
                                    r=f;
                                    
                                    final=final+r;
                                    pcount=pcount+r;
                                    
                    }
                    
                    
            }
            
            cout<<"Case #"<<i<<": "<<final<<"\n";
            
            
    }
            
            
    
    //system("pause");
    
    return 0;
}
