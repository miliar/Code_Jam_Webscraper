#include <iostream>
#include <cstdio>
using namespace std;
int t;
int main(){
 	freopen("b_input","rt",stdin);
 	freopen("b_output","wt",stdout);
 	cin>>t;
 	for(int x=1;x<=t;x++) {
 		bool pos=1;
 		int n,m,a[200][200],mi[200],mj[200];
 		cin>>n>>m;
 		for(int i=0;i<m;i++) mj[i]=0;
 		for(int i=0;i<n;i++) { 
 			mi[i]=0;
 			for(int j=0;j<m;j++) {
 				cin>>a[i][j];
 				if(mi[i]<a[i][j]) mi[i]=a[i][j];
 				if(mj[j]<a[i][j]) mj[j]=a[i][j];
 			}
 		}
 		for(int i=0;i<n;i++) 
 			for(int j=0;j<m;j++) {
 			 	if((a[i][j]<mi[i])&&(a[i][j]<mj[j])) pos=0;	
 			}
 		printf("Case #%d: %s\n",x,(pos?"YES":"NO"));
 	}
 	return 0;
}