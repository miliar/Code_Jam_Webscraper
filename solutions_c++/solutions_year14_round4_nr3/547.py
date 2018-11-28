#include<bits/stdc++.h>
using namespace std;
const int inf=9999999;
int X0[1024],Y0[1024],X1[1024],Y1[1024],d[1024];
int a[1024][1024],w,h;
bool b[1024];
int calc(int a,int b) {
	if(X0[a]>X0[b])swap(a,b);
	if(X1[a]>=X0[b]){
		if(Y0[a]>Y1[b])
			return Y0[a]-Y1[b]-1;
		else return Y0[b]-Y1[a]-1;
	}else{
		if(Y0[a]>Y0[b])swap(a,b);
		if(Y1[a]>=Y0[b]){
			if(X0[a]>X1[b])
				return X0[a]-X1[b]-1;
			else return X0[b]-X1[a]-1;
		}else{
			if(X0[a]>X0[b])swap(a,b);
			int x=X0[b]-X1[a]-1;
			if(Y0[a]>Y0[b])swap(a,b);
			int y=Y0[b]-Y1[a]-1;
			return max(x,y);
		}
	}
}
int sol(){
	int W,H,n;
	scanf("%d%d%d",&W,&H,&n);
	for(int i=1;i<=n;++i)
		scanf("%d%d%d%d",X0+i,Y0+i,X1+i,Y1+i);
	X0[0]=X1[0]=-1;
	Y0[0]=0;Y1[0]=H-1;
	X0[n+1]=X1[n+1]=W;
	Y0[n+1]=0;Y1[n+1]=H-1;
	n+=2;
	for(int i=0;i<n;++i)
		for(int j=0;j<i;++j)
			a[i][j]=a[j][i]=calc(i,j);
	fill(d,d+n,inf);
	fill(b,b+n,false);
	d[n-1]=0;
	for(int i=0;i<n;++i) {
		int k=-1;
		for(int j=0;j<n;++j)
		if(!b[j] &&(k==-1 || d[j]<d[k])) k = j;
		b[k]=1;
		if(k==0)break;
		for(int j=0;j<n;++j)
		if(!b[j])d[j]=min(d[j],d[k]+a[k][j]);
	}
	return d[0];
}
int main(){
	int T;
	cin >> T;
	for(int i=1;i<=T;++i)
		cout << "Case #"<<i <<": " << sol() << endl;
}
