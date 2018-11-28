#include <bits/stdc++.h>
using namespace std;

typedef    unsigned long long                 ull;
typedef    long long                          ll;
typedef    long double                        ld;
#define    Set(v,d)                           memset(v, d, sizeof(v))
#define    oo                                 100000007   //infinity
#define    F                                  first
#define    S                                  second
#define    pb                                 push_back
#define    sz(x)                              (int)(x.size())
#define    all(x)                             (x.begin()), (x.end())
#define    rall(x)                            (x.rbegin()), (x.rend())
typedef    vector<int>                        vi;
typedef    pair<int, int>                     ii;

int N, j;
ll arr[11][33];
ll p2, p3, p4, p5, p6, p7, p8, p9, p10;
ll div2, div3, div4, div5, div6, div7, div8, div9, div10;

ll divisor(ll n){
    for(ll i=2;i*i<=n;i++)
        if( !(n%i) ) return i;
    return -1;
}

ll Base(string s, int base){
    ll sum = 0;
    for(int i=0;i<sz(s);i++) sum+=(s[i]-'0')*arr[base][i];
    return sum;
}

bool Check(string s, ll i){
    div2 = divisor(i);
    if(div2 == -1) return 0;

    ll Base3 = Base(s, 3);
    div3 = divisor(Base3);
    if(div3 == -1) return 0;

    ll Base4 = Base(s, 4);
    div4 = divisor(Base4);
    if(div4 == -1) return 0;

    ll Base5 = Base(s, 5);
    div5 = divisor(Base5);
    if(div5 == -1) return 0;

    ll Base6 = Base(s, 6);
    div6 = divisor(Base6);
    if(div6 == -1) return 0;

    ll Base7 = Base(s, 7);
    div7 = divisor(Base7);
    if(div7 == -1) return 0;

    ll Base8 = Base(s, 8);
    div8 = divisor(Base8);
    if(div8 == -1) return 0;

    ll Base9 = Base(s, 9);
    div9 = divisor(Base9);
    if(div9 == -1) return 0;

    ll Base10 = Base(s, 10);
    div10 = divisor(Base10);
    if(div10 == -1) return 0;

    return 1;
}
string IntToString(ll n){
    string s;
    while(n){
        s+=(n%2)+'0';
        n/=2;
    }
    return s;
}

vector<string>foundS;
vector<ll>foundSol2, foundSol3, foundSol4, foundSol5, foundSol6, foundSol7, foundSol8, foundSol9, foundSol10;

int main() {
#ifndef ONLINE_JUDGE
//	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
int T, cnt = 0;
    arr[2][0]=1; arr[3][0]=1;
    arr[4][0]=1; arr[5][0]=1;
    arr[6][0]=1; arr[7][0]=1;
    arr[8][0]=1; arr[9][0]=1; arr[10][0]=1;
	p2=1, p3=1, p4=1, p5=1, p6=1, p7=1, p8=1, p9=1, p10=1;
	for (int i=1;i<33;i++)
	{
		p2*=2; p3*=3;
		p4*=4; p5*=5;
		p6*=6; p7*=7;
		p8*=8; p9*=9; p10*=10;
        arr[2][i]=p2; arr[3][i]=p3;
        arr[4][i]=p4; arr[5][i]=p5;
        arr[6][i]=p6; arr[7][i]=p7;
        arr[8][i]=p8; arr[9][i]=p9; arr[10][i]=p10;
	}
scanf("%d", &T);
while(T--){
    scanf("%d%d", &N, &j);
    ll start = arr[2][N-1], end = arr[2][N]-1;
    string s;
    for(ll i=start;i<=end;i++){
        if(!(i&1)) continue;
        s = IntToString(i);
        if(s[0] == '1' && s[sz(s)-1] == '1')
        if(j&&Check(s, i)){
                reverse(all(s));
                foundS.pb(s);
                foundSol2.pb(div2);
                foundSol3.pb(div3);
                foundSol4.pb(div4);
                foundSol5.pb(div5);
                foundSol6.pb(div6);
                foundSol7.pb(div7);
                foundSol8.pb(div8);
                foundSol9.pb(div9);
                foundSol10.pb(div10);
                j--;
        }
        else if(!j){
            break;
        }
    }

    printf("Case #%d:\n", ++cnt);
    for(int i=0;i<sz(foundS);i++){
        cout<<foundS[i]<<" ";
        printf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d\n", foundSol2[i], foundSol3[i], foundSol4[i], foundSol5[i], foundSol6[i], foundSol7[i], foundSol8[i], foundSol9[i], foundSol10[i]);
    }
    foundS.clear(), foundSol2.clear(), foundSol3.clear(), foundSol4.clear(), foundSol5.clear(), foundSol6.clear(), foundSol7.clear(), foundSol8.clear(), foundSol9.clear(), foundSol10.clear();
}
    return 0;
}

