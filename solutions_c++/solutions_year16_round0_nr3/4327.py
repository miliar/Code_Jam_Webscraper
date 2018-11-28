#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
bool prime[1000111];
lli fact(lli num)
 {
 	
 	 lli sqr=sqrt(num);
 	 for(int i=2;i<=sqr;i++)
 	 {
 	 	 if(num%i==0) return i;
	  }
	  
	  return 0;
 }
 
 string bin(lli num)
  {
  //	cout<<" converssion of "<<num<<" ";
  	  string s;
  	  while(num!=0)
  	   {
  	   	 if(num%2==0)
  	   	 s+='0';
  	   	 else s+='1';
  	   	 num/=2;
		 }
		   
		  //cout<<s<<endl;
		  string ss;
		for(int i=15;i>=0;i--) ss+=s[i];
		  return ss;
  }
  
lli base(lli num,int bas,int deg)
 {
 	 lli ret=0;
 	 lli temp=num;
 	 int bit=0;
 	   for(int i=0;i<deg;i++)
 	    {
 	    	 if(num & (1<<i))
 	    	  {
 	    	  	 ret+=pow(bas,i);
			   }
		 }
		 return ret;
		 
 }
 
 


 vector<lli> v;
  int check(lli num)
   {

		  
		  	 lli sqr=sqrt(num);
		  	   for(int i=2;i<=sqr;i++)
		  	      {
		  	    	if(num%i==0) return 1;
				  }

		  return 0;
   }
int main()
{
	
	freopen("abc.txt","r",stdin);
	freopen("pqr.txt","w",stdout);
	
	int t;
	 cin>>t;
	 int cas=1;
	 while(t--)
	 {
	 	 cout<<"Case #"<<cas++<<":"<<endl;
	 	 lli n,m;
	 	 cin>>n>>m;
	 	 int cov=0;
	 	 lli maxi=1<<n;
	 	 int cc=0;
	 	 for(int i=0;i<maxi && cc<m;i++)
	 	  {
	 	  	 if(((i & 1)==0 )     || (i & (1<<(n-1)))==0) continue;
	 	  	 else
	 	  	     {
	 	  	     	 
	 	  	     	int f=0;
	 	  	     	
	 	  	     	  for(int  j=2;j<=10;j++)
	 	  	     	       {
	 	  	     	   	         lli num=base(i,j,n);
	 	  	     	   	          
	 	  	     	   	         if(check(num)==0)
	 	  	     	   	         {
	 	  	     	   	         	f=1;
	 	  	     	   	         	break;
								}
						   }
						   if(f==0)
						   {
						   	// cout<<" valid num "<<i<<" "<<cc<<endl;
						   	v.push_back(i);
						   	cc++;
						   }
				 }
		   }
		   
		   int siz=v.size();
		   
		   for(int i=0;i<siz;i++)
		    {
		    	lli num=v[i];
		    	vector<lli> temp;
		    	temp.push_back(num);
		    	for(int i=2;i<=10;i++)
		    	 {
		    	 	  lli val=base(num,i,n);
		    	 	  lli fac=fact(val);
		    	 	  if(fac!=0)
		    	 	    {
		    	 	   	  temp.push_back(fac);
						}
				 }
				 if(temp.size()==10)
				 {
				 	  cout<<bin(temp[0])<<" ";
				 	  for(int i=1;i<=9;i++) cout<<temp[i]<<" ";
				 	   cov++;
				 	    cout<<endl;
				 }
				 //else cout<<" checking fail ";
				 if(cov==m) break;
				  
		    		
			}
		//	 cout<<" bim of "<<bin(11);
	 	  
	 }
}
