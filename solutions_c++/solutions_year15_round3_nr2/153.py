#include<bits/stdc++.h>

using namespace std;
typedef vector<int> VI;

void buildTable(string& w, VI& z)
{
  z = VI(w.length());
  int L = 0, R = 0;
  int n=w.size();
    for (int i = 1; i < n; i++) {
        if (i > R) {
            L = R = i;
            while (R < n && w[R-L] == w[R]) R++;
            z[i] = R-L; R--;
        } else {
            int k = i-L;
            if (z[k] < R-i+1) z[i] = z[k];
            else {
                L = i;
                while (R < n && w[R-L] == w[R]) R++;
                z[i] = R-L; R--;
            }
        }
    }
}


int cntMax(VI &table,string word,int len){
    int n=word.size();
    if(len<n)return 0;
    int mx=0;
    for(auto x : table)mx=max(mx,x);
    len-=n;
    int toAdd=n-mx;
    return 1+(len/toAdd);
}

void solve(){
    int k,l,s;
    cin >> k >> l >> s;
    string word;
    string key;
    cin >> key>> word;
    VI z;
    buildTable(word,z);
    vector<bool> has(30,false);
    for(auto x : key){
        has[x-'A']=true;
    }
    for(auto x : word){
        if(!has[x-'A']){
            cout << 0 << endl;
            return;
        }
    }
    // cnt max
    int MX=cntMax(z,word,s);
    vector<double> prob(word.size()+1,0.0);
    prob[0]=1.0;

    double exp=0;
    for(int t = 0 ; t < s ; ++ t ){
        vector<double> nxt(word.size()+1,0);

        for(int i = 0 ; i  <= l ; ++ i ){
            for(int j = 0 ; j  < k ; ++ j ){
                if(i<l&&key[j]==word[i]){
                    nxt[i+1]+=prob[i]/k;
                }
                else{
                    bool filledSome=false;
                    for(int q = 1 ; q <i ; ++ q){
                        if(q+z[q]>=i&&key[j]==word[i-q]){
                            //cout << i << " " << q << " " <<key[j] << " " << i-q <<endl;
                            nxt[i-q+1]+=prob[i]/k;
                            filledSome=true;
                            break;
                        }
                    }
                    if(!filledSome){
                        if(key[j]==word[0])
                            nxt[1]+=prob[i]/k;
                        else nxt[0]+=prob[i]/k;
                    }
                }
            }
        }
        prob=nxt;
        exp+=prob[l];
    }

    cout << MX-exp << endl;
}

int main(){
    freopen("B-small-attempt0"".in","r",stdin);
    freopen("B-small-attempt0"".out","w",stdout);
    cout << setprecision(10);
    cout << fixed ;
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        cout <<"Case #" <<i <<": ";
        solve();
    }
    return 0;
}
