/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
* File Name : c.cpp
* Creation Date : 13-04-2013
* Last Modified : Saturday 13 April 2013 07:18:56 PM IST
* Created By :  Vishal Gupta
_._._._._._._._._._._._._._._._._._._._._.*/
                                   
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include<stack>
#include<vector>
#include<cstring>
#include<set>
#include<map>
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pil(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
typedef long long int LL;
using namespace std;
int main()
{
      int T,t,count,i;
      LL a,b;
      LL pre [] = {1 ,4 ,9 ,121 ,484 ,10201 ,12321 ,14641 ,40804 ,44944 ,1002001 ,1234321 ,4008004 ,100020001 ,102030201 ,104060401 ,121242121 ,123454321 ,125686521 ,400080004 ,404090404 ,10000200001 ,10221412201 ,12102420121 ,12345654321 ,40000800004 ,1000002000001 ,1002003002001 ,1004006004001 ,1020304030201 ,1022325232201 ,1024348434201 ,1210024200121 ,1212225222121 ,1214428244121 ,1232346432321 ,1234567654321 ,4000008000004 , 4004009004004 };
     si(t);
     rep(T,t)
     {
           sl(a); sl(b);
           count=0;
	   for(i=0; i<39; i++)
	   {
	      if(pre[i]>=a)
	      {
	              if(pre[i]>b)
			      break;
		      else
			      count++;
	      }
	   }
       printf("Case #%d: ",T+1); pil(count);
     }
      return 0;
}
