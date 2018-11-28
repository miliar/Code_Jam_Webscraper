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
ll number(ll num, ll base){
    ll res = 0, mul = 1;
    while(num){
        res = res + mul * (num % 10);
        mul *= base;
        num /= 10;
    }
    return res;
}

ll is_prime(ll num){
    for(ll i = 2; i * i <= num; i++){
        if(num % i == 0 ) return i;
    }
    return 0;
}
int main(){
freopen("ip.txt", "r", stdin);
freopen("output.txt", "w", stdout);
int t, cnt = 1;
cin >> t;
ll arr[]={1000000000000001,
1000000000000101,
1000000000000111,
1000000000001001,
1000000000001101,
1000000000010011,
1000000000011001,
1000000000011011,
1000000000011111,
1000000000100101,
1000000000101011,
1000000000101111,
1000000000110001,
1000000000110101,
1000000000110111,
1000000000111011,
1000000000111101,
1000000001000011,
1000000001001001,
1000000001001111,
1000000001010101,
1000000001010111,
1000000001011001,
1000000001011011,
1000000001011101,
1000000001011111,
1000000001100001,
1000000001100011,
1000000001100111,
1000000001101011,
1000000001101101,
1000000001110011,
1000000001110101,
1000000001111001,
1000000001111011,
1000000001111101,
1000000001111111,
1000000010000011,
1000000010000101,
1000000010001001,
1000000010010001,
1000000010010111,
1000000010011001,
1000000010011011,
1000000010011101,
1000000010100011,
1000000010100111,
1000000010101001,
1000000010110011,
1000000010110101,
1000000010111001};
while(t--){
    ll n,j;
    cin >> n >> j;
    printf("Case #%d:\n", cnt++);
    int sz = sizeof(arr) / sizeof(ll);
    for(int i = 0; i < 50; i++){
        cout << arr[i] << " ";
        for(int j = 2; j <= 10; j++){
            ll num = number(arr[i], (ll)j);
            cout << is_prime(num) << " ";
        }
        printf("\n");
    }
}
return 0;
}
