//---------------------------JUGNU: LET YOUR LIGHT SHINE---------------------------//
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%d",&a)
#define sm(a,b) scanf("%d%d", &a, &b)
#define pr(a) printf("%d\n", a)
#define pm(a,b) printf("%d %d\n", a, b)
#define cn(a) cin >> a
#define ct(a) cout << a << endl
#define isset(x,i) ((x>>i)&1)
#define MAXN 100005
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline printf("---------------------------\n");
using namespace std;
int nums[40];
void printResult(int  n)
{
	int i;
	frr(i, n-1, 0) printf("%d", nums[i]);
	fre(i, 2, 10) printf(" %d", i+1);
	printf("\n");
	return;
}
int main()
{
	int i, j, t, n, m, k, l, r, mini,cnt, maxi, temp, flag, result;
	sc(t);
	sm(n, m);
	nums[0] = 1;
	nums[n-1] = 1;
	if(n%2) temp = 2;
	else temp = 0;
	cnt = 0;
	printf("Case #1:\n");
	while(cnt != m)
	{
		if(temp == 0)
		{
			printResult(n);
			cnt++;	
		}
		for(i = 1; i < n-1 && cnt != m; i++)
		{
			for(j = i+1; j < n-1 && cnt != m; j++)
			{
				flag = temp;
				if(j%2) flag += -1;
				else flag += 1;
				if(i%2) flag += -1;
				else flag += 1;
				if(flag == 0)
				{
					nums[i] = 1;
					nums[j] = 1;
					printResult(n);
					cnt++;
					nums[i] = 0;
					nums[j] = 0;
				}
			}
		}
		for(i = 1; i < n-1 && cnt != m; i++)
		{
			for(j = i+1; j < n-1 && cnt != m; j++)
			{
				for(k = j + 1; k < n-1 && cnt != m; k++)
				{
					for(l = k + 1; l < n-1 && cnt != m; l++)
					{
						flag = temp;
						if(j%2) flag += -1;
						else flag += 1;
						if(i%2) flag += -1;
						else flag += 1;
						if(k%2) flag += -1;
						else flag += 1;
						if(l%2) flag += -1;
						else flag += 1;
						if(flag == 0)
						{
							nums[i] = 1;
							nums[j] = 1;
							nums[k] = 1;
							nums[l] = 1;
							printResult(n);
							cnt++;
							nums[i] = 0;
							nums[j] = 0;
							nums[k] = 0;
							nums[l] = 0;
						}
					}
				}
			}
		} 
	}
return 0;
}
