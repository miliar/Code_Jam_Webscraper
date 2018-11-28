#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define all(x)      (x).begin(), (x).end()
#define re(i,s,n)   for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef unsigned long long ull;
template<class T> T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
const double EPS = 1e-7;

string words[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SVNEE", "EIGHT", "IENN"};

vector<int> finalans;
bool done = false;
void solve(vector<int> f, vector<int> ans) {
    if(done) return;
    int s = 0;
    fr(i,26) s+=f[i];
    if(s<0) return;
    if(s==0) {
        finalans.clear();
        fr(i,ans.size()) {
            finalans.push_back(ans[i]);
            //cout << "ans " << ans[i];
        }
        //cout << endl;
        done = true;
        return;
    }

    fr(i,10) {
        bool found = true;
        string ww = words[i];
        fr(j, ww.size()) {
            if((i==3 && j==3)|| (i==7 && j==3) || (i==9 && j==2)) {
                if(f[ww[j]-'A']<=1) {
                    found = false;
                    break;
                }
            } else {
                if(f[ww[j]-'A']<=0) found = false;
            }
        }

        if(found) {
//            cout << "Found " << i << endl;

            vector<int> nf(f),nans(ans);
            nans.push_back(i);
            fr(j,ww.size()) {
                nf[ww[j]-'A']--;
            }
            solve(nf,nans);
        }
    }
}

int main() {
    int t;
    cin >> t;
    fr(_t,t) {
        done = false;
        vector<int> f(26,0);
        string s;
        cin >> s;

        int n = s.length();

        fr(i,n) {
            f[s[i] - 'A']++;
        }

        vector<int> ans;

        solve(f,ans);

        sort(all(finalans));
        printf("Case #%d: ",_t+1);
        fr(i,finalans.size()) {
            cout << finalans[i];
        }
        cout << endl;
    }


    return 0;
}


