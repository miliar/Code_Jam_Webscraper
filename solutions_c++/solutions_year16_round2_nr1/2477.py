//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int

int main() {
	ios::sync_with_stdio(false);
	int t,tc=1;
	cin>>t;
	while(t--){
		string s;
		int ans[10];
		for(int i=0;i<10;i++) ans[i]=0;
		cin>>s;
		int nz=0,nw=0,nu=0,nx=0,ng=0,no=0,nt=0,nf=0,ns=0,nn=0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='Z')
				nz++;
			if(s[i]=='W')
				nw++;
			if(s[i]=='U')
				nu++;
			if(s[i]=='X')
				nx++;
			if(s[i]=='G')
				ng++;
			if(s[i]=='O')
				no++;
			if(s[i]=='T')
				nt++;
			if(s[i]=='F')
				nf++;
			if(s[i]=='S')
				ns++;
			if(s[i]=='N')
				nn++;
		}
		ans[0]=nz;
		ans[2]=nw;
		ans[4]=nu;
		ans[6]=nx;
		ans[8]=ng;
		ans[1]=no-(nz+nw+nu);
		ans[3]=nt-nw-ng;
		ans[5]=nf-nu;
		ans[7]=ns-nx;
		ans[9]=(nn-ans[1]-ans[7])/2;
		cout<<"Case #"<<tc<<": ";
		for(int i=0;i<10;i++){
			if(ans[i]!=0){
				for(int j=0;j<ans[i];j++){
					cout<<i;
				}
			}
		}
		cout<<"\n";
		tc++;
	}
	return 0;
}