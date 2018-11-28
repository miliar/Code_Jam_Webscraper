#include<bits/stdc++.h>

using namespace std;

#define ll long long

int main()
{
    ll casoos,lon,cas=0;
    cin>>casoos;
    while(casoos--){
        cin>>lon;
        string s;
        cin>>s;
        ll total=0,amigos=0,ta=0;
        for(ll i=0; i<=lon;i++){
            amigos=0;
            if(total<i){
                ta+=amigos=i-total;
                total+=amigos;
            }
            total+=s[i]-'0';
        }
        cout<<"Case #"<<cas+1<<": "<<ta<<endl;
        cas++;
    }
    return 0;
}
