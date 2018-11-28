#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#define For(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
vector<int> v1,v2;

void nhap1(){
	int vt, x; cin>>vt;
	for(int i=1; i < vt ;i++)
	For(j,1,4) cin>>x;
	For(j,1,4){
		cin>>x; v1.push_back(x);
	}
	for(int i=vt + 1; i <=4 ;i++)
	For(j,1,4) cin>>x;
}

void nhap2(){
	int vt, x; cin>>vt;
	for(int i=1; i < vt ;i++)
	For(j,1,4) cin>>x;
	For(j,1,4){
		cin>>x; v2.push_back(x);
	}
	for(int i=vt + 1; i <=4 ;i++)
	For(j,1,4) cin>>x;
}

int main(){
//	freopen("A.out","w",stdout);
//	freopen("A.in","r",stdin);
	int test; cin>>test;
	For(t,1,test){
		nhap1(); nhap2();
		int dem = 0, gt = 0;
		printf("Case #%d: ",t);
		For(i,0,3)
		For(j,0,3) if(v1[i] == v2[j]){
			dem++; gt = v1[i];
		}
		
		if(dem == 0) printf("Volunteer cheated!\n");
		else if(dem == 1) printf("%d\n",gt);
		else printf("Bad magician!\n");
		v1.clear(); v2.clear();
	}
	
	return 0;
}
