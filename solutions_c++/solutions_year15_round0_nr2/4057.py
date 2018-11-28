#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("B-small-attempt0.in.txt");
ofstream cout("out.txt");

int a[60],n,ans;

void cal(int x)
{
	if (ans>0 && x>=ans) 
		return;
	int i,k=0;
	for (i=1;i<=n;i++)
		if (a[i]>a[k]) 
			k=i;
	if (ans==-1||x+a[k]<ans)
		ans=x+a[k];
	if (ans==1) 
		return;
	n++;
	for (i=1;i<=a[k]/2;i++)
	{
		a[k]-=i;
		a[n]=i;
		cal(x+1);
		a[k]+=i;
	}
	n--;
	return;
}

int main()
{
	int t,i,caseNum=0;

	cin>>t;
	while (t--)
	{
		caseNum++;
		a[0]=0;
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>a[i];
		ans=-1;
		cal(0);
		cout<<"Case #"<<caseNum<<": "<<ans<<endl;
	}
	return 0;
}