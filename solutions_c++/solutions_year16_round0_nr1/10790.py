/* Bismillahir rahmanir rahim */
//#pragma comment(linker, "/STACK:36777216")

#include <bits/stdc++.h>

using namespace std;

#define pi          acos(-1.0)
#define eps         1e-9

#define rep(i, n)       for(int i = 0; i < (n); i++)
#define reps(i, a, b)   for(int i= (a); i <= (b); i++)
#define fill(a, v)      memset(a, v, sizeof (a))
#define pb              push_back
#define pf              push_front
#define mp              make_pair
#define all(a)          (a).begin(),(a).end()

template<class T> inline T gcd(T a, T b)    { return b == 0 ? a : gcd(b, a % b); }
template<class T> inline T lcm(T a, T b)    { return (a / gcd(a, b)) * b; }

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;

#define siz         2147483647

//int diri[] = {0, 1, 0, -1, -1, 1, 1, -1};
//int dirj[] = {1, 0, -1, 0, 1, 1, -1, -1};

int main() {
//    clock_t start = clock();
//    ios_base::sync_with_stdio(false);
//    cin.tie(NULL);
//    #ifndef ONLINE_JUDGE
//        freopen("in.txt","r",stdin);
//        freopen("Output.txt","w",stdout);


    int t, n, cas = 1;
    int arr[19];
    LL temp;
    bool flag;
    cin >> t;
    while( t-- ) {
        memset(arr, 0, sizeof arr);
        cin >> n;
        for(int i = 1; i <= 1000; i++) {
            temp = n * i;
            LL temp2 = temp;
            while( temp2 > 0 ) {
                arr[ temp2 % 10 ] = 1;
                temp2 /= 10;
            }
            flag = true;
            for(int j = 0; j < 10; j++) {
                if( arr[j] == 0 ) {
                    flag = false;
                }
            }
            if( flag ) {
//                cout << "i = " << i << endl;
                break;
            }

//            cout << "temp = " << temp << endl;
        }
//        printf("Case #%d: ", cas++);

        cout << "Case #" << cas++ << ": ";
        if( flag )
            cout << temp << endl;
        else
            cout << "INSOMNIA" << endl;
    }
//    #endif
//    clock_t final = clock()-start;
//    cerr<<endl<<final/ (double) CLOCKS_PER_SEC<<endl;
    return 0;
}
