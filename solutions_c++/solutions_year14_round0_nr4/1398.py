#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;
#define eps 1e-12
int n;
double w[2][100010];
bool vis[100010];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int T = 0, Cas = 0, n = 0;
	scanf("%d",&T); 
    while(T--)
    {
    	scanf("%d", &n);
    	for(int ss = 0; ss <= 1; ss++) {
    		for(int i = 1 ; i <= n; i++) {
    			scanf("%lf", &w[ss][i]);
    		}
    		sort(w[ss] + 1, w[ss] + 1 + n);

    		/*for(int i = 1 ; i <= n; i++) {
    			printf("%lf ", w[ss][i]);
    		}
    		puts("");*/
    	}

    	int st = 1, ed = n, ans = 0;
    	for(int i = 1; i <= n; i++) {
    		bool flag = true;
    		st = i, ed = 1;
    		for(int j = 1; j <= n - i + 1; j++) {
    			if(w[0][st] > w[1][ed]) {

    			} else {
    				flag = false;
    			}
    			st++,ed++;
    		}
    		if(flag) {
    			ans = max(ans, n - i + 1);
    		}
    		if(w[0][i] > w[1][n - i + 1]) {
    			break;
    		} else {

    		}
    	}
    	int ans2 = n;
    	memset(vis, false, sizeof(vis));
    	for(int i = 1; i <= n; i++) {
    		bool flag = false;
    		for(int j = 1; j <= n; j++) {
    			if(!vis[j]) {
    				if(w[1][j] > w[0][i]) {
    					vis[j] = 1;
    					//cout<<w[1][j]<<" > "<<w[0][i]<<endl;
    					flag = true;	
    					ans2--;
    					break;
    				}
    			}
    		}
    		if(!flag) {
    			for(int j = 1; j <= n; j++) {
	    			if(!vis[j]) {
	    				vis[j] = true;
	    				break;
	    			}
    			}
    		}
    	}
    	printf("Case #%d: %d %d\n", ++Cas, ans, ans2);
    	
    }
      	
}