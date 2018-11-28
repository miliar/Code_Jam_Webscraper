#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>

#define maxn 110

using namespace std;

int n,m,lon[maxn][maxn];

struct cell{
	int ii,jj,hh;
}temp;
vector<cell>v;

bool compare(cell a,cell b){
	return a.hh>b.hh;
}

bool size_dite(int x,int y,int d){
	for(int i=1;i<=n;i++)if(lon[i][y]>d)goto here;
	return true;
	here:;
	for(int j=1;j<=m;j++)if(lon[x][j]>d)return false;
	return true;
}

int main()
{
	freopen("sam.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,r=0;
	cin>>t;
	while(t--){
		cin>>n>>m;
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				temp.ii=i;
				temp.jj=j;
				cin>>temp.hh;
				lon[i][j]=temp.hh;
				v.push_back(temp);
			}
		}
		sort(v.begin(),v.end(),compare);
		k=v.size();
		i=0;
		while(i<k){
			temp=v[i];
			if(size_dite(v[i].ii,v[i].jj,v[i].hh)!=true){
				printf("Case #%d: NO\n",++r);
				goto there;
			}
			i++;
		}
		printf("Case #%d: YES\n",++r);
		there:;
		v.clear();
	}
	return 0;
}