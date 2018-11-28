#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define ff first
#define ss second
int n,m;
vector<ll> prime;
bool np[99999999];

void si(){
    np[0] = true;
    np[1] = true;
    for(int i=1;i*i<=99999999;i++){
        if(!np[i]){
            for(int j=i*i;j<=99999999;j+=i)np[j]=true;
        }
    }
    for(int i=1;i<=99999999;i++)
        if(!np[i])prime.push_back(i);
}
int ans = 0;
void solve(string s){
    if(!n)return;
    if(s.size()==15&&n){
        bool flag = true;
        vector<int> v;
        for(int i=2;i<=10;i++){
            ll x = 0;
            for(int j=0;j<s.size();j++){
                x+=s[j]-'0';
                x*=i;
            }
            x++;
            int y = 0;
            bool f= false;
            while(y<prime.size()&&prime[y]*prime[y]<=x){
                if(x%prime[y]==0){
                    f=true;
                    v.push_back(prime[y]);
                    break;
                }
                y++;
            }
            flag&=f;
        }
        if(flag){
            n--;
            cout << s << "1 " ;
            for(int i=0;i<v.size();i++)cout << v[i] << " ";
            cout << "\n";
        }
        return;
    }
    solve(s+"0");
    solve(s+"1");
}
int main()
{
    //freopen("B-large.in","r",stdin);
    freopen("outcon.txt","w",stdout);
    //test("");
    int t;
    si();
    scanf("%d",&t);
    for(int I=1;I<=t;I++){
       cin >> m >> n;
       cout << "Case #" << I << ":\n";
       solve("1");
    }
    return 0;
}
