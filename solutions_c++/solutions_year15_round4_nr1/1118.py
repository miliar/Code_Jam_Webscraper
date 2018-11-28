#include<iostream>
using namespace std;


int answer;
int N,M;
char s[1000][1000];
char str[]="<>^v";
int ii[256];
int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};
int T[1000][1000];
int a[10],b[10], c[10],d[10];
char ss[10][10];

bool dfs(int i,int j, char S[10][10])
{
	if(i<0||j<0||i==N||j==M) return true;
	if(T[i][j]) return false;
	T[i][j] = 1;
	int x = dx[ii[S[i][j]]]+i;
	int y = dy[ii[S[i][j]]]+j;
	return dfs(x,y,S);
}


void check(int cnt, char S[10][10])
{
	for(int i = 0; i <N; i++)
		for(int j = 0; j <M; j++)
			T[i][j]=0;
	for(int i = 0; i <N; i++)
		for(int j = 0; j <M; j++)
			if(!T[i][j] && S[i][j] != '.') 
			{
				if(dfs(i,j,S)) return;
			}
	answer = min(answer,cnt);
}


void gen(int i,int j,int cnt, char S[10][10])
{
	if(answer <= cnt) return;
	if(j==M)
	{
		j=0;
		i++;
	}
	if(i==N)
	{
		check(cnt,S);
		return;
	}
	gen(i,j+1,cnt,S);
	if(S[i][j]=='.') return;
	char ch = S[i][j];
	for(int d= 0; d < 4; d++)
	{
		if(ch != str[d])
		{
			S[i][j] = str[d];
			gen(i,j+1,cnt+1,S);
			S[i][j]=ch;
		}
	}
}

void magic()
{
	for(int i = 0; i < N; i++)
		for(int j  = 0; j < M; j++)
			T[i][j] = 0;
	for(int i = 0; i < N; i++)
	{
		a[i] = 1000;
		b[i] = -1;
		for(int j = 0; j < M; j++)
		{
			ss[i][j] = s[i][j];
			if(s[i][j]!='.')
			{
				a[i] = min(a[i], j);
				b[i] = max(b[i], j);
			}
		}
		if(a[i]!=1000 && b[i]!=-1 && a[i] != b[i])
		{
			if(s[i][a[i]]!='>') T[i][a[i]]=1;
			if(s[i][b[i]]!='<') T[i][b[i]]=1;
			ss[i][a[i]]='>';
			ss[i][b[i]]='<';
		}
	}
	for(int j = 0; j < M; j++)
	{
		c[j] = 1000;
		d[j] = -1;
		for(int i = 0; i < N; i++)
		{
			if(s[i][j]!='.')
			{
				c[j] = min(c[j], i);
				d[j] = max(d[j], i);
			}
		}
		if(c[j]!=1000 && d[j]!=-1 && c[j] != d[j])
		{
			if(s[c[j]][j]!='v') T[c[j]][j]=1;
			if(s[d[j]][j]!='^') T[d[j]][j]=1;
			ss[c[j]][j]='v';
			ss[d[j]][j]='^';
		}
	}
	int cnt = 0;
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j <M; j++)
		{
			if(ss[i][j]!='.')
			{
				if(a[i]!=b[i] && b[i]>=0)
				{
					if(ss[i][j]=='>'||ss[i][j]=='<') continue;
				}
				if(c[j]!=d[j] && d[j]>=0)
				{
					if(ss[i][j]=='^' || ss[i][j]=='v') continue;
				}
				if(a[i]!=b[i] && b[i]>=0)
				{
					T[i][j]=1;
					ss[i][j]='>';
					continue;
				}
				if(c[j]!=d[j] && d[j]>=0)
				{
					T[i][j]=1;
					ss[i][j]='^';
					continue;
				}

			}

		}
	}
	for(int i = 0; i < N; i++)
		for(int j  = 0; j < M; j++)
			if(T[i][j]) cnt++;
	check(cnt,ss);

}

int row[1000],col[1000];
int cc[1000],rr[1000];
void magic1()
{
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
		{
			row[i]=rr[i]=0;
			col[j]=cc[j]=0;
		}
	int cnt = 0;
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
			if(s[i][j]!='.') 
			{
				rr[i]++;
				cc[j]++;
			}
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
		{
			if(s[i][j]=='^' && !col[j])
			{
				cnt++;
			}
			if(s[i][j]=='<' && !row[i])
			{
				cnt++;
			}
			if(s[i][j]=='v')
			{
				if(col[j] +1 == cc[j]) 
				{
					cnt++;
				}
			}
			if(s[i][j]=='>')
			{
				if(row[i]+1 ==rr[i])
				{
					cnt++;
				}
			}
			if(s[i][j]!='.' &&rr[i]==1 && cc[j] ==1) return;
			if(s[i][j]!='.')
			{
				row[i]++;
				col[j]++;
			}
		}
	answer = cnt;
}

void magic2()
{
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
		{
			row[i]=rr[i]=0;
			col[j]=cc[j]=0;
		}
	int cnt = 0;
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
			if(s[i][j]!='.') 
			{
				rr[i]++;
				cc[j]++;
			}
	for(int i = 0; i <N; i++)
		for(int j = 0; j < M; j++)
		{
			if(s[i][j]=='^' && col[j])
			{
				cnt++;
			}
			if(s[i][j]=='<' && !row[i])
			{
				cnt++;
			}
			if(s[i][j]=='v')
			{
				if(col[j] +1 == cc[j]) 
				{
					cnt++;
				}
			}
			if(s[i][j]=='>')
			{
				if(row[i]+1 ==rr[i])
				{
					cnt++;
				}
			}
			if(rr[i]==1 && cc[j] ==1) return;
			row[i]++;
			col[j]++;
		}

}






void solve(int test)
{
	
	scanf("%d%d",&N,&M);
	answer = N*M*2;
	for(int i = 0; i <N;i++)
	{
		scanf("%s",&s[i]);
	//	printf("%s\n",s[i]);
	}
	magic1();
	//printf("magic: %d\n",answer);
	//if(answer != N*M*2)	gen(0,0,0,s);
	if(N*M*2==answer) printf("Case #%d: IMPOSSIBLE\n", test);
	else printf("Case #%d: %d\n",test, answer);

}



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	for(int i = 0; i < 4; i++) ii[str[i]]=i;
	int TT;
	scanf("%d",&TT);
	for(int i =1; i <=TT; i++) solve(i);
	return 0;
}