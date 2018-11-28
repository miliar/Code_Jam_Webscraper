#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
string str[205][2005];
string str1[204];
int n;
map<string,int> s;
map<string,int> s0;
int num[205];
int make(int x,int ty){
	int ret=0;
	for (int i=0;i<num[x];i++){
		int ty0=s0[str[x][i]];
		int ty1=s[str[x][i]];
		//cout<<tmp<<' '<<tynow<<' '<<ty<<endl;
		if(ty0==0){
			if(ty1==0) s[str[x][i]]=ty;
			if(ty1+ty==3) {ret++;s[str[x][i]]=-1;}
		}
		else {
			if(ty1!=0&&ty1!=ty0) {ret++;s[str[x][i]]=-1;}
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
		int have=0;
		s0.clear();
		have+=make1(0,1);
		have+=make1(1,2);
		int ans=200000;
		for (int i=0;i<(1<<(n-2));i++){
			//cout<<"case: "<<i<<endl;
			int ret=0;
			s.clear();
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
