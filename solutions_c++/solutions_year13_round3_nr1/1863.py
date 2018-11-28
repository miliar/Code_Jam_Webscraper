#include<iostream>
#include<cstdio>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<utility>
#include<set>
#include<fstream>
#include<map>
#include<cstring>
#include<cmath>
#include <string>
#include <vector>
#define inf 2e9
#define mp(a,b) make_pair(a,b)
#define all(a) a.begin(),a.end()
#define pb(a) push_back(a)
#define show_vector(a) for(int i=0;i<a.size();i++) cout << a[i]<<" ";
#define show_array(a,n) for(int i=0;i<=n;i++) cout << a[i]<<" ";
#define take_array(a,n) for(int i=1;i<=n;i++) cin >> a[i];
typedef long long ll; 

using namespace std;

bool cons(char s)
{
  if(s=='a'||s=='e'||s=='i'||s=='o'||s=='u') return false;
  else return true;
}

int main()
{
  ifstream fin("input.txt"); ofstream fout("output.txt");  
  int t,ans,l,n,a,b;
  vector<pair<int,int> >v;
  pair<int,int>p;
  char s[100006];
  fin >> t;
  for(int c=1;c<=t;c++)
  {
    ans=0;
    v.clear();
   // v.pb(mp(0,0));
    fin >> s >> n;
    l=strlen(s);
    for(int i=0;i<l;i++)
    {
      if(cons(s[i]))
      {
	int j=i,count=0;
	while(j<l&&count<n&&cons(s[j]))
	{
	  j++;
	  count++;
	}
	
	if(count==n) {
	  v.pb(mp(i,j-1));
	  }
      }
    }
    for(int i=0;i<v.size();i++)
    {
     p=v[i];
     if(i!=0)
     {
       a=p.first-(v[i-1].first+1) +1;
      b= l-p.second;
    }
    else
    {
       a = p.first+1;
       b= l-p.second;
    }
        ans+= a*b;
    }
    fout << "Case #"<<c<<": "<<ans<<endl;
  }
  
}
 
 
//fout << "Case #"<<c<<": "<<ans<<endl;