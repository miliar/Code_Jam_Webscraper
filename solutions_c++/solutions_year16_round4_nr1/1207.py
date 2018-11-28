#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;


int rep[3];
int arr[30000];
char arr2[31111];
void solve(int l,int r,int curr){
	if(l==r){
		rep[curr]++;
		arr[l]=curr;
		return;
	}
	int mid=(r+l)/2;
	solve(l,mid,curr);
	solve(mid+1,r,(curr+2)%3);
	
}
void solve2(int l,int r){
	if(l==r)return;
	int mid=(r+l)/2;
	int len=(r-l+1)/2;
	solve2(l,mid);
	solve2(mid+1,r);
	bool is_swap=false;
	for(int i=l;i<=mid;i++){
		if(arr2[i] > arr2[i+len]){
			is_swap=true; 
			break;
		} else if(arr2[i] < arr2[i+len]){
			break;
		}
	}
	if(is_swap){
		for(int i=l;i<=mid;i++){
			swap(arr2[i],arr2[i+len]);
		}
	}
}
int T;
int n;
char gett(int x){
	if(x==0)return 'R';
	if(x==1)return 'P';
	if(x==2)return 'S';
}
int main(){
	freopen("aaaa.in","r",stdin);
	freopen("bbb.txt","w",stdout);
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		cin>>n;
		for(int i=0;i<3;i++){
			rep[i]=0;
		}
		solve(0,(1<<n)-1,0);
		int inp[3];
		for(int i=0;i<3;i++){
			cin>>inp[i];
		}
		int sh;
		for(sh=0;sh<3;sh++){
			bool ok=true;
			for(int j=0;j<3;j++){
				if(rep[j]!=inp[(sh+j)%3]){
					ok=false;
				}
			}
			if(ok)break;
		}
		cout<<"Case #"<<tt<<": ";
		if(sh==3){
			cout<<"IMPOSSIBLE"<<endl;
		} else {
			//solve(0,(1<<n)-1,sh);
			for(int i=0;i<(1<<n);i++){
				arr2[i]=gett((arr[i]+sh)%3);
			}
			solve2(0,(1<<n)-1);
			for(int i=0;i<(1<<n);i++){
				cout<<arr2[i];
			}
			cout<<endl;
		}
	}
}