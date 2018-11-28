#include <iostream>
#include <utility>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;
const ll mod=1000002013;
int n,m;
typedef pair<int, int> joft;
vector<joft> events;
bool comp(const joft& j1,const joft& j2){
    if (j1.first!=j2.first)
        return j1.first<j2.first;
    return j1.second>j2.second;
}
int main(){
    int tcou;cin>>tcou;int tnum=0;
    while (tcou--){
        cin>>n>>m;
        events.clear();
        ll save = 0;
        for (int i=0;i<m;++i){
            int s,e,p;
            cin>>s>>e>>p;
            ll l=e-s;
            save = (save+((l*(l-1)/2)%mod*p)%mod)%mod;
            events.push_back(joft(s,p));
            events.push_back(joft(e,-p));
        }
        map<int, ll> cards;
        sort(events.begin(), events.end(),comp);
        save = (mod-save)%mod;
        for (int i=0;i<events.size();++i){
            if (events[i].second>0){
                cards[events[i].first]+=events[i].second;
            }
            else{
                map<int, ll>::iterator it=cards.end();--it;
                while (events[i].second<0){
                    ll num=min(it->second, ll(-events[i].second));
                    it->second-=num;
                    events[i].second+=num;
                    ll l=events[i].first-it->first;
                    save = (save+(((l*(l-1)/2)%mod)*num)%mod)%mod;
                    --it;
                }
            }
        }
        cout<<"Case #"<<(++tnum)<<": "<<(save)%mod<<endl;
    }
    return 0;
}
