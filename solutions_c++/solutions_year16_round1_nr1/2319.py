#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000001
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,size(x))
#define INF 1e18
#define ll long long
#define endl "\n"

set<string> all;
set<string>::iterator it;
void fun(string s1,string s,int index,int len)
{   if(index==len)
    {
    	all.insert(s1);
    	return;
    }
	string s2="";
	string s3="";
	string s4="";
	s3=s1;
    s4=s4+s[index];
	s2=s2+s[index];
	s1=s1+s2;
	fun(s1,s,index+1,len);
	s4=s4+s3;
	fun(s4,s,index+1,len);
}
int main() {
    //hg;
    int t,k;
    string ss,first;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {   all.clear();
    	cin>>ss;
    	first="";
    	first=first+ss[0];
    	int l=ss.length();
    	fun(first,ss,1,l);
    	    it=all.end();
    	    it--;
    	printf("Case #%d: ",k);
    	cout<<*it<<"\n";
    }
	return 0;
}