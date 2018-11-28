#include<stdio.h>
#include<string.h>
#include<map>
#include<string>
#include<iostream>
using namespace std;
map<string,int> h[10];
string str[10];
int a[10];
int n,m;
int ans,sum;
void getans(){
	string s;
	int i,w,j,ss=0;
	for (i=0;i<n;i++) h[i].clear();
	for (i=0;i<m;i++){
		w=a[i];
		s="";
		if (!h[w][s]) {h[w][s]=1;ss++;}
		for (j=0;j<str[i].size();j++){
			s=s+str[i][j];
			if (!h[w][s]) {h[w][s]=1;ss++;}
		}
	}
	if (ss>ans) {ans=ss;sum=1;}
	else if (ss==ans) sum++;
}		
void dfs(int w){
	int i;
	if (w==m){
		getans();
		return;
	}
	for (i=0;i<n;i++){
		a[w]=i;
		dfs(w+1);
	}
}
int main(){
	freopen("d.in","r",stdin);	
	freopen("d.out","w",stdout);
	int i,ca,cc=0;
	scanf("%d",&ca);
	while (ca--){
		scanf("%d%d",&m,&n);
		for (i=0;i<m;i++) cin>>str[i];
		ans=0;
		sum=0;
		dfs(0);
		printf("Case #%d: %d %d\n",++cc,ans,sum);
	}
	return 0;
}
