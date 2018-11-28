#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
int has[10];
int main()
{
	 freopen("abc.txt","r",stdin);
	 freopen("pqr.txt","w",stdout);
	int t;
	 cin>>t;
	 int cas=1;
	 while(t--)
	  {
	  	 cout<<"Case #"<<cas++<<": ";
	  	 lli num;
	  	  cin>>num;
	  	 //map<lli,int> ma;
	  	 int op=0;
	  	  memset(has,0,sizeof has);
	  	  int cov=0;
	  	  int f=0;
	  	  while(op<=10000)
	  	   {
	  	   	 //  cout<<" op "<<op<<endl;
	  	   	 op++;
	  	   	 lli temp=num*op;
	  	   	 while(temp!=0)
	  	   	  {
	  	   	  	 // cout<<" temp "<<temp<<endl;
	  	   	  	  if(has[temp%10]==0)
	  	   	  	   {
	  	   	  	   	has[temp%10]++;
	  	   	  	   	//  cout<<"  map "<< temp%10<<endl;
	  	   	  	   	 cov++;
						  }
						   
						  temp/=10;
			  }
			  if(cov==10)
			   {
			   	f=1;
			   	 cout<<num*op<<endl;
			   	 break;
			   }
		   }
		   if(f==0)
		    cout<<"INSOMNIA"<<endl;
	  }
	
}
