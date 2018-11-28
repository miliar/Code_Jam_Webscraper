#include<stdio.h>
#include<iostream>
using namespace std;
int a[5][5],b[5][5];
int r1,r2;
void f(){
	int i,j,ret=-1;
	for(i=1;i<=4;i++){
		for(j=1;j<=4;j++){
            if(b[r2][j]==a[r1][i]){
                if(ret==-1){
					ret=a[r1][i];
                }
                else{
					cout<<"Bad magician!"<<endl;
					return;
                }
            }
		}
	}
    if(ret==-1) cout<<"Volunteer cheated!"<<endl;
    else cout<<ret<<endl;
}
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
		cin>>r1;
		for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) cin>>a[i][j];
		cin>>r2;
		for(int i=1;i<=4;i++) for(int j=1;j<=4;j++) cin>>b[i][j];
		cout<<"Case #"<<C<<": ";
		f();
    }
}
