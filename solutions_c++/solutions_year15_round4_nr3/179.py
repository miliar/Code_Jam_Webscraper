#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<map>
#include<string>
#include<vector>

using namespace std;

map <string,int> M;

vector <int> s[30];

string Str;

int E[3100],F[3100],_M,n,Ans,Now;

int main()
{
	int TestCase,Case,i,j,k,l;
//	freopen("c.in","rb",stdin);
//	freopen("c.out","wb",stdout);
	cin>>TestCase;
	for(Case=1;Case<=TestCase;Case++)
	{
		cin>>n;
		getline(cin,Str);
		_M=0;
		M.clear();
		for(i=0;i<n;i++)
		{
			getline(cin,Str);
			istringstream IN(Str);
			s[i].clear();
			for(;(IN>>Str)!=NULL;)
			{
				if(!M[Str])
					M[Str]=++_M;
				s[i].push_back(M[Str]);
			}
		}
		memset(E,0,sizeof(int)*(_M+10));
		memset(F,0,sizeof(int)*(_M+10));
		for(i=0;i<s[0].size();i++)
			E[s[0][i]]=1;
		for(i=0;i<s[1].size();i++)
			F[s[1][i]]=1;
		Ans=_M;
		Now=0;
		for(i=1;i<=_M;i++)
			if(E[i]&&F[i])
				Now++;
		for(i=0;i<(1<<(n-2));i++)
		{
			for(j=2;j<n;j++)
			if(i&(1<<j-2))
				for(k=0,l=s[j].size();k<l;k++)
				{
					E[s[j][k]]++;
					if(E[s[j][k]]==1&&F[s[j][k]])
						Now++;
				}
			else
				for(k=0,l=s[j].size();k<l;k++)
				{
					F[s[j][k]]++;
					if(F[s[j][k]]==1&&E[s[j][k]])
						Now++;
				}

			if(Now<Ans)
				Ans=Now;

			for(j=2;j<n;j++)
			if(i&(1<<j-2))
				for(k=0,l=s[j].size();k<l;k++)
				{
					E[s[j][k]]--;
					if(E[s[j][k]]==0&&F[s[j][k]])
						Now--;
				}
			else
				for(k=0,l=s[j].size();k<l;k++)
				{
					F[s[j][k]]--;
					if(F[s[j][k]]==0&&E[s[j][k]])
						Now--;
				}
			
			}
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
