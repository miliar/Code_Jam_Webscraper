/*Author: Rishul Aggarwal*/

#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define in(type,x) scanf("%" #type,&x)
#define debug(args...) {dbg,args; cerr<<endl;}
#define test int t;\
			 in(d,t);\
			 while(t--)

using namespace std;

struct debugger
{template<typename T> debugger& operator,(const T& v)
 {cerr<< v <<" ";
  return *this;
 }
}dbg;

ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m) {ll ans=1; b%=m; while(exp){if(exp&1) ans=(ans*b)%m; exp>>=1; b=(b*b)%m; } return ans; }


int graph[30][30];

int cnt[30],visited[30];

ll fact[103];

int main()
{

fact[0]=1LL;
rep(i,1,100)
 fact[i] = (fact[i-1] *i)%mod;
    
FILE *f1,*f2;
f1=fopen("input.txt","r");
int cas=1;
f2=fopen("output.txt","w");	

int t;
fscanf(f1,"%d",&t);

while(t--)
{
	int n;
	fscanf(f1,"%d",&n);
	vector<string> a;
	
	for(int k=0;k<n;k++)
	{
		char s[105];
	    fscanf(f1,"%s",s);
	    int l=strlen(s);
	    int i,j;
	    string temp;
		int hash[26]={0};
		for(i=0;i<l;i++)
		 {
		  temp+=s[i];	
		  //char cur=s[i];
		  for(j=i+1;j<l;j++)
		   if(s[i]!=s[j])
		    break;
		  i=j-1;
	     }
	    //cout<<temp<<endl;
		a.push_back(temp); 
	
	}
	//cout<<"here";
	
	ll ans=0;
	sort(a.begin(),a.end());
	int cnt=0;
	do
	{
		bool flag=1;
		int hash[26]={0};
		int i,j;
		string temp;
		for(int i=0;i<a.size();i++)
		{
			for(int j=0;j<a[i].length();j++)
			{
				temp+=a[i][j];
			}
		}
		int l=temp.length();
		for(i=0;i<l;i++)
		{
			if(hash[temp[i]-97])
			 {
			 	flag=0;
			 	break;
			 }
			hash[temp[i]-97]=1;
			int j=i+1;
			while(temp[j]==temp[i] && j<l)
			 j++;
			i=j-1;
		}
		if(flag)
		 ans = (ans + 1)%mod;
		cnt++; 
	}while(next_permutation(a.begin(),a.end()));
   
   map<string,int>x;
   for(int i=0;i<a.size();i++)
    x[a[i]]++;
   map<string,int>::iterator it;
   for(it=x.begin();it!=x.end();it++)
    ans = (ans*(fact[it->second]))%mod; 
   
   cout<<cnt<<endl;
   fprintf(f2,"Case #%d: %lld\n",cas,ans);
   cas++;	
			
			
		
	
}
return 0;
}



