/*
    Author : SHUBHAM SINGH
*/
 
#include<bits/stdc++.h>
 
using namespace std;
 
typedef long long ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef unsigned long long llu;

const ld PI = acos(-1.0);
 
#define lp(i,a,b) for(i=a;i<b;i++)
#define loop(i,a,b) for(i=a;i>=b;i--)
#define iter(j,a) for(vector<int>::iterator j = a.begin();j!=a.end();j++)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define gc getchar
#define mem(a,b) memset(a,b,sizeof(a));

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define allr(c) (c).rbegin(),(c).rend()

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
// #define PI 3.141592653589793238462643383279502884197169399375
#define __int64 9223372036854775807
#define unsigned__int64 18446744073709551615
#define mod 1000000007


int main(){
    ll i,j;
    ios_base :: sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    int m=1;

    while(t--){
      string s;
      cin >> s;
      cout << "Case #" << m << ": ";
      int n = s.size();

      int x=0,i=0;
      bool flag=true;
      while(i<n){
        if(s[i]=='-'){
          if(flag)
            x++;
          flag = false;
        }else{
          flag = true;
        }
        i++;
      }

      if(s[0]=='+')
        cout << 2*x << "\n";
      else
        cout << 2*x-1 << "\n";
      
      m++;
    }

    return 0;
}