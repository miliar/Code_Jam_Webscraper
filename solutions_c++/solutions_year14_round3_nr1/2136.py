#include <iostream>
using namespace std; 
int gcd(int a, int b)
{
    while(b) b ^= a ^= b ^= a %= b;
    return a;
}
int main() 
{   int  g;
    int t,d,j;
    int i,count[1000];
    int fraction[2];
    float num;
    cin>>t;
    for(i=0;i<t;i++)
    count[i]=0;
    for(i=0;i<t;i++)
    {
        scanf("%i/%i",&fraction[0],&fraction[1]);
        
        g=gcd(fraction[0],fraction[1]);
       
    fraction[0]/=g;
    fraction[1]/=g;
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
        cout<<"Case #"<<j<<": Impossible\n";
        else
        cout<<"Case #"<<j<<": "<<count[i]<<"\n";
    }
    int gggg;
    cin>>gggg;
} 
