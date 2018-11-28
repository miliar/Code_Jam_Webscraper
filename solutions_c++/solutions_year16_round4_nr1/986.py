#include <bits/stdc++.h>
using namespace std;

int V[1<<15];
int N,R,P,S;
void build(int id)
{
	if (id >= 1<<(N+1)) return;
	V[id*2] = V[id];
	V[id*2+1] = (V[id]-1+3)%3;
	if ((V[id*2]==0&&V[id*2+1]==1)||(V[id*2]==0&&V[id*2+1]==2)||(V[id*2]==2&&V[id*2+1]==1)) swap(V[id*2],V[id*2+1]);
	build(id*2);
	build(id*2+1);
}

int main()
{
	//ios_base::sync_with_stdio(false);
	int T; int cnt[3];
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		cin >> N >> R >> P >> S;
		vector<string> vt;
		V[1] = 0;
		build(1);
		
		cnt[0] = cnt[1] = cnt[2] = 0;
		for (int i = 1<<N; i < 1<<(N+1); i++)
			cnt[V[i]]++;
		if (cnt[0]==R && cnt[1]==P && cnt[2]==S)
		{
			string s;
			for (int i = 1<<N; i < 1<<(N+1); i++)
			{
				if (V[i]==0) s += "R";
				else if (V[i]==1) s += "P";
				else s += "S";
			}
			for (int i = 0; i < s.size(); i+=2)
				if (s[i]>s[i+1]) swap(s[i],s[i+1]);
			for (int k = 2; k <= 1<<(N-1); k*=2)
				for (int i = 0; i < s.size(); i+=2*k)
					if (string(s.begin()+i,s.begin()+i+k)>string(s.begin()+i+k,s.begin()+i+2*k)) swap_ranges(s.begin()+i,s.begin()+i+k,s.begin()+i+k);
			vt.push_back(s);
		}
		else
		{
			V[1] = 1;
			build(1);
			cnt[0] = cnt[1] = cnt[2] = 0;
			for (int i = 1<<N; i < 1<<(N+1); i++)
				cnt[V[i]]++;
			if (cnt[0]==R && cnt[1]==P && cnt[2]==S)
			{
				string s;
				for (int i = 1<<N; i < 1<<(N+1); i++)
				{
					if (V[i]==0) s += "R";
					else if (V[i]==1) s += "P";
					else s += "S";
				}
				for (int i = 0; i < s.size(); i+=2)
					if (s[i]>s[i+1]) swap(s[i],s[i+1]);
			for (int k = 2; k <= 1<<(N-1); k*=2)
				for (int i = 0; i < s.size(); i+=2*k)
					if (string(s.begin()+i,s.begin()+i+k)>string(s.begin()+i+k,s.begin()+i+2*k)) swap_ranges(s.begin()+i,s.begin()+i+k,s.begin()+i+k);
				vt.push_back(s);
			}
			else
			{
				V[1] = 2;
				build(1);
				cnt[0] = cnt[1] = cnt[2] = 0;
				for (int i = 1<<N; i < 1<<(N+1); i++)
					cnt[V[i]]++;
				if (cnt[0]==R && cnt[1]==P && cnt[2]==S)
				{
					string s;
					for (int i = 1<<N; i < 1<<(N+1); i++)
					{
						if (V[i]==0) s += "R";
						else if (V[i]==1) s += "P";
						else s += "S";
					}
					for (int i = 0; i < s.size(); i+=2)
						if (s[i]>s[i+1]) swap(s[i],s[i+1]);
			for (int k = 2; k <= 1<<(N-1); k*=2)
				for (int i = 0; i < s.size(); i+=2*k)
					if (string(s.begin()+i,s.begin()+i+k)>string(s.begin()+i+k,s.begin()+i+2*k)) swap_ranges(s.begin()+i,s.begin()+i+k,s.begin()+i+k);
					vt.push_back(s);
				}
			}
		}
		if (vt.size()>0)
		{
			sort(vt.begin(),vt.end());
			printf("%s\n", vt[0].c_str());
		}
		else printf("IMPOSSIBLE\n");
	}
}
