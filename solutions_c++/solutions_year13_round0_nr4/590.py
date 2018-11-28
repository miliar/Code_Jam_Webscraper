/* Author : migdal */
#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define INF 1000000000
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
string MAX="99 99 99 99 99 99 99 99 99 99 99 99 99 99 99 99 99 99 99 99",all;
int type[21];
int n,k;
vector< vector<int> >in;
map<string,string>dp;
map<string,string>::iterator it;
string add(int num)
{
   stringstream ss;
   ss<<num;
   if(num<10)return "0"+ss.str();
   else return ss.str();
}
string sol(string bit,int hav[21])
{
   if(bit==all)return "";
   it=dp.find(bit);
   if(it!=dp.end())
   {
      return dp[bit];
   }
   int i,j,k;
   string ans=MAX,temp,ret,fr;
   for(i=0;i<bit.length();i++)
   {
      if(bit[i]=='0')
      {
          int fl=0;
	  if(hav[type[i+1]]>0)fl=1;
	  if(fl)
	  {
	     int tmp[21];
             for(k=1;k<=20;k++)tmp[k]=hav[k];
	     for(k=0;k<in[i].size();k++)tmp[in[i][k]]++;
	     tmp[type[i+1]]--;
	     temp=bit;
	     temp[i]='1';
	     ret=sol(temp,tmp);
	     fr=add(i+1);
	     if(ret!=MAX)
	     {
		if(ans>fr+" "+ret)ans=fr+" "+ret;
	     }
	  }
      }
   }
   dp[bit]=ans;
   return ans;

}
int fn(string tmp)
{
   int num;
   istringstream(tmp)>>num;
   return num;
}
int main()
{
   int test,i,j,num,coun;
   string ans,tmp;
   cin>>test;coun=0;
   while(test--)
   {
      coun++;
      in.clear();dp.clear();
      int key[21];for(i=1;i<=20;i++)key[i]=0;
      cin>>k>>n;
      for(i=1;i<=k;i++){cin>>num;key[num]++;}
      for(i=1;i<=n;i++)
      {
	 vector<int>temp;
	 cin>>type[i];
	 cin>>k;
	 for(j=1;j<=k;j++){cin>>num;temp.PB(num);}
	 in.PB(temp);
      }
      all="";
      for(i=1;i<=n;i++)all=all+"1";
      tmp="";
      for(i=1;i<=n;i++)tmp=tmp+"0";
      ans=sol(tmp,key);
      if(ans==MAX)cout<<"Case #"<<coun<<": "<<"IMPOSSIBLE"<<endl;
      else
      {
	 cout<<"Case #"<<coun<<": ";
	 int fl=0;int num=0;
	 for(i=0;i<ans.length();i++)
	 {
	    if(ans[i]!=' ')
	    {
	       num=num*10;
	       num=num+ans[i]-48;
	       fl=1;
	    }
	    else if(ans[i]==' '&&fl)
	    {
	       cout<<num<<" ";
	       num=0;
	       fl=0;
	    }
	 }
	 if(fl)cout<<num;
	 cout<<endl;
      }
   }
   return 0;
}
