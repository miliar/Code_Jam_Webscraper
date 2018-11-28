//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)

#define si(n) scanf("%d", &n)
#define sll(l) scanf("%lld",&l)
#define ss(s) scanf("%s", s)
#define sc(c) scanf("%c", &c)
#define sd(f) scanf("%lf", &f)

#define pi(n) printf("%d\n", n)
#define pll(l) printf("%lld\n", l)
#define ps(s) printf("%s\n", s)
#define pc(c) printf("%c\n", c)
#define pd(f) printf("%lf\n", f)

#define debug(x) cout<<"\n#("<<x<<")#\n"
#define nline printf("\n")

#define mem(a,i) memset(a,i,sizeof(a))

#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define PB push_back
#define SZ size
#define MP make_pair
#define fi first
#define sec second

std::vector<int> v[30], cols[15], rows[15], ans;
int N;

std::vector<std::vector<int> > mat;
bool vis[30];

int main()
{
	int i, j, k;

	int cases;
	si(cases);

	int caseNo = 1;

	wl(cases)
	{

		cin>>N;

		fl(i,0,2*N)
			v[i].clear();
		ans.clear();


		fl(i,0,2*N - 1)
		{
			fl(j,0,N)
			{
				int temp;
				cin>>temp;
				v[i].PB(temp);
			}
		}

		sort(v,v+(2*N)-1);

		int limit = 1<<(2*N - 1);

		fl(i,0,limit)
		{
			if(__builtin_popcount(i) != N)
				continue;

			mat.clear();
			fl(j,0,N)
			{
				rows[j].clear();
				cols[j].clear();
			}
			fl(j,0,(2 * N) - 1)
				vis[j] = 0;

			fl(j,0,(2*N)-1)
			{
				if(i&(1<<j))
				{
					//cout<<j<<" ";
					mat.PB(v[j]);
				}
			}
			//nline;

			/*fl(j,0,N)
			{
				fl(k,0,N)
					cout<<mat[j][k];
				nline;
			}*/

			bool colIncreasing = 1, rowIncreasing = 1;

			fl(j,0,N)
			{
				fl(k,1,N)
				{
					if(mat[j][k] <= mat[j][k - 1])
						rowIncreasing = 0;
				}
			}

			

			fl(k,0,N)
			{
				fl(j,1,N)
				{
					if(mat[j][k] <= mat[j - 1][k])
					{
						colIncreasing = 0;
					}
				}
			}

			//cout<<colIncreasing<<" "<<rowIncreasing; nline;

			fl(k,0,N)
			{
				fl(j,0,N)
				{
					cols[k].PB(mat[j][k]);
				}
			}

			if(rowIncreasing && colIncreasing)
			{

				fl(j,0,N)
				{
					fl(k,0,(2*N) - 1)
					{
						if(mat[j] == v[k] && !vis[k])
						{

							vis[k] = 1;
							break;
						}
					}
				}

				fl(j,0,N)
				{
					fl(k,0,(2*N) - 1)
					{
						if(cols[j] == v[k] && !vis[k])
						{
							vis[k] = 1;
							break;
						}
					}
				}

				bool gotAns = 1;

				fl(j,0,(2*N) - 1)
					if(!vis[j])
					{
						gotAns = 0;
					}

				if(!gotAns)
					continue;

				/*fl(j,0,N)
				{
					fl(k,0,N)
						cout<<mat[j][k];
					nline;
				}*/

				break;
			}
		}

		int gotIt = 0;

		fl(i,0,(2*N) - 1)
			vis[i] = 0;

		fl(j,0,N)
		{
			int f = 0;
			fl(k,0,(2*N) - 1)
			{
				if(mat[j] == v[k] && !vis[k])
				{
					vis[k] = 1;
					f = 1;
					break;
				}
			}

			if(!f)
				ans = mat[j];
		}

		fl(j,0,N)
		{
			int f = 0;
			fl(k,0,(2*N) - 1)
			{
				if(cols[j] == v[k] && !vis[k])
				{
					vis[k] = 1;
					f = 1;
					break;
				}
			}
			if(!f)
				ans = cols[j];
		}




		cout<<"Case #"<<caseNo<<": ";
		caseNo++; 
		fl(i,0,N)
			cout<<ans[i]<<" ";
		nline;
	}


	return 0;
}
/*
	Powered by Buggy Plugin
*/
