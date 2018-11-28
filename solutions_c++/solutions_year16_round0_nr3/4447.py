#include<bits/stdc++.h>
using namespace std;
int n;
#define ll long long int 
#define pb push_back
vector<ll> v;
vector<ll> factors[500];
void solve(ll num,int pos)
{
	     if(pos==n)
	     {
	     	  v.push_back(num);
	     	  return ;
		 }
		 if(pos==n-1)
		 solve(num|1<<pos,pos+1);
		 else solve(num,pos+1),solve(num|1<<pos,pos+1);
}
ll find(ll num,ll base)
{
	     
	     ll x=1;
	     ll sum=0;
	     for(ll i=0;i<n;i++)
	     {
	     	   if(num>>i &1)
	     	   {
	     	   	      sum+=x;
			   }
			   x*=base;
		 }
		 return sum;
}
bool isprime[1000010];
void pre()
{
	  isprime[2]=0;
	  for(int i=2;i<=1000000;i++)
	  {
	  	  if(!isprime[i])
	  	  {
	  	  for(int j=2*i;j<=1000000;j+=i)
	  	  {
	  	  	    isprime[j]=1;
		  }
	      }
	  }
}
long long int  fact(ll num)
{
	    ll rng=sqrt(num);
	    for(ll i=2;i<=rng;i++)
	    {
	    	  if(num%i==0)
	    	  return i;
		}
		return -1;
}
int main()
{
	   int t;
	   pre();
	   freopen("out.txt","w",stdout);
	   cin>>t;
	   while(t--)
	   {
	   	    int J;
	   	    cin>>n>>J;
	   	    ll num=1;
	   	    solve(num,1);
	   vector<ll> ans;
	   int l=v.size();
	   //cout<<"len "<<l<<endl;
	  int cnt=0;
	   for(int i=0;i<l;i++)
	   {
	  // 	cout<<"vvecto "<<v[i]<<endl;
	   	        if(cnt==J)
	   	        break;
	   	        bool f=0;
	   	        vector<ll> temp;
	   	       for(ll j=2;j<=10;j++)
	   	       {
	   	       	
	   	                 ll num=find(v[i],j);	
	   	                 //cout<<"at base "<<j<<" "<<num<<endl;
	   	                 
	   	                	   ll  ff=fact(num);
						 	  if(ff==-1)
						 	  {
						 	  	  f=1;
						 	  	  break;
							   }
							   else
							    temp.pb(ff);
						 
			   }
			   if(f==0)
			   {
			   	//cout<<"push "<<v[i]<<endl;
			   	   ans.pb(v[i]);
			   	   for(int k=0;k<9;k++)
			   	   {
			   	     factors[cnt].pb(temp[k]);	 
				   }
				   cnt++;
			   }
	   }
	  // cout<<"cnt "<<cnt<<endl;
	    cout<<"Case #"<<1<<":"<<endl;
	     for(int i=0;i<J;i++)
	     {
	     	     for(int k=n-1;k>=0;k--)
	     	     {
	     	     	  if(ans[i]>>k &1)
	     	     	  {
	     	     	    cout<<"1";	
					   }
					   else cout<<"0";
				  }
				  cout<<" ";
				  for(int k=0;k<9;k++)
				  cout<<factors[i][k]<<" ";
				  cout<<endl;
		 }
     }
	 return 0; 
}
