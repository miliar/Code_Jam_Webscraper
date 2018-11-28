#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <algorithm>

using namespace std;

long long comp(long long n,long long p){
    return ((n+n-p+1)*p)/2;
}
long long solve(){
    long long n,m,a,b,p,celkovo=0ll,res=0ll;
    cin >> n >> m;
    vector<pair<pair<long long,long long>, long long > > pas;
    for(int i=0;i<m;i++){
        cin >> a >>  b >> p;
        pas.push_back(make_pair(make_pair(a,b),p));
        celkovo += p*comp(n,b-a);
    }
    sort(pas.begin(),pas.end());
    pas.push_back(make_pair(make_pair(1023456789ll,1023456789ll),0ll));
    vector<pair<long long,long long> > kon,zac;

    for(int i=0;i<m+1;i++){
        while(!kon.empty() && kon.back().first < pas[i].first.first){
            p = kon[kon.size()-1].second;
            while(p){
                cerr << kon.back().first << " " << zac.back().first << " ";
                if(zac.back().second>p){
                    cerr << p << endl;
                    res += p * comp(n,kon.back().first - zac.back().first);
                    zac.back().second-=p; p=0ll;
                }
                else {
                    cerr << zac.back().second << "*"<<endl;
                    p-= zac.back().second;
                    res += zac.back().second * comp(n,kon.back().first - zac.back().first);
                    zac.pop_back();
                }
            }
            kon.pop_back();
        }
        zac.push_back(make_pair(pas[i].first.first,pas[i].second));
        kon.push_back(make_pair(pas[i].first.second,pas[i].second));
        sort(kon.rbegin(),kon.rend());
    }
    cerr << celkovo << " " << res << endl;
    return celkovo-res;
}
int main(void){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)cout << "Case #" << t <<": " << solve() << endl;
    return 0;
}
