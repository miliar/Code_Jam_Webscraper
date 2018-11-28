#include<bits/stdc++.h>
#define nl '\n'
using namespace std;
struct node
{
	char c;
	int num;
};
bool comp(node a,node b)
{
	if(a.num > b.num)
		return true;
	else return false;
}
int main()
{
	ios::sync_with_stdio(0);cin.tie(0);
	int t,i,n,j,cnt=0;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		node A[30];cnt=0;
		cin>>n;
		for(j=0;j<n;j++)
		{
			A[j].c=(char)(j+65);
			cin>>A[j].num;
			cnt+=A[j].num;
		}
		sort(A,A+n,comp);int k=0;
		cout<<"Case #"<<i<<": ";
		while(cnt!=0)
		{

			if((A[k].num > A[k+1].num))
			{
				while(A[k].num != A[k+1].num){
					cout<<A[k].c<<" ";
					A[k].num --;
					cnt--;
				}
			}
			if(n>2 && A[k].num == 1 && A[k+1].num == 1 && A[k+2].num == 1)
			{
				cout<<A[k+2].c<<" ";
				cout<<A[k].c<<A[k+1].c<<" ";
				cnt -= 3;
			}
			else if((A[k].num == A[k+1].num) && A[k].num!=0)
			{
				cout<<A[k].c<<A[k+1].c<<" ";
				A[k].num--;A[k+1].num--;
				cnt-=2;
			}
			sort(A,A+n,comp);
		}
		cout<<nl;
	}
	return 0;
}
