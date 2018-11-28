#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main(int argc,char **argv)
{
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    int cnt,ans,mapn[20],arr[5]; 
	cin >> cnt;
	for(int i=1;i<=cnt;i++){
		int res_ans=0,ans_x;
		printf("Case #%d: ", i);
		for(int j=0;j<20;j++){
			mapn[j]=0;
		}
		cin >> ans_x;
		int a,b,c,d;
		for(int j=1;j<=4;j++){
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if(j==ans_x){
				mapn[a]+=1;mapn[b]+=1;
				mapn[c]+=1;mapn[d]+=1;
			}
		}
		cin >> ans_x;
		for(int j=1;j<=4;j++){
			scanf("%d %d %d %d",&a,&b,&c,&d);
			if(j==ans_x){
				res_ans=mapn[a]+mapn[b]+mapn[c]+mapn[d];
				mapn[a]+=1;mapn[b]+=1;
				mapn[c]+=1;mapn[d]+=1;
			}
		}
		if(res_ans==0){
			printf("Volunteer cheated!\n");	
		}
		else if(res_ans>1){
			printf("Bad magician!\n");	
		}
		else{
			for(int j=0;j<20;j++){
				if(mapn[j]==2){
					printf("%d\n",j);
				}
			}
		}
	}
} 
