#include<bits/stdc++.h>
#define trace1(x)                    cerr << #x << ": " << x << endl;
#define trace2(x, y)                 cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)              cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)           cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)        cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f)     cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#define ll long long int
#define MAXN 1002
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%lld",&i)
#define sout(i) printf("%d",i)
#define soutl(i) printf("%lld",i)
#define mp make_pair
#define REP(i,a,n) for(int i=a;i<n;i++)
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define vll vector<ll>

using namespace std;

int main(){
freopen("ip.txt", "r", stdin);
freopen("op.txt", "w", stdout);
int t, cnt = 1;
cin >> t;
while(t--){
    string str, ptr;
    map<string,int>min_steps;
    map<string,int>::iterator it;
    min_steps["+"] = 0;
    min_steps["-"] = 1;
    min_steps["++"] = 0;
    min_steps["--"] = 1;
    min_steps["+-"] = 2;
    min_steps["-+"] = 1;
    cin >> str;
    printf("Case #%d: ", cnt++);
    if(str.length() < 3)
        printf("%d\n", min_steps[str]);
    else{
        int ans = 0;
        ptr += str[0];
        char c = str[0];
        for(int i = 1; i < str.length(); i++){
            if(str[i] != c){
                ptr += str[i];
                c = str[i];
            }
        }
        for(int i = 0; i < ptr.length(); i++)
            ans += (ptr[i] == '-');
        ans *= 2;
        if(ptr[0] == '-'){
                ans --;
        }
        printf("%d\n", ans);
    }
}
return 0;
}
