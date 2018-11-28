#include<bits/stdc++.h>
#define intMAX 1123456789LL
#define MAX intMAX * intMAX
#define F first
#define S second
#define mp make_pair
#define ll long long
#define pb push_back
#define pv(v,b,a) v.insert(v.begin()+b,a)
#define all(c) c.begin(),c.end()
#define sf(a) scanf("%d",&a);
#define sl(a) scanf("%lld",&a);
#define MAXCR 1000000000
#define mem(arr,a) memset(arr, a, sizeof arr)
#define er(vec,a,b) vec.erase(vec.begin() + a, vec.begin() + b+1)
#define traverse(a) for()
#define pii pair<int ,int>
#define mod 1000000007
#define LIM 100
using namespace std;
/*
list as pop_front();push_front(ELEMENT);
list as pop_front();push_back(ELEMENT);
to see first element stack=q.front()
to see last element queue=q.back()
*/
//str.insert(6,str3,3,4); to insert 4 words from str3 starting from 3rd position(0 based indexing) to str from 6th position (0 based indexing)
//str.find("live");//finds first occurance of string and returns its 0 based indes
//string str1=str.substr (a,n);//a=0 based start index,n=length of words//if length not given substring till end is formed
//auto bound_=upper_bound (v.begin(), v.end(), 20); //Returns an iterator pointing to the first element in the range [first,last) which compares greater than val.
//auto bound_=lower_bound (v.begin(), v.end(), 20);//Returns an iterator pointing to the first element in the range [first,last) which does not compare less than val.
//for(???<???>:iterator itr;itr!=???.end();itr++) or for(auto &tt : t.edges)
//getline(cin,s,'\n');  to get input terminating at'\n';excluding '\n'
//(a/b)%m = ((a%m)(b^(m-2)%m))%m.
//(a^b)%m=
int check[5][5]={{0}};
string s;
vector<int>leftv;
vector<int>rightv;
int get_(char a)
{
	if(a=='1')
		return 1;
	if(a=='i')
		return 2;
	if(a=='j')
		return 3;
	if(a=='k')
		return 4;
} 
void set_()
{
	check[1][1]=1;
	check[1][2]=2;
	check[1][3]=3;
	check[1][4]=4;
	check[2][1]=2;
	check[2][2]=-1;
	check[2][3]=4;
	check[2][4]=-3;
	check[3][1]=3;
	check[3][2]=-4;
	check[3][3]=-1;
	check[3][4]=2;
	check[4][1]=4;
	check[4][2]=3;
	check[4][3]=-2;
	check[4][4]=-1;
}
void initialize(int seg[],int node,int a,int b)
{
	if(a==b)
	{
		seg[node]=get_(s[a]);
		return ;
	}
	initialize(seg,node*2+1,a,(a+b)/2);
	initialize(seg,node*2+2,(a+b)/2+1,b);
	int p1=seg[node*2+1];
	int p2=seg[node*2+2];
	int p11,p22;
	if(p1>0)
		p11=1;
	else
		p11=-1;
	if(p2>0)
		p22=1;
	else
		p22=-1;
	seg[node]=check[abs(p1)][abs(p2)]*p11*p22;
}
int query(int seg[],int node,int a,int b,int i,int j)
{
	
	if(i>j)
		return -10;
	
	if(j<a||i>b)
		return -10;
		
	if(a>=i&&b<=j)
		return seg[node];
	int p1=query(seg,node*2+1,a,(a+b)/2,i,j);
	int p2=query(seg,node*2+2,(a+b)/2+1,b,i,j);
	
	if(p1==-10)
		return p2;
	if(p2==-10)
		return p1;
	int p11,p22;
	if(p1>0)
		p11=1;
	else
		p11=-1;
	if(p2>0)
		p22=1;
	else
		p22=-1;
	int ans=check[abs(p1)][abs(p2)]*p11*p22;
	
	return ans;
}
int main()
{
	freopen ("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	
	int flag,z,temp,j,t,len,l,x,i,temp1;
	string s1;
	set_();
	sf(t)
	for(z=1;z<=t;z++)
	{
		int seg[50025]={0};
		rightv.clear();
		leftv.clear();
		sf(l)
		sf(x)
		cin>>s;
		s1=s;
		for(i=1;i<x;i++)
		{
			s=s+s1;
		}
		len=s.length();		
		if(l*x<3)
		{
			printf("Case #%d: NO\n",z);
			continue;
		}
		initialize(seg,0,0,len-1);
		temp=get_(s[0]);
		if(temp==2)
		{
			leftv.pb(0);
		}
		for(i=1;i<len;i++)
		{
			if(temp>0)
				temp1=1;
			else
				temp1=-1;
			temp=check[abs(temp)][get_(s[i])];
			temp=temp*temp1;
			if(temp==2)
			{
				leftv.pb(i);
			}
		}
		temp=get_(s[len-1]);
		if(temp==4)
		{
			rightv.pb(len-1);
		}
		for(i=len-2;i>=0;i--)
		{
			if(temp>0)
				temp1=1;
			else
				temp1=-1;
			temp=check[get_(s[i])][abs(temp)];
			temp=temp*temp1;
			if(temp==4)
			{
				rightv.pb(i);
			}
		}
		flag=0;
		for(i=0;i<leftv.size();i++)
		{
			for(j=0;j<rightv.size()&&rightv[j]>leftv[i];j++)
			{
				if(query(seg,0,0,len-1,leftv[i]+1,rightv[j]-1)==3)
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
			{
				break;
			}
		}	
		if(flag==1)
		{
			printf("Case #%d: YES\n",z);
		}
		else
		{
			printf("Case #%d: NO\n",z);
		}
	}
	return 0;
}
