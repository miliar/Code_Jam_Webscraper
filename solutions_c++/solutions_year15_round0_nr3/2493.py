//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define PB push_back
#define SZ size
#define MP make_pair

int mat[5][5];
int dp[1000006], dp1[1000006], dp2[1000006], arr[1000006];
vector<int> magic[1000006];
set<int> ans;

int main()
{
	freopen("input3.txt","r",stdin);
    freopen("output3.txt","w",stdout);
    mat[1][1]=1; mat[1][2]=2; mat[1][3]=3; mat[1][4]=4;
    mat[2][1]=2; mat[2][2]=-1; mat[2][3]=4; mat[2][4]=-3;
    mat[3][1]=3; mat[3][2]=-4; mat[3][3]=-1; mat[3][4]=2;
    mat[4][1]=4; mat[4][2]=3; mat[4][3]=-2; mat[4][4]=-1;
	int i, j, k;
	int cases;
	int n;
	k=1;
	cin>>cases;
	wl(cases)
	{
		int l, x;
		cin>>l>>x;
		string str1;
		cin>>str1;
		string mmaks = str1;

		fl(i,0,10000)
			magic[i].clear();
		ans.clear();

		fl(i,1,x)
		{
			str1+=mmaks;
		}
		//cout<<str1; nline;

		l = l*x;

		fl(i,0,l)
		{
			if(str1[i]=='i')
				arr[i]=2;
			else if(str1[i]=='j')
				arr[i]=3;
			else
				arr[i]=4;
			//cout<<arr[i]<<" ";
		}
		//nline;
		int neg = 0;

		dp[0]=arr[0];

		i=0;
		if(arr[i+1]==3 && arr[i]==2)
		{
			magic[i].PB(i+1);
			ans.insert(i+1);
		}

		dp1[i+1]=arr[i+1];
		if(arr[i]==2)
		{
			fl(j,i+2,l)
			{
				neg=0;
				if(arr[j]<0)
					neg++;
				if(dp1[j-1]<0)
					neg++;
				//cout<<i<<" : "<<neg; nline;
				int temp = mat[abs(dp1[j-1])][abs(arr[j])];
				if(neg==1)
				{
					temp=-1*temp;
				}
				dp1[j]=temp;
				if(dp1[j]==3)
				{
					magic[i].PB(j);
					ans.insert(j);
				}
				//cout<<"*"<<temp<<" ";
			}
		}

		fl(i,1,l)
		{
			neg=0;
			if(arr[i]<0)
				neg++;
			if(dp[i-1]<0)
				neg++;
			//cout<<i<<" : "<<neg; nline;
			int temp = mat[abs(dp[i-1])][abs(arr[i])];
			if(neg==1)
			{
				temp=-1*temp;
			}
			dp[i]=temp;

			if(dp[i]==2)
			{
				//cout<<i<<" : ";
				if(arr[i+1]==3)
					magic[i].PB(i+1);
				dp1[i+1]=arr[i+1];
				fl(j,i+2,l)
				{
					neg=0;
					if(arr[j]<0)
						neg++;
					if(dp1[j-1]<0)
						neg++;
					//cout<<i<<" : "<<neg; nline;
					int temp = mat[abs(dp1[j-1])][abs(arr[j])];
					if(neg==1)
					{
						temp=-1*temp;
					}
					dp1[j]=temp;
					if(dp1[j]==3)
					{
						magic[i].PB(j);
						ans.insert(j);
					}
					//cout<<j<<" : "<<temp;nline;
					
				}
			}
			//nline;
		}

		/*fl(i,0,l)
			cout<<dp[i]<<" ";
		nline;*/

		dp2[l-1]=arr[l-1];
		int limit = ans.SZ();
		int f = 0;
		//cout<<limit; nline;
		cout<<"Case #"<<k++<<": ";
		//nline;

		set<int>::const_iterator itr = ans.begin();


		for( ; itr!=ans.end(); itr++)
		{
			//cout<<ans[i]<<" ";
			int ele = *itr;
			//cout<<ele<<" ";
			dp2[ele+1]=arr[ele+1];
			fl(j,ele+2,l)
			{
				neg=0;
				if(arr[j]<0)
					neg++;
				if(dp2[j-1]<0)
					neg++;
				//cout<<i<<" : "<<neg; nline;
				int temp = mat[abs(dp2[j-1])][abs(arr[j])];
				if(neg==1)
				{
					temp=-1*temp;
				}
				dp2[j]=temp;
			}
			if(dp2[l-1]==4)
			{
				f=1;
				break;
			}
		}
		//nline;
		if(f==1)
			cout<<"YES";
		else
			cout<<"NO";

		/*
		rev(i,l-2,0)
		{
			neg=0;
			if(arr[i]<0)
				neg++;
			if(dp2[i+1]<0)
				neg++;
			//cout<<i<<" : "<<neg; nline;
			int temp = mat[abs(dp2[i+1])][abs(arr[i])];
			if(neg==1)
			{
				temp=-1*temp;
			}
			dp2[i]=temp;
		}

		fl(i,0,l)
			cout<<dp2[i]<<" ";
		nline;

		fl(i,0,1000)
		{
			if(magic[i].SZ()>0)
			{
				cout<<i<<" : ";
				fl(j,0,magic[i].SZ())
					cout<<magic[i][j]<<" ";
				nline;
			}
		}
		nline;*/

		
		//cout<<ans;
		nline;
	}

	return 0;
}