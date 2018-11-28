#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int l1,l2;
long long ans,ans_n1,ans_n2;

char s1[100],s2[100];

void dfs2(int d){
	if (d>l2){
		int n1,n2;
		sscanf(s1,"%d",&n1);
		sscanf(s2,"%d",&n2);
		if (abs(n1-n2)<ans || ans==-1){
			ans=abs(n1-n2);
			ans_n1=n1;
			ans_n2=n2;
		}
		else if (abs(n1-n2)==ans && n1<=ans_n1){
			if (n1<ans_n1){
				ans_n1=n1;
				ans_n2=n2;
			}
			else{
				if (n2<ans_n2)
					ans_n2=n2;
			}
		}
		return;
	}
	if (s2[d]=='?'){
		for (int j=0;j<=9;j++){
			s2[d]=j+'0';
			//cerr<<"kkkkkk"<<endl;
			dfs2(d+1);
		}
		s2[d]='?';
	}
	else dfs2(d+1);
}

void dfs1(int d){
	if (d>l1){
		dfs2(0);
		return;
	}
	//cerr<<"k "<<d<<endl;
	if (s1[d]=='?'){
		for (int j=0;j<=9;j++){
			s1[d]=j+'0';
			dfs1(d+1);
		}
		s1[d]='?';
	}
	else dfs1(d+1);
}

int main(){
	int tt;
	cin>>tt;

	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		scanf("%s%s",s1,s2);
		//cerr<<"s1 : "<<s1<<endl;
		l1=strlen(s1);
		l2=strlen(s2);
		ans=-1;
		dfs1(0);
		int i;
		long long u=1;
		for (i=1;i<=l1-1;i++) u*=10;
		while (u>ans_n1){
			u/=10;
			printf("0");
		}
		if (ans_n1>0) printf("%lld ",ans_n1);
		else printf(" ");
		u=1;
		for (i=1;i<=l2-1;i++) u*=10;
		while (u>ans_n2){
			u/=10;
			printf("0");
		}
		if (ans_n2>0) printf("%lld\n",ans_n2);
		else printf("\n");
	}

	return 0;
}