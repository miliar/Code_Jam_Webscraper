#include <iostream>
using namespace std;

int f(string str,int n,char P)
{
    if(n == 0) return 0;
    
    int ans=0;
    if(str[n-1] == P)
        ans+=f(str,n-1,P);
    
    else
    {
        P=P=='+'?P='-':P='+';
        ans+=1+f(str,n-1,P);
    }
    
    return ans;
}

int main()
{    
    int t=1,T;
    cin>>T;
    
    while(t <= T)
    {
        string str;
        cin>>str;
        
        cout<<"Case #"<<t<<": "<<f(str,str.size(),'+')<<'\n';
        
        ++t;
    }
    
    return 0;
}