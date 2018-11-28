
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mod 1000000007
int m;
void recur(int ar[17][17],int r,int c,int index,int ans,int left)
{
	
	if( left==0)
	{
		//cout<<"HII";
		m=m<ans?m:ans;
		return ;
	}
	if(index>=r*c)
		return ;
	int col=index%r;
	int row=(index-col)/r;
	int temp=0;
	if(row-1>=0)
	{
		if(ar[row-1][col]==1)
			temp=1;
	}
	if(col-1>=0)
	{
		if(ar[row][col-1]==1)
			temp++;
	}

	recur(ar,r,c,index+1,ans,left);
	ar[row][col]=1;
	recur(ar,r,c,index+1,ans+temp,left-1);
	ar[row][col]=0;


}
int main()
{
	int t,r,c,n;
	scanf("%d",&t);
	int x=0;
	ll ans=0;
	m=10000;
	while(t--)
	{
		m=1000;
		scanf("%d%d%d",&r,&c,&n);
		ans=0;
		cout<<"Case #"<<++x<<": ";
		if(n<=(r*c+1)/2)
		{
			cout<<"0"<<endl;
			continue;
		}
		int ar[17][17];
		recur(ar,r,c,0,0,n);
		cout<<m<<endl;

	}
	return 0;
}