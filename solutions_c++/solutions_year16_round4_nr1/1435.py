#include<bits/stdc++.h>
#define maxn 50007
using namespace std;
typedef long long LL;
int nn,n;
string st[3]={"P","R","S"};
string res="";
bool isfound=false;
int dem[3],md[3];
int a[maxn];
int dd=0;
void openFile(){
	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
}
int duel(int x,int y){
	if(x!=2 && y!=2) return min(x,y);
	if(x!=0 && y!=0) return 1;
	return 2;
}
string build(int i,int x,int left,int right){
	int mid=(left+right)/2;
	string r1,r2;
	if(left==right){
		a[left]=x;
		return st[x];
	}
	if(x==0){
		r1=build(i+1,0,left,mid);
		r2=build(i+1,1,mid+1,right);
		if(r1>r2) return r2+r1;
		return r1+r2;
	}
	if(x==1){
		r1=build(i+1,1,left,mid);
		r2=build(i+1,2,mid+1,right);
		if(r1>r2) return r2+r1;
		return r1+r2;
	}
	if(x==2){
		r1=build(i+1,0,left,mid);
		r2=build(i+1,2,mid+1,right);
		if(r1>r2) return r2+r1;
		return r1+r2;
	}
}
void solve(){
	cin>>n>>md[1]>>md[0]>>md[2];//PRS
	nn=(int)pow(2,n);
	isfound=false;
	res="";
	////////////////////
	int tt=0;
	while(tt<3){
		for(int i=0;i<3;i++)dem[i]=0;
		string rr=build(0,tt,1,nn);
		for(int i=1;i<=nn;i++)dem[a[i]]++;
		isfound=true;
		for(int i=0;i<3;i++)
		if(dem[i]>md[i]){
			isfound=false;
		}
		tt++;
		if(isfound){
			if(res==""){
				res=rr;
			}else{
				if(res>rr) res=rr;
			}
		}
	}
	if(res!=""){
		cout<<res<<endl;
		return;
	}
	///////////////////
	cout<<"IMPOSSIBLE"<<endl;
}
int main(){
	openFile();
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++) {
		cout<<"Case #"<<tt<<": ";
		solve();	
	}
	return 0;
}
