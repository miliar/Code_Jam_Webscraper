#include<iostream>
#include<cstdio>

using namespace std;

void input(int (&a)[4])
{
	int x,y;
	cin>>x;
	int cnt=(x-1)*4;
	while (cnt--) cin>>y;
	for (int i=0;i<4;++i) cin>>a[i];
	cnt=(4-x)*4;
	while (cnt--) cin>>y;
}

void f(int a[4],int b[4])
{
	int ans=-1;
	for (int i=0;i<4;++i)
	  for (int j=0;j<4;++j)
	  	if (a[i]==b[j])
		  if (ans==-1) ans=a[i];else {printf("Bad magician!\n");return;}
	if (ans==-1) printf("Volunteer cheated!\n");
	else cout<<ans<<endl;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;++t)
	{
		printf("Case #%d: ",t);
		int a[4],b[4];
		input(a);
		input(b);
		f(a,b);
	}
}
