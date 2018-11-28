#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
using namespace std;
typedef pair<int,int> ii;
int main(){
	int T;	
	cin>>T;
	for(int cas = 1; cas<=T; ++cas){
		int N;
		cin>>N;
		char str[200][200];
		char str2[200][200];
		int count[200][200];
		for(int i=0; i<N; ++i){
			scanf("%s", str[i]);
		}
		int found = 1;
		int ans=0;
		for(int i=0; i<N; ++i){
			int cnt=0;
			for(int j=0; j<strlen(str[i]); ++j){
				if(cnt==0){
					count[i][cnt] = 1;
					str2[i][cnt++]=str[i][j];
				}
				else if(str[i][j]!=str2[i][cnt-1]){
					count[i][cnt]=1;
					str2[i][cnt++]=str[i][j];
				}
				else{
					count[i][cnt-1]++;
				}
			}
			str2[i][cnt]='\0';
			//cout<<str2[i]<<endl;
			if(i!=0 && strcmp(str2[i], str2[i-1])!=0) found = 0;
		}
		//cout<<found<<endl;
		
		if(found){
			for(int i =0; i<strlen(str2[0]); ++i){
				double repeat = 0;
				for(int j=0; j<N; ++j){
					repeat+=count[j][i];
				}
				repeat/=N;
				repeat+=0.5;
				for(int j=0; j<N; ++j){
					ans+=abs(count[j][i]-(int)repeat);
				}
			}
			printf("Case #%d: %d\n", cas, ans);
		}
		else printf("Case #%d: Fegla Won\n", cas);

	}	
	return 0;
}
