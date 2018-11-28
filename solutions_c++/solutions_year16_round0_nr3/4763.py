#include<bits/stdc++.h>
#define ll long long int
#define ull unsigned long long
#define pb push_back
#define in     insert
#define all(v) v.begin(),v.end()
#define rep(s,n) for(ll i=s;i<n;i++)
#define rep1(s,n) for(ll i=s;i<=n;i++)
#define TC()      ull t;cin>>t;while(t--)
#define mk make_pair
#define endl '\n'
#define vitr vector<ll>::iterator
#define sitr set<ll>::iterator

using namespace std;
void FastIO(){ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);}

bool p[10000001];
void seive(ll n)
{
	memset(p,true,sizeof(p));
	
   p[0]=false;
   p[1]=false;
   p[2]=true;
   for(ll i=2;i<=n;i+=1)
   {
    	if(p[i]==true)
		for(ll j=2;j*i<n;j++)
    			p[i*j]=false;
   }    
}
int arr[17];
   
ull foo(int  base)
{
	ull ans=0,mul=1;
	for(int i=15;i>=0;i--,mul*=base)
	if(arr[i]==1) ans+=mul;
	
	return ans;
}

ull show_div(ull num)
{
	ull i;
	if(i<10000001&&p[i]) return 0;
//	
	for(i=2;i<=sqrt(num);i++)
     if(num%i==0) return i;

return 0;
}

void set_str(int num)
{
      int tp=num,idx=15;
	while(tp)
       {
   	if((tp&1)==1)  arr[idx]=1;//cout<<"1";
   	else            arr[idx]=0;//cout<<"0";
   	tp>>=1;
      idx--;
      }

}
int main()
{
  FastIO();
  ifstream cin("inputfile.txt");
  ofstream cout("out.txt");
   
seive(10000001);
   int ct=0;
   int t,T,len,hmany;
   cin>>T;
   vector<ull> vec;
   ull get_no;
   ull divv=0;
   for(int t=1;t<=T;t++)
   {
     ct=0;
     cin>>len>>hmany;
     cout <<"Case #"<<t<<": "<<endl;
    		
  for( int num=32769;(num<=65535)&&(ct<hmany);num++)
  {          
   	    divv=0;
		 if( p[num]==false && (num&1) && (num&(1<<15) ) )
		       {           //cout<<num<<" ";
		
					set_str(num);
				 
				   for(int base=3;base<=10;base++)
  			  	     {
  				        get_no=foo(base);
  	                          divv=show_div(get_no);
 				         if(divv==0) 
					   {
						vec.clear();
						break;
					   }  
		                    else vec.pb(divv);
					}
                if(divv==0) vec.clear();
		    else 
		    {
		    	for(int i=0;i<=15;i++) cout<<arr[i]; //showing actual string
				 cout<<" "<<show_div(num)<<" ";       //showing the list fo non trival divisors
				 
		    for(int i=0;i<vec.size();i++) cout<<vec[i]<<" ";
		    vec.clear();
		    ct++;
	          cout<<endl;
		    }
		    
		    }
   }
 }
   return 0;
}

