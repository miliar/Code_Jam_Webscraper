#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

string s[10];
int LP[10][10];
int siz[10];
int cur[10];

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++)
	{
		int M, N;
		cin >> M >> N;
		
		for(int i=0; i<M; i++)
			cin >> s[i];
		
		for(int i=0; i<M; i++)
			for(int j=0; j<M; j++)
			{
				LP[i][j]=0;
				int si=s[i].size(), sj=s[j].size();
				while(LP[i][j]<si && LP[i][j]<sj && s[i][LP[i][j]]==s[j][LP[i][j]])
					LP[i][j]++;
			}
		
		long long tope=1;
		for(int i=0; i<M; i++)
		{ 
			siz[i]=s[i].size();
			tope*=N;
		}
		int ans=0, cant=1;
		for(long long mask=0; mask<tope; mask++)
		{
			long long tmpmask=mask, curans=0;
			for(int i=0; i<M; i++)
			{
				cur[i]=tmpmask%N;
				tmpmask/=N;
				
				int bestpref=0, found=0;
				for(int j=0; j<i; j++)
				if(cur[i]==cur[j])
				{
					found=1;
					bestpref=max(bestpref, LP[i][j]);
				}
				
				curans+=siz[i]-bestpref;
				if(found==0) curans++;
			}
			
			if(curans>ans)
			{
				cant=0;
				ans=curans;
			}
			
			if(curans==ans) cant++;
		}
		
		cout << "Case #" << tc << ": " << ans << " " << cant << endl;
	}
}
