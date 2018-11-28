#include<iostream>
using namespace std;
struct numin
{
	int grid1[4][4],grid2[4][4],r1,r2;
};
int i,j,k;
void check(struct numin *,int);
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t;
	struct numin a[100];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>a[i].r1;
		for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		cin>>a[i].grid1[j][k];
		cin>>a[i].r2;
		for(j=0;j<4;j++)
		for(k=0;k<4;k++)
		cin>>a[i].grid2[j][k];
	}
	check(a,t);
	return 0;
}
void check(struct numin *a,int t)
{
	int p,n;
	for(i=0;i<t;i++)
	{
		p=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[i].grid1[a[i].r1-1][j]==a[i].grid2[a[i].r2-1][k])
				{
					p++;
					n=a[i].grid1[a[i].r1-1][j];
				}
			}
		}
		if(p==0)
		cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else if(p>1)
		cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else
		cout<<"Case #"<<i+1<<": "<<n<<endl;
	}
}
