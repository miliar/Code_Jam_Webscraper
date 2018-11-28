#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <fstream>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

int m[5][5] = { {0,0,0,0,0},{0,1,2,3,4}, {0, 2,-1,4,-3}, {0,3,-4,-1,2},{0,4,3,-2,-1}};

int t, l, x;
char o;
int oi;
char s1[10005], s2[10005];
bool yes = 0;
	
int mul(int left, int right)
{
		int v1,v2, value;
	//	cout<<"l "<<left<<" r "<<right<<endl;
		if (left==right)
			return (s2[left]-'0');
		v1 = mul(left, (left+right)/2);
		v2 = mul((left+right)/2+1, right);
		
		if (v1<0)
		{
			 if (v2<0)
			 	return m[-v1][-v2];
			return -m[-v1][v2];
		}
		if (v2<0)
		{
			return -m[v1][-v2];
		}
		return m[v1][v2];
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.out");
	/*for (int j=0;j<5;j++)
		{
			for (int k=0;k<5;k++)
				cout<<m[j][k]<<' ';
			cout<<endl;
		}
		cout<<endl;
	*/
	fin>>t;
	REP(i,1,t)
	{
		fin>>l;
		fin>>x;
		fin>>s1;
		REP(j,0, l*x-1)
		{
			o = s1[j%l];
			s2[j] = (o == 'i')?'2':(o == 'j' ? '3': '4'); 
		}
		s2[l*x] = '\0';
		int tr1=1,tr2=1,tr3=1;
		yes = 0;
		
		REP(j,0,l*x-3)
		{
			oi = s2[j]-'0'; 
			//cout<<"oi"<<' '<<oi<<endl;
			//cout<<"tr"<<' '<<tr1<<endl;
			if (tr1<0)
				tr1 = -m[-tr1][oi];
			else
			{
				tr1 = m[tr1][oi];
			//	cout<<"get p\n";
			}
			//cout<<"h "<<m[tr1][oi]<<endl;	
			//cout<<"o "<<tr1<<endl;
			if (tr1==2)
			{
				tr3 = 1;
				for (int k=l*x-1;k>=j+2;k--)
				{
					oi = s2[k]-'0'; 
					if (tr3<0)
						tr3 = -m[oi][-tr3];
					else
						tr3 = m[oi][tr3];
					if (tr3==4)
					{
						tr2=mul(j+1,k-1);
						if (tr2==3)
						{
							yes=1;
							break;
						}
						break;
					}
				}
				if (yes)
					break;
				break;
			}
			
		}
		
		/*
		REP (j,0,l*x-3)
		{
			tr1 = mul(0,j);
		//	cout<<"1 "<<tr1<<endl;
			if (tr1!=2)
				continue;
			REP(k,j+1,l*x-2)
			{
				tr2 = mul(j+1,k);
		//		cout<<"2 "<<tr2<<endl;
				if (tr2!=3)
					continue;
				tr3 = mul(k+1, l*x-1);
		//		cout<<"3 "<<tr3<<endl;
				if (tr1==2 && tr2==3 && tr3==4)
				{
					yes=1;
					break;
				}
			}
			if (yes)
				break;
		}
		
		*/
		/*
		REP(j,0,l*x-1)
		{
			oi = s2[j]-'0'; 
			//cout<<"oi"<<' '<<oi<<endl;
			//cout<<"tr"<<' '<<tr1<<endl;
			if (tr1<0)
				tr1 = -m[-tr1][oi];
			else
			{
				tr1 = m[tr1][oi];
			//	cout<<"get p\n";
			}
			//cout<<"h "<<m[tr1][oi]<<endl;	
			//cout<<"o "<<tr1<<endl;
			if (tr1==2)
			{
				tr2 = 1;
				REP(k, j+1, l*x-1)
				{
					oi = s2[k]-'0'; 
					if (tr2<0)
						tr2 = -m[-tr2][oi];
					else
						tr2 = m[tr2][oi];
					if (tr2==3)
					{
						tr3 = 1;
						REP(n, k+1, l*x-1)
						{
							oi = s2[n]-'0'; 
							if (tr3<0)
								tr3 = -m[-tr3][oi];
							else
								tr3 = m[tr3][oi];
						}
						if (tr3==4)
							yes = 1;
					}
					if (yes)
						break;
				}
			}
			if (yes)
				break;
		}
		*/
		if (yes)
			fout<<"Case #"<<i<<": "<<"YES"<<endl;
		else
			fout<<"Case #"<<i<<": "<<"NO"<<endl;
		
	}
	return 0;
}

