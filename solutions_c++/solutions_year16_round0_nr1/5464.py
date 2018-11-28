#include <iostream>
#include <fstream>

using namespace std;
typedef long long ll;

bool mass[10]={0};

void func(long long a)
{
    while(a)
    {
        
        long long b=a%10;
        
        mass[b]=1;
        
        a/=10;
    }
}


int main()
{
    
    ifstream in("//Users/vlad8/Downloads/A-large.in.txt");
    ofstream out("/Users/vlad8/Downloads/D-small-attempt123.out.txt");
    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
    ll n;
    in>>n;
        
        if(!n)
        {
            out<<"Case #"+to_string(i+1)+": INSOMNIA"<<'\n';
            
            continue;
        }
        
        ll n1=n;
        
        while(true)
        {
        
            func(n1);
            
            int sum=0;
            
            for(int u=0;u<10;u++)
            {
                sum+=mass[u];
            }
            
            if(sum==10)
                break;
            
            n1+=n;
            
        }
        
        
        out<<"Case #"+to_string(i+1)+": ";
        
        out<<n1;
        
        out<<endl;
        
        for(int u=0;u<10;u++)
            mass[u]=0;
    }
    
    
   
}