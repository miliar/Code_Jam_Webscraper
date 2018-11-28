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
ll t;

scanf("%ld",&t);
for(int k=1;k<=t;k++){
	int a[4][4],b[4][4];
	ll ans1,ans2,count=0,num;
	scanf("%ld",&ans1);
	
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++){
		scanf("%ld",&a[i][j]);
	}
scanf("%ld",&ans2);

	
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++){
		scanf("%ld",&b[i][j]);
	}

        for(int i=0;i<4;i++){
        	for(int j=0;j<4;j++){
        		if(a[ans1-1][i]==b[ans2-1][j]){
                         count++;
                         num=b[ans2-1][j];
                         
                     }  }}
                    
                    cout<<"Case #"<<k<<": ";
                     if(count==0)
                     cout<<"Volunteer cheated!"<<endl;
                      else if(count==1)
                      cout<<num<<endl;
                      else
                       cout<<"Bad magician!"<<endl;
				
				
			}
                 
cin.get();
return 0;
}

