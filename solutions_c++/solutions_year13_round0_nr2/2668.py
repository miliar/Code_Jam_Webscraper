
/*
Author Name::Himanshu Tomar
Lang::C++
*/

// header files

#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cassert>
#include<utility>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<iomanip>
#include<map>
#include<set>
#include<ctime>
#include<cstring>
#include<cmath>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

// definitions

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define ppb() pop_back()
#define ll long long int
#define s(a) scanf("%d",&a)
#define clr(x) memset(x,0,sizeof(x))
#define bs(a,b,c) binary_search(a,b,c)
#define ub(a,b,c) upper_bound(a,b,c)
#define lb(a,b,c) lower_bound(a,b,c)
#define mod 1000000007
using namespace std;

void init()
{}

int main()
{
     freopen("C:\\Users\\JI\\Desktop\\input.txt","r",stdin);
     freopen("C:\\Users\\JI\\Desktop\\output.txt","w",stdout);
      int tc,in=1;
      s(tc);
      while(tc--)
      {
                 int m,n;
                 bool flag=false;
                 scanf("%d%d",&m,&n);
                 
                 int arr1[m][n],arr2[m][n];
                 
                 for(int i=0;i<m;i++)
                 for(int j=0;j<n;j++)
                 {
                 	s(arr1[i][j]);
                 	arr2[i][j]=2;
                 }
                 
                 for(int i=0;i<m;i++)
                 {
                 	flag=false;
                 	for(int j=0;j<n;j++)
					{
						if(arr1[i][j]!=1)
							{
								flag=true;
								break;
							}
							
					}
                 	if(!flag)
					{
						for(int j=0;j<n;j++)
							arr2[i][j]=1;
					}
                 }
                    for(int i=0;i<n;i++)
                     {flag=false;
                 	for(int j=0;j<m;j++)
					{  
						if(arr1[j][i]!=1)
							{
								flag=true;
								break;
							}
							
					}
                 	if(!flag)
					{
						for(int j=0;j<m;j++)
							arr2[j][i]=1;
					}
                     }
                     flag=true;
                     for(int i=0;i<m;i++)
						for(int j=0;j<n;j++)
					 {
					 	if(arr1[i][j]!=arr2[i][j])
						{
							//cout<<i<<" "<<j<<" "<<arr1[i][j]<<" "<<arr2[i][j]<<endl;
							flag=false;
							break;
						}
					 }
					 
					 if(flag)
						printf("Case #%d: YES\n",in);
					 else
						printf("Case #%d: NO\n",in);
              in++;
      }
                 return 0;
      }