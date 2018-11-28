#include <iostream>
#include <cstdio>
#define NAME "c-large"
using namespace std;
int T;
int main(){
	freopen(NAME".in","rt",stdin);
	freopen(NAME".out","wt",stdout);
	cin>>T;
	for(int I=1;I<=T;I++) {
		printf("Case #%d:\n",I);
		int r,c,m,f;
		cin>>r>>c>>m;
		bool ok=0;
		if(r==1||c==1) {
			cout<<'c'<<(c==1?"\n":"");
			for(int i=1;i<(r==1?c:r);i++)
				if (r*c-m > i) cout<<"."<<(c==1?"\n":"");
				else cout<<"*"<<(c==1?"\n":"");
				if(r==1) cout<<"\n";
		} else if(r*c-m==1) {
			for(int i=0;i<r;i++) {
				for(int j=0;j<c;j++) {
					cout <<((i||j)?'*':'c');
				}
				cout<<endl;
			}
		} else {
			for(int b1=2;b1<=c && !ok;b1++) {
				for(int a1=2;a1<=r && !ok;a1++) {
					for(int b2=b1;b2<=c && !ok;b2++) {
						for(int a2=a1;a2<=r;a2++) {
							int s=(c-b2)*r+(r-a2)*c-(r-a2)*(c-b2);
							if(s<=m && s+(b2-b1)*(a2-a1)>=m) {
								ok=1;
								m-=s;
								char map[100][100];
								for(int i=0;i<a2-a1;i++) {
									for(int j=0;j<b2-b1;j++) {
										if(m>0) map[i][j]='*';
										else map[i][j]='.';
										m--;
									}
								}
								for(int i=1;i<=r;i++) {
									for(int j=1;j<=c;j++) {
										if(i==1&&j==1) cout<<'c';
										else {
											if(i>a2 || j>b2) cout<<'*';
											else {
												if(i>a1&&j>b1) {
													cout<<map[a2-i][b2-j];
												} else cout<<'.';
											}
										}
									}
									cout<<endl;
								}
								break;
							}
						}
					}
				}
			}
			if(!ok) cout<<"Impossible\n";
		}
	}
	return 0;
}