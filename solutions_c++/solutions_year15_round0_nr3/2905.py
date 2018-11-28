#include<bits/stdc++.h>
#define ll long long int
#define F first
#define S second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rep(i,in1,n) for(i=in1;i<=n;i++)
#define repd(i,in1,n) for(i=in1;i>=n;i--)

#define pf(n) printf("%d ",n);
#define sf(n) scanf("%d",&n)
#define sl(n) scanf("%I64d",&n)
#define nl printf("\n")
#define mem(arr,init) memset(arr,init,sizeof(arr))
#define vi vector<int>
#define vvi vector<vi>

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define ep emplace_back//c++11
#define ii pair<int,int>
using namespace std;


string str;

int arr[5][5];


int conv(char ch)
{
	if(ch=='1')
		return 1;
	if(ch=='i')
		return 2;
	if(ch=='j')
		return 3;
	if(ch=='k')
		return 4;
}
vi veci;//vector that stores pos for i
vi veck;//vector that stores pos for k
void build(int tree[],int node,int a,int b)
{
	if(a>b)
	return;
	if(a==b)
	{
		tree[node]=conv(str[a]);
		return;
	}
	build(tree,node*2,a,(a+b)/2);
		build(tree,node*2+1,(a+b)/2+1,b);
		int l1,l2,r1,r2;
		l1=tree[node*2]; r1=tree[node*2+1];
		if(l1>0)
		l2=1;
		else
		l2=-1;
		
		if(r1>0)
		r2=1;//sign
		else
		r2=-1;
		tree[node]=arr[abs(l1)][abs(r1)]*l2*r2;
		
		
	
}
int query(int tree[],int node,int a,int b,int x,int y)
{
	if(a>b || x>b || y<a)
	return -50;
	if(x<=a && y>=b)
	return tree[node];
	
	int q1=query(tree,node*2,a,(a+b)/2,x,y);
	int q2=query(tree,node*2+1,(a+b)/2+1,b,x,y);
	if(q1==-50)
	return q2;
	if(q2==-50)
	return q1;
	
	int l2,r2,temp;
	
		if(q1>0)
		l2=1;
		else
		l2=-1;
		
		if(q2>0)
		r2=1;//sign
		else
		r2=-1;
		temp=arr[abs(q1)][abs(q2)]*l2*r2;
		return temp;
	
}

int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,nc,l,pos,ptr1,ptr2,sign,len;
	int chk;
	int temp;
	freopen ("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	
	arr[1][1]=1;  arr[1][2]=2;  arr[1][3]=3;  arr[1][4]=4;
	arr[2][1]=2;  arr[2][2]=-1;  arr[2][3]=4;  arr[2][4]=-3;
	arr[3][1]=3;  arr[3][2]=-4;  arr[3][3]=-1;  arr[3][4]=2;
	arr[4][1]=4;  arr[4][2]=3;  arr[4][3]=-2;  arr[4][4]=-1;
	
	sf(nc);
		for(t=1;t<=nc;t++)
		{
			sf(l); sf(x);
			veci.clear();
			veck.clear();
			
			string s1;
			cin>>str;
			
			int tree[50005]={0};
			s1=str;
			for(i=1;i<x;i++)
			{
				str+=s1;
			}
			len=str.length();
			if(len<3)
			{
				printf("Case #%d: NO\n",t);
				continue;
			}
			build(tree,1,0,len-1);
			
			temp=conv(str[0]);
			
			if(temp==2)
			{
				veci.pb(0);
			}
			
			for(i=1;i<len;i++)
			{
				if(temp>0)
				{
					sign=1;
				}
				else
				sign=-1;
				ptr1=abs(temp);
				ptr2=conv(str[i]);
				temp=arr[ptr1][ptr2]*sign;
				if(temp==2)
				{
					veci.pb(i);
				}
				
			}
			temp=conv(str[len-1]);
			if(temp==4)
			{
				veck.pb(len-1);
				
			}
			for(i=len-2;i>=0;i--)
			{
				if(temp>0)
				{
					sign=1;
				}
				else
				sign=-1;
				ptr2=abs(temp);
				ptr1=conv(str[i]);
				temp=arr[ptr1][ptr2]*sign;
				if(temp==4)
				{
					veck.pb(i);
				}
				
			}
		/*	printf("hi\n");
			tr(veci,it)
			{
				cout<<*it<<" ";
			}
			printf("hello\n");
			tr(veck,it)
			{
				cout<<*it<<" ";
			}*/
			
			bool flag=0;
			for(i=0;i<veci.size();i++)
			{
				for(j=0;j<veck.size();j++)
				{
					ptr1=veci[i];
					ptr2=veck[j];
					if(ptr1>ptr2)
					continue;
					if(query(tree,1,0,len-1,ptr1+1,ptr2-1)==3)
					{
						printf("Case #%d: YES\n",t);
						flag=1;
						break;
					}
				}
				if(flag)
				break;
			}
			if(!flag)
			{
				printf("Case #%d: NO\n",t);
			}
			
			
			
			
		}





	return 0;
}

