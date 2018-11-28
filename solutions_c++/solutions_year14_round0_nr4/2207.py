#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <vector>
#define ll long long
#define s second
#define f first
#define PB push_back
using namespace std;
map<ll,ll>mpn;
map<ll,ll>mpt;
typedef pair<int,int>pib;

#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main(){
ll cases;
cin>>cases;
for(int t=1;t<=cases;t++){
	 ll n;
	int naomi[100006],ken[100006];
	 cin>>n;
	 double num;
	 	 for(int i=0;i<n;i++){
	 	 cin>>num;
	num=num*100000;
             naomi[i]=num;
         }
             
 for(int i=0;i<n;i++){
	 	 cin>>num;
	num=num*100000;
             ken[i]=num;
         }
             
             qsort(naomi,n,sizeof(int),compare);
             qsort(ken,n,sizeof(int),compare);
             int count1=0,count2=0,index1,index2;
             
             index1=n-1,index2=n-1;
             
                while(index1>=0)
                {
                if(naomi[index1]>ken[index2])
                {
                  
                count1++;
                }
             else
               {
                index2--;
                }
            index1--;
              }        
			  
			index1=0;
			index2=0;

        while(index1<n)
        {
            if(naomi[index1]>ken[index2])
            {
                index2++;
                count2++;
            }
            
            index1++;
        }
		printf("Case #%d: %d %d\n",t,count2,count1);	  
			  
		}
             
cin.get();
return 0;
}

