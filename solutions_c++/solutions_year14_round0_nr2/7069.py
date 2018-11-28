/*"The Woods are lovely dark and deep,
But i have promises to keep,
Miles to go before i sleep and Miles to go before i Sleep"
*/
#include<bits/stdc++.h>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<string.h>
#define pb(n) push_back(n)
unsigned long long mod=1000000007;
using namespace std;
#define GI ({long int t;scanf("%ld",&t);t;})
#define all(x) x.begin(),x.end() //sort(all(x))
#define sz(h1) h1.size()
int main()
{
        int t=GI;
        double c,f,x,inc,initial;
        int trial=t;
        int i=1;
        while(t--)
                {
                        initial=2.0;
                        inc=0.0;
                        cin>>c>>f>>x;
                        while(i)
                        {
                          if(x/initial<=(c/initial+x/(initial+f)))
                          {
                          inc=inc+x/initial;
                          break;
                          }
                        inc=inc+c/initial;
                        initial=initial+f;
                        }
                        cout<<"Case #"<<trial-t;
                        printf(": %.7f\n",inc);
                        i++;
                }
      return 0;
}
