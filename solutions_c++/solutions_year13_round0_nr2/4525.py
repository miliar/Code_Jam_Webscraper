#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


struct node{
	int x,y;
	int h;
};

node arr[10005];

int mat[102][102];
int height[102][102];

bool cmp(const node& a, const node& b){
	return a.h<b.h;
}

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;

	cin>>T;

	for(int ca=1;ca<=T;ca++){
		memset(mat,0,sizeof(mat));
		int N,M;
		cin>>N>>M;
		int sz=0;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++){
				cin>>arr[sz].h;
				height[i][j]=arr[sz].h;
				arr[sz].x=i;
				arr[sz].y=j;
				sz++;
			}
		sort(arr,arr+sz,cmp);
		bool flag = true;
		for(int k=0;k<sz;k++)
			if(mat[arr[k].x][arr[k].y]==0){
				int v = arr[k].h;
				int i,j;
				//row
				for(j=0;j<M;j++)
					if(height[arr[k].x][j] > v) break;
				if(j==M){
					for(j=0;j<M;j++)
						mat[arr[k].x][j]=1;
					continue;
				}
				//col
				for(i=0;i<N;i++)
					if(height[i][arr[k].y] > v) break;
				if(i==N){
					for(i=0;i<N;i++)
						mat[i][arr[k].y] = 1;
					continue;
				}
				//
				flag = false;
				break;
			}
			if(flag) printf("Case #%d: YES\n",ca);
			else printf("Case #%d: NO\n",ca);
	}
}