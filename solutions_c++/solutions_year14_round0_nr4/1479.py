#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
double a[1001],b[1001];
int f[1001][1001],done[1001];
int n;
void init(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=n;i++) cin>>b[i];
    sort(a+1,a+n+1);
    sort(b+1,b+n+1);
}
int max(int i,int j){
	return(i>j?i:j);
}
int find(double x){
    int i,y=-1;
    for(i=n;i>=1;i--){
		if(b[i]>x&&done[i]==0) y=i;
    }
    if(y!=-1){
		done[y]=1;
		return(0);
    }
    for(i=1;i<=n;i++){
		if(done[i]==0){
            done[i]=1;
            return(1);
		}
    }
}
void dp(){
    memset(f,0,sizeof(f));
    memset(done,0,sizeof(done));
    int i,j;
    for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
            int x=(a[i]>b[j]);
            f[i][j]=max(f[i][j-1],f[i-1][j]);
            f[i][j]=max(f[i][j],f[i-1][j-1]+x);
		}
    }
	int s=0;
	for(i=n;i>=1;i--){
		s=s+find(a[i]);
	}
	cout<<f[n][n]<<" "<<s<<endl;
}
int main(){
	freopen("D-large.in","r",stdin);
	freopen("4.out","w",stdout);
    int T,C;
    cin>>T;
    for(C=1;C<=T;C++){
			init();
		cout<<"Case #"<<C<<": ";
		dp();
    }
}
