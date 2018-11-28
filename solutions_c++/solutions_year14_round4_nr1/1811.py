#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

vector<int> da;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	
	int t;
	scanf("%d",&t);
	for(int cnt=1;cnt<=t;cnt++)
	{
	    int n,x;
		scanf("%d%d",&n,&x);
		da.resize(n);
		for(int i=0; i<n; i++)
            scanf("%d",&da[i]);
		sort(da.begin(),da.end());
		int ans = 0;
		for(int i=0,j=n-1; i<=j; )
        {
            ans++;
            if(i==j)
                break;
            if(da[i]+da[j]<=x)
            {
                i++;
                j--;
            }
            else
                j--;
        }
        
		printf("Case #%d: %d\n",cnt,ans);
	} 
} 
