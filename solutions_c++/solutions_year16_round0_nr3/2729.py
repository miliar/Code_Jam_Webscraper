#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1e9+7
vector<ll> v;
ll pno=0;
bool prime(ll n)
{
	bool f=0;
	for(ll  i=2;i*1LL*i<=n;i++)
	{
		if((n%i)==0)
		{
			f=1;
			pno=i;
			break;
		}
	}
    if(!f) return 1;
	return 0;	
}

bool check(string a)
{
	ll n=a.length();
  for(ll i=2;i<=10;i++)
  {
 	 bool temp=0;
     ll num=0;
  	 for(ll j=n-1;j>=0;j--)
  	 {
  	 	if(a[j]=='1')
        num+=powl(i,n-j-1);    	 	
  	 }
  	 temp=prime(num);
     if(temp==1)
     return 0;

    v.push_back(pno);
  } 	
   return 1;   
}

vector<string> vec;
string s;
void init(ll index,ll n)
{
    if(index==n)
    {
    	vec.push_back(s);
        return ; 
    }
    s+='0';
    init(index+1,n);
    s.resize(s.length()-1);
 	s+='1';
    init(index+1,n);
    s.resize(s.length()-1);   	
}

int main()
{
  //freopen("in.txt","r",stdin);
  //freopen("out.txt","w",stdout);
  ll t;
  cin>>t;
  for(ll test=1;test<=t;test++)
  {
       ll n,j;
       ll count=0;
       cin>>n>>j;
         string a;
        init(0,n-2);
       ll i;
       cout<<"Case #"<<test<<": "<<endl;
     bool f=0;
	 for( i=0;i<vec.size();i++)	   	  
    {   //	        cout<<a<<" ";
              f=0;
			  	 a+='1';
              for(ll w=0;w<vec[i].length();w++)
              a+=vec[i][w];
              a+='1';
           	  if(check(a))
              {
                  	f=1;
             		count++;
                    cout<<a<<" ";
              }
			  if(v.size()==9)
			  {
			  
			  for(auto it:v)
   	 	        {
                           cout<<it<<" ";
		        }
		  	 } 
              if(f) cout<<endl;
        	if(count==j)
       	  break;
          v.clear();
         a.clear();
       }
  }
  return 0;
}
