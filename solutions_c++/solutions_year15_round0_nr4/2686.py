#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>

#define ull unsigned long long
#define sz (int)1e7

using namespace std;

int arr[sz];

int solve()
{
	int v,r,c;
	cin>>v>>r>>c;
	if(v>=7)
		return 0;
	if(v==1)
		return 1;
	int max=r;
	if(c>r)
		max=c;
	if(v>max)
		return 0;
	if((r*c)%v!=0)
		return 0;
	if(v==2)
		return 1 ;

	if(r>c){
		int temp=r;
		r=c;
		c=temp;
	}
	for(int i=1;i<=v;i++){
		int a=i;
		if(a>r && a>c)
			return 0;
		int b=v/i;
		if(a>b){
			int temp=a;
			a=b;
			b=temp;
		}
		if(a<=r && b<=c)
			continue;
		return 0;
	}
	int rem=0;
	if(v>r)
		rem=v-r;
	if(v>(r) && (rem+1)>r)
		return 0;
	for(int i=1;i<=rem;i++){
		for(int l=0;l<=i;l++){
			int rt=i-l;
			if(l==0 || (l+1+rt)<r)
				continue;
			else{
				if((l+v)%r!=0){
					return 0;
				}
			}
			if(rt==0)
				continue;
			else{
				if((rt+v)%r!=0){
					return 0;
				}
			}		
		}
	}
	rem=0;
	if(v>c)
		rem=v-c;
	for(int i=1;i<=rem;i++){
		for(int l=0;l<=i;l++){
			int rt=i-l;
			if(l==0 || (l+1+rt)<c)
				continue;
			else{
				if((l+v)%c!=0)
					return 1;
			}
			if(rt==0)
				continue;
			else{
				if((rt+v)%c!=0)
					return 1;
			}		
		}
	}
	return 1;
}

int main() 
{
	freopen("small.in","r",stdin);
	freopen("out","w",stdout);
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		cout<<(solve()?"GABRIEL":"RICHARD");
		cout<<endl;
	}
	return 0;
}
