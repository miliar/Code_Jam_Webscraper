
#pragma comment(linker,"/STACK:16777216")
#pragma  warning ( disable: 4786)
#include <bits/stdc++.h>
using namespace std;

#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))

#define forl(i,a,b) for ( i = a; i < b; i++)
#define fore(i,a,b) for ( i = a; i <= b; i++)
#define forrev(i,a,b) for ( i = a; i >= b; i--)
#define MID(a, b) (a + ((b - a) >> 1))
#define pb push_back
typedef long long  LL;
#define in(a,b,c) ((a) <= (b) && (b) <= (c))
#define ms(a,b) memset((a),(b),sizeof(a))

#define all(v) (v).begin(),(v).end()
#define pb push_back
#define ull unsigned long long int
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

string to_string(long long x) { stringstream ss; ss << x; return ss.str(); }
long long to_int(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

#define MAX 105
#define INF 9999999

int main(void)
{
    freopen("B-large.in", "r", stdin);
    freopen("2_large.txt", "w", stdout);
    int t;
    int ca=1;
    cin >> t;
    getchar();
    int i,j,k;
    char in[MAX];
    int arr[MAX];
    int n;
    while(t--){
        gets(in);
        n = strlen(in);
        cout << "Case #" << ca++ << ": ";
        int ans = 0;
        forl(i,0,n){
            if(in[i] == '-'){
                arr[i] = 0;
            }else{
                arr[i] = 1;
            }
        }
        for(i=n-1;i>=0;i--){
           j = i;
           k=j;
           while(j>=0 && arr[j] == 1){
              k = j;
              j--;
           }
           if(j>=0){
              ans++;
              while(j>=0){
                  arr[j] ^= 1;
                  j--;
              }
           }
           i = k;
        }
        cout << ans << endl;
        
    }
    return 0;
}
