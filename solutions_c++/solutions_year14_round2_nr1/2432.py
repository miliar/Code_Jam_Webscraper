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
map<ll,ll>mp;
typedef pair<int,int>pib;

#define SWAP(a, b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main(){
int cases;
cin>>cases;
ll n,count1,count2,ans=0,temp;
char a[101],b[101];
for(int t=1;t<=cases;t++){
	temp=0;
	cin>>n;
	cin>>a>>b;
	
	ll i=0,j=0;
	if(a[0]==b[0]){
		ans=0;
	     while(i<strlen(a)&&j<strlen(b))
	     {
	     	count1=1,count2=1;
	     	while(a[i]==a[i+1])
                {
                    count1++;
                    i++;
                }
                while(b[j]==b[j+1])
                {
                    count2++;
                    j++;
                }

            if(count1>count2)
                    ans=ans+(count1-count2);
                else
                    ans=ans+(count2-count1);
                i++;
				j++;
				
				 if(a[i]!=b[j])
                {
                     temp=1;
                    break;
                }
            }
            if(temp==1)
                    printf("Case #%d: Fegla Won\n",t);
                else
                    printf("Case #%d: %d\n",t,ans);
 
 
        }
        else
           printf("Case #%d: Fegla Won\n",t);
    }


cin.get();
return 0;
}

