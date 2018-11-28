#include <bits\stdc++.h>

using namespace std;

int n;

void test(int nom)
{     int n,m[10001],s1=0,s2=0,d=0; 
      cin>>n; for(int i=0;i<n;++i) cin>>m[i];
	  for(int i=1;i<n;++i) {d=max(m[i-1]-m[i],d);if (m[i]<m[i-1]) s1+=m[i-1]-m[i];}
      for(int i=1;i<n;++i) s2+=min(m[i-1],d);  
	  cout<<"Case #"<<nom<<": "<<s1<<" "<<s2<<'\n';
}

int main ( )
{
 freopen("in.txt","r",stdin);
 freopen("out.txt","w",stdout);
 cin>>n; 
 for(int i=1;i<=n;++i) test(i);
}
