//coder: handa.vikalp
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int main(int argc, char const *argv[])
{
	FILE *input = freopen("A-large.in","r", stdin);
	FILE *output = freopen("A-large-1.out", "w", stdout);

	int T,i;
	scanf("%d",&T);
	for(int t = 1; t<=T; ++t)
	{
		int smax, count=0, upman=0;
	    char s[1005];
        scanf("%d", &smax);
	    scanf("%s", s);
              
        if(0==smax) count=0;
        else
        {
            upman=s[0]-'0';
            for(i=1;i<=smax;i++)
            {
                if( (0 != (s[i]-'0')) && ((i-upman) >0) ) 
                {
                    int diff = i-upman;
                    count += diff;   
                    upman += diff;
                }
                upman += s[i]-'0';
            }
        }
        
		printf("Case #%d: %d\n", t, count);
	}

	fclose(input);
	fclose(output);
	return 0;
}
