/*
    Author:-Sarthak Taneja
    CSE 2nd year,MNNIT Allahabad
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair< int,int > ii;
typedef vector< ii > vii;

#define sfd(x) scanf("%d",&x)
#define sfs(x) scanf("%s",x)
#define sff(x) scanf("%lf",&x)
#define mod 1000000007
#define MAX 1000000
#define pb push_back
#define mp make_pair
#define fr first 
#define sc second
#define testcases scanf("%d",&t);while(t--)
#define ffor(a,b,c) for(a=b;a<c;a++)
#define rfor(a,b,c) for(a=b;a>=c;a--)

int divs[10]= {3,5,7,11,13,17,19,23,29,31};

vector< pair< string, vector<int> > > ans;

void generate(vector<int> no, int md[10][9],int index)
{
	int i,j;
	if(index == 32)
	{
		string str="";
		bool flag;
		vector<int> fact(9);
		for(j=0;j<9;j++)
		{
			flag=0;
			for(i=0;i<10;i++)
			{
				if(md[i][j] == 0)
				{
					flag=1;
					fact[j]=divs[i];
					break;
				}
			}
			if(flag == 0)
				break;
		}
		if(flag)
		{
			for(i=0;i<no.size();i++)
			{
				char ch= '0'+no[i];
				str+=ch;
			}
			ans.pb(mp(str, fact));
		}

		if(ans.size() == 500)
		{
			for(i=0;i<500;i++)
			{
				cout<<ans[i].fr<<" ";
				for(j=0;j<9;j++)
					cout<<ans[i].sc.at(j)<<" ";
				cout<<endl;
			}
			exit(0);
		}
		return;
	}

	int md2[10][9];
	for(i=0;i<10;i++)
	{
		for(j=0;j<9;j++)
		{
			md2[i][j]=md[i][j];
		}
	}

	no.pb(1);
	for(i=0;i<10;i++)
	{
		for(j=0;j<9;j++)
			md[i][j] = (md[i][j]*(j+2) + 1)%divs[i];
	}
	generate(no, md, index+1);
	no.pop_back();

	if(index != 0 && index != 31)
	{
		for(i=0;i<10;i++)
		{
			for(j=0;j<9;j++)
			{
				md[i][j]=md2[i][j];
			}
		}

		no.pb(0);
		for(i=0;i<10;i++)
		{
			for(j=0;j<9;j++)
				md[i][j] = (md[i][j]*(j+2) + 0)%divs[i];
		}
		generate(no, md, index+1);
	}
}

int main()
{
	int i,j,t;
	printf("Case #1:\n");

	vector<int> no;
	int md[10][9];

	for(i=0;i<10;i++)
	{
		for(j=0;j<9;j++)
		md[i][j]=0;
	}
	generate(no,md,0);
	return 0;
}