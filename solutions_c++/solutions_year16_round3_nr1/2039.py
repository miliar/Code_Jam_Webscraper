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


int main() {
    int t;
    cin >> t;
    fr(_t,t) {
        vector<pair<int,int> > senators;
        int n;
        cin >> n;

        int temp,total1 = 0;
        fr(i,n) {
            cin >> temp;
            total1 += temp;
            senators.push_back(make_pair(temp,i));
        }

        int total = total1;
        printf("Case #%d: ",_t+1);

        while(total>0) {
            sort(all(senators),greater<pair<int,int> >());
            string plan = "";

            if(senators.size()>2 && senators[2].first == 1 && total == 3) {
                plan += (char)('A' + senators[2].second);
                senators[2].first--;
                total--;
            } else if(senators[0].first > 0) {
                if(senators[1].first>0) {
                    char a = 'A' + senators[0].second;
                    char b = 'A' + senators[1].second;
                    senators[0].first--;
                    senators[1].first--;
                    total-=2;
                    plan += a;
                    plan += b;
                } else {
                    if(senators[0].first>1) {
                        char a = 'A' + senators[0].second;
                        char b = 'A' + senators[0].second;
                        senators[0].first--;
                        senators[0].first--;
                        total-=2;
                        plan += a;
                        plan += b;
                    } else {
                        char a = 'A' + senators[0].second;
                        senators[0].first--;
                        plan += a;
                        total-=1;
                    }
                }
            }
            cout << plan << " ";

        }
        cout << endl;
    }
    return 0;
}


