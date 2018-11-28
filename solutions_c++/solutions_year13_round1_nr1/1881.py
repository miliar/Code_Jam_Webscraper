#include <iostream>

using namespace std;

int main()
{
    int T;
    long long r,t;
    long long resp=0;
    long long aux;
    cin>>T;
    
    for(int i=1; i<=T; i++)
    {
            cin>>r>>t;
            resp=0;
            
            while(1)
            {
               aux=((r+1)*(r+1)-(r*r));
			   r+=2;
               if(t<aux) break;
               resp++;
               t-=aux;
            }
                 
            cout<<"Case #"<<i<<": "<<resp<<endl;
    }
    
    return 0;    
}
