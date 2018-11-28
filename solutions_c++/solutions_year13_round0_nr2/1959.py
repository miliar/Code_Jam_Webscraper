#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cctype>
#include<cstdio>
using namespace std;
int arr[100][100];
int n,m; 
int main(){
	int cases,num; 
	scanf("%d",&cases);
	bool flag;
	for(int t = 1; t<= cases;t++){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&(arr[i][j]));
		flag = true;
		for (int i=0;i<n && flag;i++) {
			for (int j=0;j<m && flag;j++) {
				flag = true;
				num = arr[i][j];
				for(int k=0;k<n;k++){
					if(arr[k][j] > num){flag = false;break;}
				}
				if(flag)continue;
				flag = true;
				for(int k=0;k<m;k++){
					if(arr[i][k] > num){flag = false;break;}
				}
			}
		}
		printf("Case #%d: ",t);
		if(flag)printf("YES\n");
		else printf("NO\n");
	}
} 
