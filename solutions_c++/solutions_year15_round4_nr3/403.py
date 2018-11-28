#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
string str[205][2005];
string str1[204];
int t0[205][2005];
int t1[205][2005];
int shu[205][2005];
int sss[400];
int n;
map<string,int> s;
map<string,int> s0;
map<string,int>ss;
int num[205];
int make(int x,int ty){
	int ret=0;
	for (int i=0;i<num[x];i++){
		int ty0=t0[x][i];
		int ty1=sss[shu[x][i]];
		if(ty0==-1||ty1==-1) continue;
		if(ty0==0){
			if(ty1==0) sss[shu[x][i]]=ty;
			if(ty1+ty==3) {ret++;sss[shu[x][i]]=-1;}
		}
		else {
			if(ty1!=0&&ty1!=ty0) {ret++;sss[shu[x][i]]=-1;}
			if(ty!=ty0) {ret++;sss[shu[x][i]]=-1;}
		}
	}
	return ret;
}
int make1(int x,int ty){
	int ret=0;
	for (int i=0;i<num[x];i++){
		int tynow=s0[str[x][i]];
		//cout<<tmp<<' '<<tynow<<' '<<ty<<endl;
		if(tynow==0) s0[str[x][i]]=ty;
		if(tynow+ty==3) {ret++;s0[str[x][i]]=-1;}
	}
	return ret;
}
//char ch;
int main(){
	int T,ca=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		getchar();
		for (int i=0;i<n;i++){
			getline(cin,str1[i]);
			int l=str1[i].length();
			int j=0;
			int now=0;
			while(now<l){
				str[i][j]="";
				while(now<l&&str1[i][now]==' ') now++;
				if(now>=l) break;
				while(now<l&&str1[i][now]!=' '){
					str[i][j].append(1,str1[i][now]);
					now++;
				}
				j++;
			}
			num[i]=j;
		}
		ss.clear();
		int nownum=0;
		for (int i=2;i<n;i++){
			for (int j=0;j<num[i];j++){
				if(ss[str[i][j]]==0) ss[str[i][j]]=++nownum;
			}
		}
		for (int i=2;i<n;i++){
			for (int j=0;j<=num[i];j++){
				shu[i][j]=ss[str[i][j]];
			}
		}
		int have=0;
		s0.clear();
		have+=make1(0,1);
		have+=make1(1,2);
		for (int i=2;i<n;i++){
			for (int j=0;j<num[i];j++){
				t0[i][j]=s0[str[i][j]];
				//cout<<i<<' '<<j<<' '<<t0[i][j]<<' '<<str[i][j]<<endl;
			}
		}
		int ans=200000;
		for (int i=0;i<(1<<(n-2));i++){
			//cout<<"case: "<<i<<endl;
			int ret=0;
			memset(sss,0,sizeof(sss));
			int x=i;
			for (int j=2;j<n;j++){
				ret+=make(j,x%2+1);
				x/=2;
			}
			ans=min(ret+have,ans);
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
