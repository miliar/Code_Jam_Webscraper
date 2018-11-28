#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<utility>

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
#define iii pair<ii,i>
//	freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
using namespace std;
int mark[18];
int cnt=0;
string s1,tmp;
void add()
{
	int i,j,k,n;

	n=tmp.length();
	int carry=0,val,v1,v2;
	for(i=0;i<n;i++)
	{
		val=s1[i]-'0';
		v1=tmp[i]-'0';
		val=v1+val+carry;
		s1[i]=(val%10 +'0');
		carry=val/10;


	}
	
		while(carry>0 && i<s1.length())
		{
			val=s1[i]-'0';
			val=val + carry ;
			s1[i]=val%10 +'0';
			carry=val/10;
			i++;
		}
		if(carry>0 )
		{
			s1+=(carry+'0');
		}
	

}
int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,cs;
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>t;
	cs=1;
	while(t--)
	{
		cin>>s1;
		

		n=s1.length();
		reverse(s1.begin(),s1.end());
		tmp=s1;
	//	nl;
		if(s1[0]=='0' && n==1)
		{
			//cout<<"hello";
			printf("Case #%d: INSOMNIA",cs++);
			nl;
			continue;

		}

		//cout<<s1;

		mem(mark,0);
		cnt=0;

		for(i=0;i<s1.length();i++)
		{
			if(mark[s1[i]-'0']==0)
				cnt++;
			mark[s1[i]-'0']=1;

		}
		int ans=1;
		while(cnt<=9)
		{
			ans++;
			add();
			//cout<<"hi"<<s1;
	//		nl;
			for(i=0;i<s1.length();i++)
			{
				if(mark[s1[i]-'0']==0)
					cnt++;
				mark[s1[i]-'0']=1;

			}


		}
		reverse(s1.begin(),s1.end());
		printf("Case #%d: ",cs++);
		cout<<s1;;
		nl;



		

	}

	return 0;
}