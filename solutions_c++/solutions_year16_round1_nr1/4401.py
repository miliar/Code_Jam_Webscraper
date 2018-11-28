#include<stdio.h>
#include <bits/stdc++.h>
#include<string.h>
using namespace std;
int main()
{   freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,t,k,i,j;
    string b;
    //b.max_size(1001);
    char c;
    scanf("%d",&t);
    k=1;
    while(t--)
    { string a;
	  cin>>a;
      n=a.length();
      b.resize(1);
      b.at(0)=a.at(0);
      j=b[0];
     // cout<<"11b="<<a.at(0)<<endl;
      for(i=1;i<=n;i++)
      { if(a[i]>=j)
       { c=a[i];
	     //b.insert(0,1,c);
	   //  cout<<b.size()<<endl;
	     b.resize(i+1);
	     b.insert(0,1,c);
	     j=a[i];
	    // cout<<"b="<<b<<endl;
;	   }
         
        else
		{ c=a[i];
	      //b.insert(i,1,c);
	      b.resize(i+1);
	      b.insert(i,1,c);
	     //  cout<<b.size()<<endl;
	   }
	  }
	  
	   printf("Case #%d: ",k);
	  cout<<b<<endl;
	  
	  k++;
    }
	 
	  return 0;
	  
	}
