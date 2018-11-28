#include <iostream>
using namespace std; 
int main() 
{ 
    int t,d,j;
    int i,count[100];
    int fraction[2];
    float num;
    cin>>t;
    for(i=0;i<t;i++)
    count[i]=0;
    for(i=0;i<t;i++)
    {
        scanf("%i/%i",&fraction[0],&fraction[1]);
        d=fraction[1];
        while(d%2==0)
        d/=2;
        if(d==1)
        {
            num=fraction[0]/(float)fraction[1];
            while((int)num!=1)
            {
                if(num<1)
                {
                    num*=2.0;
                    count[i]++;
                }
                else
                    num-=1.0;
                
            }
        }
                
        else
        count[i]=-1;
        
    }    
    for(i=0;i<t;i++)
    {   
        j=i+1;
        if(count[i]==-1)
        cout<<"Case #"<<j<<": impossible\n";
        else
        cout<<"Case #"<<j<<": "<<count[i]<<"\n";
    }
}