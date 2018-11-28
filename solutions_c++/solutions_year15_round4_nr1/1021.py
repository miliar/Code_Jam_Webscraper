#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef unsigned long long llu;
#define loop(i,a,b) for(i=a;i<b;i++)
#define iter(j,a) for(vector<int>::iterator j = a.begin();j!=a.end();j++)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define gc getchar   

int ri() {
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  int ret = 0;
  while(c>='0' && c<='9') {
	ret = 10 * ret + c - 48;
	c = gc();
  }
  return ret;
}

ll rl()
{
	char c = gc();
	while(c<'0' || c>'9') c = gc();
	ll ret = 0;
	while(c>='0' && c<='9') {
		ret = 10 * ret + c - 48;
		c = gc();
	}
	return ret;		
}

string rs()
{
	char c = gc();
	while(c=='\n' || c==' ') c=gc();
	string ret="";
	while(c!=10 && c!=' ')
	{
		ret+=c;
		c=gc();
	}
	return ret;
}

char rc()
{
	char c = gc();
	while(c=='\n' || c==' ') c=gc();
	return c;
}

ll gri[101][101],r,c;

ll flag1(ll i,ll j)
{
	//cout<<"here"<<endl;
	ll k,ret = -1;
	for(k=i-1;k>=0;k--)
	{
		if(gri[k][j]!='.')
		{
			ret = k;
			break;
		}
	}
	return ret;
}

ll flag2(ll i,ll j)
{
	ll k,ret = -1;
	for(k=j+1;k<c;k++)
	{
		if(gri[i][k]!='.')
		{
			ret = k;
			break;
		}
	}
	return ret;
}

ll flag3(ll i,ll j)
{
	ll k,ret = -1;
	for(k=i+1;k<r;k++)
	{
		if(gri[k][j]!='.')
		{
			ret = k;
			break;
		}
	}
	return ret;
}

ll flag4(ll i,ll j)
{
	ll k,ret = -1;
	for(k=j-1;k>=0;k--)
	{
		if(gri[i][k]!='.')
		{
			ret = k;
			break;
		}
	}
	return ret;
}

int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t=rl(),caseno=0,i,j,k,n,p,x,y,temp,dir,flag,imp=0,count;
	
	while(t--)
	{
		caseno++;
		r=rl();c=rl();
		imp=0;
		count=0;
		loop(i,0,r)
		{
			loop(j,0,c)
			{
				gri[i][j]=rc();
				if(gri[i][j]!='.')
				{
					if(gri[i][j]=='^')
						gri[i][j] = 1;
					else
						if(gri[i][j]=='>')
							gri[i][j]=2;
						else
							if(gri[i][j]=='v')
								gri[i][j]=3;
							else
								gri[i][j]=4;
				}
			}
		}
		loop(i,0,r)
		{
			loop(j,0,c)
			{
				if(gri[i][j]!='.') // its an arrow
				{
					//cout<<"its an arrow="<<gri[i][j]<<endl;
					flag = 1;
					dir = gri[i][j];
					if(dir == 1)
					{
						if(flag1(i,j)!=-1) // if a flag in same direction
							continue;
						else
						{
							if(flag3(i,j)!=-1) // flag in down direction
							{
								gri[i][j]=3;
								count++;
							}
							else
							{
								if(flag2(i,j)!=-1)
								{
									gri[i][j]=2;
									count++;
								}
								else
								{
									if(flag4(i,j)!=-1)
									{
										gri[i][j]=4;
										count++;
									}
									else
										imp=1;
								}
							}
						}
					}
					else
					{
						if(dir == 2)
						{
							if(flag2(i,j)!=-1) // if a flag in same direction
								continue;
							else
							{
								if(flag3(i,j)!=-1) // flag in down direction
								{
									gri[i][j]=3;
									count++;
								}
								else
								{
									if(flag1(i,j)!=-1)
									{
										gri[i][j]=2;
										count++;
									}
									else
									{
										if(flag4(i,j)!=-1)
										{
											gri[i][j]=4;
											count++;
										}
										else
											imp=1;
									}
								}
							}
						}
						else
						{
							if(dir == 3)
							{
								if(flag3(i,j)!=-1) // if a flag in same direction
									continue;
								else
								{
									if(flag2(i,j)!=-1) // flag in down direction
									{
										gri[i][j]=3;
										count++;
									}
									else
									{
										if(flag1(i,j)!=-1)
										{
											gri[i][j]=2;
											count++;
										}
										else
										{
											if(flag4(i,j)!=-1)
											{
												gri[i][j]=4;
												count++;
											}
											else
												imp=1;
										}
									}
								}
							}
							else
							{
								if(flag4(i,j)!=-1) // if a flag in same direction
									continue;
								else
								{
									if(flag2(i,j)!=-1) // flag in down direction
									{
										gri[i][j]=3;
										count++;
									}
									else
									{
										if(flag1(i,j)!=-1)
										{
											gri[i][j]=2;
											count++;
										}
										else
										{
											if(flag3(i,j)!=-1)
											{
												gri[i][j]=4;
												count++;
											}
											else
												imp=1;
										}
									}
								}
							}
						}
					}
				}
			}
		}
		if(imp)
			cout<<"Case #"<<caseno<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<caseno<<": "<<count<<endl;
	}
	return 0;
}