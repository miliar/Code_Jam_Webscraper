//Aditya Dixit
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <functional>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <cmath>
#include <numeric>
#include <set>

using namespace std;

#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#define LIM
#define MOD 1000000009
#define pb push_back
#define mp make_pair
#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )

const int INF = 2000000000;

typedef long long int i64;
typedef long int i32;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector <PII> VPII;

int vis[105];

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	std::ios_base::sync_with_stdio(false);
	int t,tt;
	cin >> t;
	
	while(t--)
	{
		tt++;
		int n;
		cin >> n;
		
		string a,b;
		cin >> a >> b;
		
		int flag = 0,i,k;
		int j,ctr1,ctr2;
		int ans = 0;
		for(i = 0,k = 0; i < (int)a.length() && k < (int)b.length();)
        {  
            if(a[i]!= b[k])
            {
                 flag=1;
                 break;
            }    
            
            j=i,ctr1=ctr2=0;
            for(;a[j] == a[i];i++)
             ctr1++;
            
            int l=k;
            for(;b[k] == b[l];k++)
             ctr2++;
            
            ans += (ctr1-ctr2 > 0 ? ctr1 - ctr2 : ctr2 - ctr1);
        }    
         
         cout << "Case #" << tt <<": ";    
        if(flag == 0 && i == (int)a.length() && k == (int) b.length() )
         cout << ans <<endl;
        else
         cout<<"Fegla Won\n"; 
	}
	
    return 0;
}

