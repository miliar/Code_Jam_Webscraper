#include<iostream>
#include<stdio.h>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<sstream>
using namespace std;
typedef long long int ll;
int xx[]={1,1,1,0,-1,-1,-1,0};
int yy[]={-1,0,1,1,1,0,-1,-1};
ll gcd(ll a,ll b)
{ return ((a%b==0)?b:gcd(b,a%b)) ;}
ll mod = 1000000000+7;
ll k,l,S,len,tot,bingo;
string s1,s2;
vector<char>v;
map<string,bool>m;
vector<ll>ans;
int chek(string s)
{
	ll i,count=0,sub;
	sub = s2.size();
	string tmp;
	for(i=0;i<=S-l;i++)
	{
		 tmp = "";
		 tmp = s.substr(i,l);
		 //cout<<tmp<<" "<<i<<endl;
		 if(tmp==s2)
		 count++;
	}
	//cout<<count<<endl;
	bingo = max(bingo,count);
	//cout<<count<<endl;
	return count;
	
}
void dfs(int len1,string s)
{
	 if(len1==S)
	 {
	 	 //if(m[s]==0)
	 	 //{
		    tot++;
		// cout<<s<<endl;
		   ans.push_back(chek(s));
		    m[s] = 1;
		 //}
		 return ;
	 }
	 
	 int i;
	 for(i=0;i<len;i++)
	 {    
	 	 dfs(len1+1,s+v[i]);
	 }
	 
	 return ;
}
int main()
{  
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
   ll tcase,t,i,tar;
   
   cin>>tcase;
   for(t=1;t<=tcase;t++)
   {
   	  cin>>k>>l>>S;
   	  cin>>s1>>s2;
   	  len = s1.size();
   	  for(i=0;i<len;i++)
   	  v.push_back(s1[i]);
   	  string str;
   	  tot = 0;
   	  bingo = 0;
   	  for(i=0;i<len;i++)
   	  {
	        str ="";
	        str+=v[i];
			dfs(1,str);
	  }
	  
	  double ans1;
	 
	  tar = 0;
	  len = ans.size();
	  if(bingo==0)
	  len = 0;
	  for(i=0;i<len;i++)
	   tar += (bingo-ans[i]);
	  //  cout<<tar<<" "<<tot<<endl;
	  ans1 = (double)tar/(double)tot;
	  printf("Case #%lld: %.8lf\n",t,ans1);
   	  v.clear();
   	  m.clear();
   	  ans.clear();
   }
  
 return 0;
}

