#include <bits/stdc++.h>

using namespace std;
typedef long long  ll;

vector <string> numbers ;
void build(ll x,string res  ){
    if (x==17) {
        numbers.push_back(res);
       // cout<<res<<endl;
        return;
    }
    else {
       if(x!=16 && x!=1) build(x+1,res+'0');
        build(x+1,res+'1');
    }

}

int main()
{    freopen("filla.txt","w",stdout);

    int cc=1;
    //freopen("ini.txt","r",stdin);
    cout<<"Case #1:\n";

    build(1,"");
   // cout<<numbers.size();
    
    
    for (int y=0; y<numbers.size(); y++) {
        
    
    vector<ll> divisors ;
    for (int k = 2; k<11; k++) {
        
        ll sum =0;
        for (int i = 0;i<numbers[y].size(); i++) {
            sum=sum*k +(numbers[y][i]-'0');
        }
        for (int i = 2; i<100; i++) {
            if (sum%i==0) {
                divisors.push_back(i);
                break;
            }
        }
        
        
    }
    
    if (divisors.size()==9) {
        cout<<numbers[y]<<" ";
        for (int i = 0;i<divisors.size() ; i++) {
            cout<<divisors[i]<<" ";
        }
        if (cc==50) {
            break;
        }
        cc++;
        cout<<endl;
    }
        
    }
    return 0 ;
}


