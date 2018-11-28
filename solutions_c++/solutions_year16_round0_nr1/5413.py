#include<bits/stdc++.h>
using namespace std;
int h[20];
#define ll long long int 
void upd(ll val)
{
	  while(val!=0)
	  {
	  	  int rem=val%10;
	  	  h[rem]++;
	  	  val/=10;
	  }
}
int main()
{
	 int t;
//	 freopen("abc.txt","r",stdin);
//	 freopen("out.txt","w",stdout);
	 cin>>t;
	 int tt=0;
	 while(t--)
	 {
	 	  tt++;
	 	  ll n;
	 	  cin>>n;
	 	  ll val=n;
	 	  if(n==0)
	 	  {
	 	     cout<<"Case #"<<tt<<": INSOMNIA"<<endl;	
		       continue;
		  }
	 	  int last=2;
	 	  memset(h,0,sizeof(h));
	 	  while(1)
	 	  {
	 	  //	cout<<val<<endl;
	 	     upd(val);
	 	     bool f=0;
			  for(int i=0;i<=9;i++)
			  {
			      if(h[i]>0)
				  {
				  	  continue;
				  }
				  else {
				      f=1;
					  break;	  
				  }	
			  }
			  if(f)
			  {
			       val=last*n;
				   last++;	
			  }else break;	  
		  }
		  cout<<"Case #"<<tt<<": "<<val<<endl;
		  
	 }
	 return 0;
}
