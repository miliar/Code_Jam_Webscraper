			/* AK_47*/
#include<iostream>
#include<stdio.h>
#include<list>
#include<vector>
#include<map>
#include<algorithm>
#include<set>
#include<string.h>
#include<queue>
#include<stdlib.h>
using namespace std;
#define S(x) scanf("%d",&x)
#define pb(x) push_back(x)
#define V(x) vector<x>
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define REP(i,a,n) for(i=(a);i<(n);++i)

int main()
{
    int t,n,cs=1;
    S(t);
    char a[1010];
    F(i,0,t)
   {  
      // cout<<" i is:"<<i<<"  "<<endl;
       //cs = 0 ;
   	   S(n);
   	   cin>>a;
   	     long long sum= 0,cnt=0 ;
   	     //sum = a[0] - '0';
   	     	F(j,0,n+1)
   	        {
   	           	 if(sum<j)
   	           	   {
   	           	   	 cnt = cnt + j- sum;
   	           	   	 sum = j ;
   	           	   }
   	           	   sum = sum + a[j] - '0'; 
   	        }
   	       if(n==0)
   	       {
   	       	  cout<<"Case "<<" #"<<cs<<" :0"<<endl;
   	       	  cs++;
			     	       }
		    else
		    {
		    
   	       	  cout<<"Case "<<" #"<<cs<<": "<<cnt<<endl;
            cs++;
           }
         //  cout<<" i is : "<<i<<" "<<endl;
   }




return 0;
}

