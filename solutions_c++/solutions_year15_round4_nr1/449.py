
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
const int N= 2e5+10;
int bit[N],n;
int Sum(int i){
    int ret=0;
    while(i>0){
        ret+=bit[i];
        i-=i&-i;
    }
    return ret;
}
void add(int i,int t,int val){
    while(i<=t){
        bit[i]+=val;
        i+=i&-i;
    }
}
int erfen(int val){
    int l=1,r=n,mid;
    while(l<r){
        mid=(l+r)/2;
        if(Sum(mid)<val){l=mid+1;}
        else{r=mid;}
    }
    add(r,n,-1);
    return r-1;
}
int main(){

	//freopen("in.txt","r",stdin);
	int p=0,np=1;
	cin >> n;
	memset(bit,0,sizeof(bit));
	for(int i=1;i<=n;i++) np*=i;

	for(int k=0;k<2;k++){
        for(int i=1;i<=n;i++) add(i,n,1);
        int nq=np;
        for(int i=0,a;i<n;i++){
            scanf("%d",&a);
            nq/=(n-i);
            p+=Sum(a)*nq;
            add(a+1,n,-1);
        }
	}
	p%=np;
	for(int i=1;i<=n;i++) {add(i,n,1);}
	for(int i=0;i<n;i++){
        np/=(n-i);
        int ans=p/np;
        p%=np;
        cout << erfen(ans+1) << " ";
	}
	return 0;
}
