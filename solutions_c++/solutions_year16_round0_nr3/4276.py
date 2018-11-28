#include <iostream>
#include <cstdio>
#include <cstring>
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int n,m;
vector<int> ans,v;

int prime(LL x){
	for (int i=2;(LL)i*i<=x;i++)
		if (x%i==0) return i;
	return 1;
}

int main(){
	int T;
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&m);
		ans.clear();
		for (int i=(1<<n-1)+1;i<(1<<n);i++){
			if (i&1){
				int bo=1;
				int p=i;
				v.clear();
				while (p){
					v.push_back(p%2);
					p/=2;
				}
				for (int j=2;j<=10;j++){
					LL z=0;
					LL zz=1;
					for (int q=0;q<v.size();q++){
						if (v[q]) z+=zz;
						zz*=j;
					}
					int ff = prime(z);
					if (ff==1){bo=0;break;}
				}
				if (bo) ans.push_back(i);
			}
			if (ans.size()==m) break;
		}
		cout <<"Case #"<< ti<<":"<<endl;
		for (int i=0;i<m;i++){
			int p=ans[i];
			v.clear();
			while (p){
				v.push_back(p%2);
				p/=2;
			}
			for (int j=v.size()-1;j>=0;j--) printf("%d",v[j]);
			for (int j=2;j<=10;j++){
				LL z=0;
				LL zz=1;
				for (int q=0;q<v.size();q++){
					if (v[q]) z+=zz;
					zz*=j;
				}
				int ff = prime(z);
				printf(" %d",ff);
			}
			printf("\n");
		}
		
	}
	return 0;
}
