/* https://code.google.com/codejam/contest/6254486/dashboard */

#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
#define rep(i,a,n) for(__typeof(n) i = a; i < n; ++i)
#define repe(i,a,n) for(__typeof(n) i = a; i <= n; ++i)
#define mfill(a,b) memset(a, b, sizeof(a))
#define all(a) a.begin(), a.end()
#define pb(a) push_back(a)
#define dbg(x) {cout<<__LINE__ <<"::" << #x << ": " << (x) << endl; }


int main()
{
    ios_base::sync_with_stdio(false);
  freopen("A-large.in","r",stdin);
  freopen("large_sheep.out ","w",stdout);
    int t;
    cin>> t;

    repe(_case, 1, t)
    {
        ll n,answer = 0 ,temp = 0, multiplier = 1, count = 0;
        bool number_seen[10] = {0};

        cin >> n;
        if( n == 0){
            cout << "Case #" << _case << ": " << "INSOMNIA" << "\n";
        }
        else{
            while(true){

                answer = multiplier++ * n;
                temp = answer;
                while(temp > 0){
                    if( !number_seen[temp % 10]){
                        number_seen[temp % 10] = 1;
                        ++count;
                    }
                    temp /= 10;
                }
                if(count == 10 )
                    break;


            }
            cout << "Case #" << _case << ": " << answer << "\n";
        }
    }
    return 0;
}
