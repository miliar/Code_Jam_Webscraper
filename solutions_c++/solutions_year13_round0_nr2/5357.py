#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int t;
int n,m;
int mp[110][110];

struct x{
	int tp;
	int v;
	int w;
};

x z[310];
int zn;

bool cmp(const x&a,const x&b){
	return a.w<b.w;
}

int main(){
	int h,i,j,k;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d",&mp[i][j]);
		zn=0;
		for(i=0;i<n;i++){
			k=-1;
			for(j=0;j<m;j++){
				if(k<mp[i][j])k=mp[i][j];
			}
			z[zn].tp=0;
			z[zn].v=i;
			z[zn].w=k;
			zn++;
		}
		for(i=0;i<m;i++){
			k=-1;
			for(j=0;j<n;j++){
				if(k<mp[j][i])k=mp[j][i];
				z[zn].tp=1;
				z[zn].v=i;
				z[zn].w=k;
				zn++;
			}
		}
		sort(z,z+zn,cmp);
		for(i=0;i<zn;i++){
			k=z[i].v;
			if(z[i].tp==0){
				for(j=0;j<m;j++)
					if(mp[k][j]!=z[i].w && mp[k][j]!=0)break;
				if(j<m)continue;
				for(j=0;j<m;j++)
					mp[k][j]=0;
			}else{
				for(j=0;j<n;j++)
					if(mp[j][k]!=z[i].w && mp[j][k]!=0)break;
				if(j<n)continue;
				for(j=0;j<n;j++)
					mp[j][k]=0;
			}
		}
		bool ab=1;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(mp[i][j]!=0)ab=0;
		printf("Case #%d: ",h);
		printf(ab?"YES\n":"NO\n");
	}
	return 0;
}
