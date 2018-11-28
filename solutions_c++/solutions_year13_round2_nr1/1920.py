/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
* File Name : a.cpp
* Creation Date : 04-05-2013
* Last Modified : Saturday 04 May 2013 11:23:06 PM IST
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
	LL A,diff,temp,num;
	int i,count,count1,T,t,n,ans,ite,I;
	si(t);
	LL a[101];
	int min[1000];
	rep(T,t)
	{
		sl(A); si(n);
		
		rep(i,n)
		{
			sl(a[i]);

		}
		sort(a,a+n);
		count1=0;
		count=0;
		I=0;
		if(A==1)
			count=n;
		else
		{
		I=0;
		while(1)
		{
			if(I==n)
				break;

			if(A>a[I])
			{	A=A+a[I];
			        I++;
			}
			else
			{
			 min[count1]=count+n-I;
			 count1++;
			 A=A+A-1;
			 count++;
			     
			     
		        }
		}
		}	
			ans=count;
		         rep(ite,count1)
			{
			  if(min[ite]<ans)
				  ans=min[ite];
			}
		
	        		
		printf("Case #%d: %d\n",T+1,ans);
	 
	}
	return 0;
}
