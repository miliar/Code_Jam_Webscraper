#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1e9+7
bool cmp(pair<int,char> a,pair<int,char> b)
{
	if(a.first > b.first) return 1;
    return 0;
}
int main()
{
   // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
 
  for(int test=1;test<=t;test++)
  {
  	   int n,x;
  	   cin>>n;
  	   ll c=0;
  	   vector<pair<int,char> > v;
  	   for(int i=0;i<n;i++)
  	   {
  	   	      cin>>x;
  	   	      c+=x;
              v.push_back({x,'A'+i});
  	   }
  	      cout<<"Case #"<<test<<": ";
  	   if(n==2 )
  	   {
  	   	 for(int i=0;i<(c/2);i++)
  	   	 {
  	   	 	 cout<<"AB ";
  	   	 }
  	   	 cout<<endl;
  	  
  	   }
    else
    {
    
  	     for(int i=0;i<c-n;i++)
		 {
		 	 sort(v.begin(),v.end(),cmp);
 		 	 cout<<v[0].second<<" ";
		 	 v[0].first--;
		 } 
         
  	     if(n&1)
  	     {
  	     	cout<<(char)('A'+n-1)<<" ";
  	     	n--;
  	     }
  	     	for(int i=0;i<n;i+=2)
  	     	{
  	     		cout<<(char)('A'+i)<<(char)('A'+i+1)<<" ";
  	     	}
       cout<<endl;
  }
}
  return 0;
}
