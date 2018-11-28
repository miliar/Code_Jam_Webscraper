#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
int t;
int main()
{
    cin>>t;
    for(int xyz=1;xyz<=t;xyz++)
    {
        string s;cin>>s;
        int pocet=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(pocet%2==0 && s[i]=='-')pocet++;
            else if(pocet%2==1 && s[i]=='+')pocet++;
        }
        cout <<"Case #"<<xyz<<": "<<pocet<<endl;
    }
    return 0;
}
