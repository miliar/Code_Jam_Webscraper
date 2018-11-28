#include <bits/stdc++.h>

using namespace std;

int n,r,p,s;
string mem[4][15];

string rec(char c,int n){
	if (n==0) return string(1,c);
	if (mem[c-'P'][n]!="") return mem[c-'P'][n];
	string &res=mem[c-'P'][n];
	if (c=='P'){
		string a=rec('P',n-1);
		string b=rec('R',n-1);
		if (a<b) return res=a+b;
		return res=b+a;
	}
	if (c=='R'){
		string a=rec('R',n-1);
		string b=rec('S',n-1);
		if (a<b) return res=a+b;
		return res=b+a;
	}
	if (c=='S'){
		string a=rec('P',n-1);
		string b=rec('S',n-1);
		if (a<b) return res=a+b;
		return res=b+a;
	}
	return res;
}

int main(){
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t){
		printf("Case #%d: ",t);
		scanf("%d%d%d%d",&n,&r,&p,&s);
		string res="";
		for(int w=0;w<4;++w){
			if (w==1) continue;
			string v(1,'P'+w);
			for(int i=0;i<n;++i){
				string v2;
				for(char c:v){
					if (c=='P'){
						v2.push_back('P');
						v2.push_back('R');
					}
					if (c=='R'){
						v2.push_back('R');
						v2.push_back('S');
					}
					if (c=='S'){
						v2.push_back('P');
						v2.push_back('S');
					}
				}
				v=v2;
			}
			int cnt[3];
			memset(cnt,0,sizeof(cnt));
			for(char c:v){
				int x=c-'P';
				if (x) --x;
				cnt[x]++;
			}
			if (p==cnt[0]&&r==cnt[1]&&s==cnt[2]){
				for(int i=0;i<n;++i){
					for(int j=0;j<4;++j){
						mem[j][i]="";
					}
				}
				v=rec('P'+w,n);
				if (res==""||v<res) res=v;
			}
		}
		if (res=="") res="IMPOSSIBLE";
		puts(res.c_str());
	}
	return 0;
}
