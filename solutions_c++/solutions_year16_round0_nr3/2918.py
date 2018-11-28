#include <bits/stdc++.h>
using namespace std;

bitset<100000010> bs;
vector<long long> primes;
void sieve(){
    bs.set();
    bs[0] = bs[1] = 0;
    for(long long i=2 ; i<=100000000 ; i++) if(bs[i]){
        for(long long j=i*i ; j<=100000000 ; j+=i) bs[j] = 0;
        primes.push_back(i);
    }
}
long long inbase(string a, int b){
    int p=0;
    long long ans=0;
    for(int i=a.size()-1 ; i>=0 ; i--){
        ans += (a[i]=='1')*(long long)pow((double)b,p);
        p++;
    }
    return ans;
}
int main(){
    freopen("cj.in","r",stdin);
    freopen("cj.out","w",stdout);
    sieve();
    //int t; cin >> t >> t >> t;
    vector<pair<string,vector<int> > > ans;
    for( long long a = (1<<15)+1 ; a<1<<16 ; a+=2){
        string s;
        for(int j=0 ; 1<<j <= a ; j++){
            if(1<<j & a) s+='1';
            else s+='0';
        }
        reverse(s.begin(),s.end());
        //cout << s << endl;
        pair<string,vector<int> > row;
        row.first = s;
        for(int b=2 ; b<=10 ; b++){
            long long temp = inbase(s,b);

            bool flag = false;
            for(int i=0 ; primes[i]<=sqrt((double)temp) ; i++){
                if(temp%primes[i] == 0){
                    row.second.push_back(primes[i]);
                    flag = true;
                    break;
                }
            }
            if(!flag) break;
        }
        if(row.second.size()==9){
            ans.push_back(row);
        }
        if(ans.size()==50) break;
        
    }
    cout << "Case #1:" << endl;
    for(int i=0 ; i<ans.size() ; i++){
        cout << ans[i].first << " ";
        for(int j=0 ; j<ans[i].second.size()-1 ; j++){
            cout << ans[i].second[j] << " ";
        }
        cout << ans[i].second[ans[i].second.size()-1] << endl;
    }

    return 0;
}