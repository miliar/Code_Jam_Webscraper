#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
#include<stack>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define EPS (1e-7)
#define PI (acos(-1.0))
#define MAXI(a,b) ((a)>(b)?(a):(b))
#define MINI(a,b) ((a)<(b)?(a):(b))
#define mxx 1005
#define SZOF sizeof
#define SZ size
typedef long long INT;

INT arr[205];
int n;

int req_steps(int i,INT mote,int lvl){
	mote+=(mote-1);
	for(i;i<n;i++){
		if(arr[i]<mote){
			mote+=arr[i];
		}
		else{break;}
	}
	if(lvl>n){return 1000000;}
	if(i==n){return 1;}
	else if(mote>arr[n-1]){return 1;}
	return MINI(req_steps(i,mote,lvl+1),(n-i))+1;

}


int main(){
	int i,j,tst,cas=1,mote,ans;
	freopen("A-large.in","r",stdin);
	freopen("output2.txt","w",stdout);

	scanf("%d",&tst);

	while(tst--){
		scanf("%lld%d",&mote,&n);
		for(i=0;i<n;i++){
			scanf("%lld",&arr[i]);
		}
		if(mote==1){printf("Case #%d: %d\n",cas++,n);continue;}
		sort(arr,arr+n);
		for(i=0;i<n;i++){
			if(arr[i]<mote){
				mote+=arr[i];
			}
			else{break;}
		}
		if(i==n){ans=0;}
		else{ans=MINI(req_steps(i,mote,0),(n-i));}
		printf("Case #%d: %d\n",cas++,ans);	
	}
	

	//system("pause");
	return 0;
}

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);