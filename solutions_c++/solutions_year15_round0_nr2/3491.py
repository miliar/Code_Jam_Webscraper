#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<sstream>
#include<set>
#include<climits>
#define gc getchar
#define f first
#define s second
#define TEST int T = scan(); for(int t=1; t<=T; t++)
int arr[1000];
using namespace std;
typedef int ll;
int scan() 
{
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  ll ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
int che(int a, int b)
{ 
	if(a%b==0) 
		return a/b-1;  
	return a/b; 
} 
int main()
{
	TEST
	{
		int D, res;
		D = scan();
		int mval=0;
 		for(int i=0; i<D; i++) 
 		{ 
 			arr[i] = scan();
 			mval=max(arr[i],mval);
 		} 
 		res=INT_MAX; 
 		for(int x=1; x<=mval; x++) 
 		{ 
 			int y=x; 
 			 for(int i=0;i<D;i++) 
 			 	if(arr[i]>x) 
 			 		y += che(arr[i],x); 
 		 	res=min(res,y);
 		}	
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
