#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

#define INF 2147483647
#define LINF 9223372036854775807
#define mp make_pair
#define pb push_back

typedef long long int lli;
typedef pair<int,int> pi;

int main ()
{
	int t;
	cin>>t;
	for(int T = 1;T <= t;T++)
	{
			string str[1000];
			int n;
			cin>>n;
			
			for(int i=0;i<n;i++)
			{
				cin>>str[i];
			}
			
			int ct[200][200];
			int cu[200][200];
			
			int check=0;
			
			char st[200][200];
			int len[200];
			
			for(int i=0;i<n;i++)
			{
				int k=0;
				for(int j=0;j<str[i].size();j++)
				{
					st[i][k] = str[i][j];
					ct[i][k]=0;
					cu[i][k]=0;
					while(j< str[i].size() && st[i][k]== str[i][j])
					{
						j++;
						ct[i][k]++;
					}
					j--;
					cu[i][k] = ct[i][k];
					
					if(i!=0)
					{
						if(st[i][k] != st[i-1][k])
						{
							check=1;
							//break;
						}
						cu[i][k] += cu[i-1][k];
					}
					
					k++;
				}
				len[i]=k;
				if(i!=0)
				{
					if(len[i]!=len[i-1])
					{
						check=1;
						//break;
					}
				}
			}
			

			if(check==1)
			{
				cout<<"Case #"<<T<<": "<<"Fegla Won\n";
				continue;
			}
			int moves =0;
			for(int i=0;i<len[0];i++)
			{
				int rnd = round(((float)cu[n-1][i])/n);
				for(int j=0;j<n;j++)
				{
					moves += abs(rnd - ct[j][i]);
				}
			}
			cout<<"Case #"<<T<<": "<<moves<<endl;
		}
		return 0;
		
	}

