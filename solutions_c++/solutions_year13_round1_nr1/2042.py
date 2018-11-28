#define PI (3.14159265358979323846)
#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
#define ull unsigned long long
using namespace std;
ull find(ull pre,ull ra){
	return (ra*ra)-(pre*pre);
}
int main(){
	freopen("A-small-attempt0 (2).in","r",stdin);
	freopen("output.txt","w",stdout);
	ull t=0;
	cin>>t;
	ull count=0;
	while(t--){
		count++;
		ull r,tt,pre;
		cin>>r>>tt;
		ull orp=0;
		while(1){
			pre=r;
			ull km=find(pre,++r);
			if(km>tt)break;
			tt-=km;
			orp++;
			++r;
		}
		cout<<"Case #"<<count<<": ";
		cout<<orp<<endl;
	}
	return 0;
}