#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

#define FOR(i,c,n) for(int i=(c) ; (i)<(n) ; ++(i))
#define FR(i,n) FOR(i,0,n)

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;
	FR(cas,t){
		printf("Case #%d: ",cas+1);
		int k1,k2;
		int a[4][4],b[4][4];
		cin>>k1;k1--;FR(i,4)FR(j,4)cin>>a[i][j];
		cin>>k2;k2--;FR(i,4)FR(j,4)cin>>b[i][j];
		int res=0,num=0;
		FR(i,4)FR(j,4){
			if(a[k1][i]==b[k2][j]) {res++;num=a[k1][i];}
		}
		if(res==1) cout<<num<<endl;
		else if(res==0) cout<<"Volunteer cheated!"<<endl;
		else cout<<"Bad magician!"<<endl;
	}

}