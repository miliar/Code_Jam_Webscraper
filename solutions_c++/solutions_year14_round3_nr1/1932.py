#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<fstream>
#include <cstring>
#include<cmath>
#include<sstream>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<utility>
#include<algorithm>
using namespace std;

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

int main()
{   char ch;
    int t,i,j;
    cin>>t;
	for(j=1;j<=t;j++)
	{   
	    long long int a,b,c=0;
	    char arr[25];
		cin>>arr;

        for(i=0;i<strlen(arr);i++)
        if(arr[i]=='/')
        break;
        
        a=atoi(arr);
        b=atoi(arr+i+1);
            
    int ans=0;
    bool f=false;
    while(a!=1 || b!=1)
    {   // cout<<a<<" -- "<<b<<"\n";
	     if(b%2==0)
         {
             b=b/2;
             
			 if(f==false)
             ans++;
           //  cout<<ans<<"  ** \n";
             if(a==1 && b==1)
             break;
             else if(a>b)
             {
             	f=true;
             	a=a-b;
             }
         }
         else {ans=-1;break;
         }
    if(a==b)
    {a=1;b=1;
    }
    }
	if(ans!=-1)
	cout<<"Case #"<<j<<": "<<ans<<"\n";
	else
	cout<<"Case #"<<j<<": impossible\n";
	}
	return 0;

}


