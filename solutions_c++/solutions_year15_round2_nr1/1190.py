#include<iostream>
#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;
typedef long int li;
#define ff first
#define ss second
#define mod 1000000007;
int hashy[10000001];
lli min(lli i,lli j)
 {
 	if(i>j)return i;
 	else return j;
 }
 lli gcd (lli a,lli  b)
  {
  	if(a%b==0)return b;
  	else return gcd(b,a%b);
  }

int main()
 {
 	 freopen("abc.txt","r",stdin);
   	freopen("pqr.txt","w",stdout);
 	int t;
 	 cin>>t;
 	 lli tt=1;
 	 while(t--)
 	 {


 	 lli  n;
 	 cin>>n;
     for(int i=0;i<=n;i++)hashy[i]=10000001;
 	 queue<pair<lli,lli> > q;
	   q.push(make_pair(1,1));
	    while(!q.empty())
		 {
		 	   lli numb=q.front().ff;
		 	   lli val=q.front().ss;
		 	   q.pop();
		 	   if(numb==n)
		 	    {
		 	    	 cout<<"Case #"<<tt++<<": "<<val<<endl;
		 	    	 break;

		 	    }
		 	    else
		 	     {
		 	     	if(numb+1<=n  && hashy[numb+1]>val+1)
					  {
					  	q.push(make_pair(numb+1,val+1));
					  	hashy[numb+1]=val;
					  }
		 	         lli rever=0;
		 	          while(numb!=0)
		 	           {
		 	           	rever=rever*10+numb%10;
		 	           	numb/=10;
		 	           }
		 	           if(rever<=n  &&  hashy[rever]>val+1)
		 	            {
		 	            	q.push(make_pair(rever,val+1));

		 	            }
		 	     }

		 }
	}
		 return 0;
 }
