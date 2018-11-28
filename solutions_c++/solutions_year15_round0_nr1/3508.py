#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.txt","w",stdout);
    int t,sum,c,h;
    string s;
    cin>>t;
    for(int x=1; x<=t; x++){
            c=sum=0;
        cin>>h>>s;
        for(int i=0; i<s.size(); i++){
            if(sum<i){c+=i-sum;
            sum=i;
            }
            sum+=s[i]-'0';
        }
     cout<<"Case #"<<x<<": "<<c<<endl;
    }
    return 0;
}
