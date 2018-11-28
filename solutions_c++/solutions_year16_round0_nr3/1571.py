#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define vi vector<int>
#define all(c) c.begin(), c.end()
#define pb push_back
#define f first
#define s second
#define mod 1000000007
#define inf 1e9
#define pl pair<ll,ll>
#define pii pair<pi,pi>
#define f first
#define mp make_pair
#define s second
#define rep(i,a,n) for(int i=a;i<n;i++)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);i--)
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())

vector<string> v;

void p1() {
    queue<string> q;
    q.push("0");
    q.push("1");
    while(q.front().size() != 15) {
        string s = q.front();
        q.pop();
        q.push(s + "0");
        q.push(s + "1");
    }
    while(!q.empty()) {
        string s = q.front();
        q.pop();
        if(s[14] == '1') {
            v.pb("10000000000000000" + s);
        }
    }
}

bool ok(string s) {
    int sum = 0;
    for(int i = 0; i < 32; i++) {
        if(i & 1) sum -= (s[i] - '0');
        else sum += (s[i] - '0');
    }
    if(sum) return false;
    return true;
}

//#define test
int main() {
    ios_base::sync_with_stdio(false);
#ifdef test
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
#endif
    p1();
    cout << "Case #" << 1 << ":" << endl;
    int i = 0;
    set<string> st;
    while(st.size() != 500) {
        string s = v[i];
        if(ok(s)) {
            st.insert(v[i]);
        }
        i++;
    }
    set<string>::iterator it;
    for(it = st.begin(); it != st.end(); it++) cout << *it << " 3 2 5 2 7 2 3 2 11" << endl;
    return 0;
}

