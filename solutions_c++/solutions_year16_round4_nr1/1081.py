#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string rec(int n,int w){
	if(n==0){
		if(w==0)
			return "P";
		if(w==1)
			return "R";
		if(w==2)
			return "S";
	}
	string u=rec(n-1,w);
	string v=rec(n-1,(w+1)%3);
	if(u>v)
		return v+u;
	else
		return u+v;
}
int main(){
	int TT;
	cin>>TT;
	int ans=0;
	int n,r,p,s;
	int a[3];
	int b[3];
	int c[100000];
	int d[100000];
	for(int T=1;T<=TT;++T){
		cin>>n>>r>>p>>s;
		int w;
		int w2=-1;
		for(int w=0;w<3;++w){
			a[0]=0;
			a[1]=0;
			a[2]=0;
			a[w]=1;
			for(int i=1;i<=n;++i){
				b[0]=a[0];
				b[1]=a[1];
				b[2]=a[2];
				a[0]=b[0]+b[2];
				a[1]=b[0]+b[1];
				a[2]=b[1]+b[2];
			}
			//cout<<a[0]<<" "<<a[1]<<" "<<a[2]<<endl;
			if(a[0]==p&&a[1]==r&&a[2]==s){
				w2=w;
			}
		}
		string ans;
		if(w2<0){
			ans="IMPOSSIBLE";
		}
		else{
			//cout<<w2<<endl;
			ans=rec(n,w2);
			//w=w2;
			//c[0]=w;
			//for(int i=1;i<=n;++i){
			//	for(int j=0;j<(1<<(n-1));++j){
			//		int u=c[j];
			//		int v=(c[j]+1)%3;
			//		if(u>v){
			//			int tmp=u;
			//			u=v;
			//			v=tmp;
			//		}
			//		d[2*j]=u;
			//		d[2*j+1]=v;
			//	}
			//	for(int j=0;j<(1<<n);++j){
			//		c[j]=d[j];
			//	}
			//}
			//for(int j=0;j<(1<<n);++j){
			//	if(c[j]==0)
			//		ans+="P";
			//	else if(c[j]==1)
			//		ans+="R";
			//	else if(c[j]==2)
			//		ans+="S";
			//}
		}

		cout<<"Case #"<<T<<": "<<ans<<"\n";
	}
	return 0;
}

