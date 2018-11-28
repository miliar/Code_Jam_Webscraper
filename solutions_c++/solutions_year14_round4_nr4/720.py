#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("D-small-attempt0.in");
ofstream cout("out.txt");

typedef struct 
{
	string ss[10];
	int num;
} server;
server ser[5];
string s[10];
int n,m;
int ans,sum;

bool check_available()
{
	int i;
	for (i=1;i<=n;i++)
		if (ser[i].num==0)
			return false;
	return true;
}

int common(string a, string b)
{
	int i,k;
	k=a.length();
	if (b.length()<k)
		k=b.length();
	for (i=0;i<k;i++)
		if (a[i]!=b[i])
			break;
	return i;
}

int calc(int x)
{
	int i,j,k,l,rtn;
	rtn=ser[x].ss[1].length()+1;
	for (i=2;i<=ser[x].num;i++)
	{
		rtn+=ser[x].ss[i].length();
		k=0;
		for (j=1;j<i;j++)
		{
			l=common(ser[x].ss[i],ser[x].ss[j]);
			if (l>k) k=l;
		}
		rtn-=k;
	}
	return rtn;
}

void work(int x)
{
	int i;
	if (x>m)
	{
		if (!check_available())
			return;
		int i,res=0;
		for (i=1;i<=n;i++)
			res+=calc(i);
		if (res>ans)
		{
			ans=res;
			sum=1;
		}
		else if (res==ans)
		{
			sum++;
		}
		return;
	}

	for (i=1;i<=n;i++)
	{
		ser[i].num++;
		ser[i].ss[ser[i].num]=s[x];
		work(x+1);
		ser[i].num--;
	}
}

int main()
{
	int t,i,j,k,l,con=0;
	cin>>t;
	while (t--)
	{
		ans=0;
		sum=0;
		con++;
		cin>>m>>n;
		for (i=1;i<=n;i++)
			ser[i].num=0;
		for (i=1;i<=m;i++)
			cin>>s[i];
		work(1);
		cout<<"Case #"<<con<<": "<<ans<<" "<<sum<<endl;
	}
	return 0;
}