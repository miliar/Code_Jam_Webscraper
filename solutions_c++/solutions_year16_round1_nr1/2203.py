#include <iostream>
using namespace std;
#define ll long long
int main()
{
    ll t,j=0;
    cin>>t;
    while(t--){j++;
        string s;
        cin>>s;
        string str="";
        str=s[0]+str;
    for(ll i=1;i<s.size();i++){
        if(s[i]>=str[0])
        str=s[i]+str;
        else 
        str=str+s[i];
    }
    cout<<"Case #"<<j<<": "<<str<<endl;
    }
    return 0;
}

