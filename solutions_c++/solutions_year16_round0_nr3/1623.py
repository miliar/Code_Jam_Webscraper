#pragma comment(linker, ”/STACK:36777216“)
#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;

#define int ll

bool larger(string a, string b){
    if(a.length()>b.length())return true;
    if(b.length()>a.length())return false;
    return(a>=b);
}
string  make_string(int a[], int n){
    string s;
    reverse(a, a+n);
    for(int i=0; i<n; i++)
        s+=char(a[i]+'0');
    return s;
}
string dif(string a, string b){
    int n = a.length();
    int m = b.length();
    if(n<m)swap(n, m), swap(a, b);
    int q[n+1], w[n+1];
    memset(q, 0, sizeof(q));
    memset(w, 0, sizeof(w));
    for(int i=0; i<n; i++)
        q[i] = (a[i] - '0');
    for(int i=0; i<m; i++)
        w[i] = (b[i] - '0');
    reverse(q, q+n);
    reverse(w, w+m);
    int ost = 0;
    for(int i=0; i<n; i++)
    {
        ost = ost + q[i] - w[i] + 10;
        q[i] = ost%10;
        if(ost<10) ost = -1; else ost = 0;
    }
    while(n>1&&q[n-1]==0)n--;
    return make_string(q, n);
}
string mod(string a, string b){
    string q, ans;
    int n = a.length();
    for(int i=0; i<n; i++)
    {
        if(q!=""||a[i]!='0')q+=a[i];
        if(larger(q, b))
        {
            int k = 0;
            while(larger(q, b)){
                q = dif(q, b);
                //cout<<q<<endl;
                k++;
            }
            ans += char(k + '0');
            if(q == "0") q = "";
        } else if(ans.length())ans+='0';
    }
    if(q=="")q="0";
    return q;
}
string mult(string a, string b){
    int n = a.length();
    int m = b.length();
    if(n<m)swap(n, m), swap(a, b);
    int q[n], w[n];
    int ans[3*n];
    memset(ans, 0, sizeof(ans));
    memset(q, 0, sizeof(q));
    memset(w, 0, sizeof(w));
    for(int i=0; i<n; i++)
        q[i] = (a[i] - '0');
    for(int i=0; i<m; i++)
        w[i] = (b[i] - '0');
    reverse(q, q+n);
    reverse(w, w+m);
    int mx = 0;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
        {
            int k = i + j;
            int x = q[i] * w[j];
            while(x>0)
            {
                x += ans[k];
                ans[k] = x % 10;
                x /= 10;
                mx = max(mx, k);
                k++;
            }
        }
    return make_string(ans, mx+1);
}
string sum(string a, string b){
    int n = a.length();
    int m = b.length();
    if(n<m)swap(n, m), swap(a, b);
    int q[n+1], w[n+1];
    memset(q, 0, sizeof(q));
    memset(w, 0, sizeof(w));
    for(int i=0; i<n; i++)
        q[i] = (a[i] - '0');
    for(int i=0; i<m; i++)
        w[i] = (b[i] - '0');
    reverse(q, q+n);
    reverse(w, w+m);
    int ost = 0;
    for(int i=0; i<n; i++)
    {
        ost = q[i] + w[i] + ost;
        q[i] = ost%10;
        ost = ost/10;
    }
    if(ost)q[n++]=ost;
    return make_string(q, n);
}
string to_string(int x){
    string s;
    while(x > 0){
        int q = x % 10;
        s = s + char(q + '0');
        x /= 10;
    }
    reverse(all(s));
    return s;
}

vector<int> trans(ll x){
    vector<int> a;
    while(x > 0){
        a.pb(x % 10);
        x /= 10;
    }
    reverse(all(a));
    return a;
}
ll f(vector<int> &a, int b){
    ll d = 1;
    ll s = 0;
    for(int i = a.size() - 1; i >= 0; i--){
        if(a[i] == 1)s += d;
        d = d * b;
    }
    return s;
}
ll f(ll x, int b){
    vector<int> a = trans(x);
    return f(a, b);
}

string f(string x, int b){
    string d = "1";
    string s = "0";
    for(int i = x.length() - 1; i >= 0; i--){
        if(x[i] == '1')s = sum(s, d);
        d = mult(d, to_string(b));
    }
    return s;
}

string composite(string x){
    for(int i = 2; i <= 100; i++){
        string y = to_string(i);
        if(mod(x, y) == "0"){
            return y;
        }
    }
    return "0";
}
int composite(ll x){
    for(int i = 2; i <= floor(sqrt(x)); i++){
        if(x % i == 0)return i;
    }
    return 0;
}

bool check(vector<int> &a){
    for(int i = 2; i <= 10; i++){
        ll x = f(a, i);
        if(!composite(x)){
            return false;
        }
    }
    return true;
}
bool check(ll x){
    vector<int> a = trans(x);
    return check(a);
}
int calc(ll x){
    int r = 0;
    while(x > 0){
        if(x % 10)r++;
        x /= 10;
    }
    return r;
}

main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    cin >> T;
    cout << "Case #1:\n";

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    vector<ll> b;
    n -= 2;


    ll y = 0;
    for(int i = 0; i < (1 << n); i++){
        y++;
        a[0] = 1;
        a[n + 1] = 1;
        for(int j = 1; j < n; j++){
            a[j] = 0;
        }
        ll x = i;
        for(int j = 0; x; j++){
            if(x & (1 << j)){
                x ^= (1 << j);
                a[1 + j] = 1;
            }
        }

        if(check(a)){
            b.pb(f(a, 10));
            if(b.size() == k)break;
        }
    }

    sort(all(b));
    for(int i = 0; i < b.size(); i++){
        string x, s = to_string(b[i]);
        for(int j = 0; j < s.length(); j++){
            x = x + s[j];
            x = x + s[j];
        }
        cout << x << " ";
        for(int j = 2; j <= 10; j++){
            cout << composite(f(x, j)) << " ";
        }
        cout << "\n";
    }
}
