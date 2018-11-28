#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;


int main()
{
	//ios::sync_with_stdio(false);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,l,x;
	string s;
	string st;
	cin>>t;
	//cout<<t<<endl;
	for(int k=1;k<=t;k++)
	{
		cin>>l>>x;
		//cout<<l<<" "<<x<<endl;
		cin>>s;
		//cout<<s<<endl;
		st.clear();
		for(int i=0;i<x;i++)
		{
			st.append(s);
			//cout<<st<<endl;
		}

		int mat[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
		int l=st.size();
		if(l<3)
		{
			printf("case #%d: NO\n",k);
			//printf("\n\n");
			continue;
		}

		//cout<<st;
		for(int i=0;i<l;i++)
			st[i]-='g';

		
		//cout<<"\n searching i";
		//fflush(stdout);
		int p=st[0];
		int i,j;
		for(i=1;i<l && p!=2;i++)
			if(p<0)
			p=-1 * mat[-p-1][st[i]-1];
		else p=mat[p-1][st[i]-1];

		//cout<<"\n i found at "<<i-1;

		if(i>l-1)
		{	
			printf("case #%d: NO\n",k);
			//printf("\n\n");
			continue;
		}

		//cout<<"\n searching k\n";
		//fflush(stdout);
		p=st[l-1];
		//cout<<p<<" ";
		for(j=l-2;j>=0 && p!=4;j--)
		{
			if(p<0)
			p=-1 * mat[st[j]-1][-p-1];
			else p=mat[st[j]-1][p-1];
			//cout<<p<<" ";
		}

		//cout<<"\n k found at "<<j+1;

		if(j<0)
		{
			printf("case #%d: NO\n",k);
			//printf("\n\n");
			continue;
		}

		//cout<<i<<" "<<j;
		

		p=st[i++];
		//cout<<p<<" ";
		
		for(;i<l && i<=j;i++)
		{
			if(p<0)
			p=-1 * mat[-p-1][st[i]-1];
			else p=mat[p-1][st[i]-1];
			//cout<<p<<" ";
		}

		if(p==3)
			printf("case #%d: YES\n",k);

		else printf("case #%d: NO\n",k);

		//printf("\n\n");

	}
			
	return 0;

}