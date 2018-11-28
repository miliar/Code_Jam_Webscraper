/* Code and Temmplate by sumit.asr@gmail.com */

#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef double ld;
typedef vector<ld> vld;

#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i, n) for(int i = 0; i < (int)(n); i++) //int ascending
#define repc(i, a, n) for(int i = (int)(a); i < (int)(n); i++) //customized
#define repd(i, n) for(int i = (int)(n) - 1; i >= 0; i--) //int descending
#define repl(i,n)   for(ll i=0;i<n;i++)

#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)

#define MEM(a,b)      memset(a,(b),sizeof(a))  //memset(arr,0,sizeof(arr))
#define MOD           1000000007

/*
void rec(stack<char> mystack)
{


}
*/

int main()
{
	//ios_base::sync_with_stdio(false) ; cin.tie(0);
    freopen("B-large.in", "r", stdin);
    freopen("Blarout.txt", "w", stdout);

    int t;
    cin>>t;

    for(int test = 1 ;test <= t; test ++ )
    {
        string s;
        cin>>s;

        int len = s.size();
        int flag = 0;
        int ans = 0;
        //int right_side = len - 1;

        while (flag != 1)
        {
            int count=0;
            for(int i=0;i<len;i++)
                if(s[i]=='+')
                    count++;
            

            if(count==len)
            {
                flag=1;
            }
            else
            {
                //--+----+++
                //      ^
                //      len       
                for(int j=len-1;j>=0;j--)            
                {
                    if(s[j]=='-')
                    {   
                        break;
                    }
                    else
                        len =j;
                }

                if(s[0]=='-')
                {
                    string temp;
                    for(int k =len-1;k>=0;k--)
                    {
                        if(s[k]=='+')
                        temp.push_back('-');
                        else
                        temp.push_back('+');
                    }

                    for(int k=0;k<len;k++)
                    {
                        s[k]=temp[k];
                    }

                    ans++;

                }
                else
                {

                        int rev_point;
                        for(int j = len-1 ; j >=0 ; j--)
                        {
                            if(s[j] == '+')
                            {
                                rev_point=j+1;
                                break;
                            }

                        }

                        string temp;
                        for(int k =rev_point-1;k>=0;k--)
                        {
                            if(s[k]=='+')
                            temp.push_back('-');
                            else
                            temp.push_back('+');
                        }

                        for(int k=0;k<rev_point;k++)
                        {
                            s[k]=temp[k];
                        }

                        ans++;


                }




            }

        }

        
        cout<<"Case #"<<test<<": "<<ans<<endl;

    }

	return 0;
}
