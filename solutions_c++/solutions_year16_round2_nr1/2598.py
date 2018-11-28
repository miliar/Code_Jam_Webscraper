#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#define NUMBER 26
using namespace std;
int main(){
	int Case,len;
	char str[2003];
	
	freopen("A-large.in","r",stdin);
	freopen("p1-small.out","w",stdout);
	int nine[10];
	int visit[NUMBER];
	scanf("%d",&Case);
	for(int i=0;i<Case;i++){
		memset(visit, 0, sizeof(visit));
		memset(nine, 0, sizeof(nine));
		scanf("%2003s",&str);
		len=strlen(str);
		for(int j=0;j<len;j++){
			visit[(int)str[j]-'A']++;
		}
		while(visit[25]>0){
			visit[25]--;
			visit['O'-'A']--;
			visit['E'-'A']--;
			visit['R'-'A']--;
			nine[0]++;
		}
		
		while(visit['T'-'A']>0&&visit['W'-'A']>0&&visit['O'-'A']>0){
			visit['O'-'A']--;
			visit['W'-'A']--;
			visit['T'-'A']--;
			nine[2]++;
		}
		
		while(visit['R'-'A']>0&&visit['F'-'A']>0&&visit['U'-'A']>0&&visit['O'-'A']>0){
			visit['O'-'A']--;
			visit['U'-'A']--;
			visit['F'-'A']--;
			visit['R'-'A']--;
			nine[4]++;
		}
		
		while(visit['S'-'A']>0&&visit['I'-'A']>0&&visit['X'-'A']>0){
			visit['S'-'A']--;
			visit['I'-'A']--;
			visit['X'-'A']--;
			nine[6]++;
		}
		
		while(visit['I'-'A']>0&&visit['G'-'A']>0&&visit['E'-'A']>0&&visit['T'-'A']>0&&visit['H'-'A']>0){
			visit['I'-'A']--;
			visit['E'-'A']--;
			visit['G'-'A']--;
			visit['H'-'A']--;
			visit['T'-'A']--;
			nine[8]++;
		}
		while(visit['F'-'A']>0&&visit['I'-'A']>0&&visit['V'-'A']>0&&visit['E'-'A']>0){
			visit['F'-'A']--;
			visit['E'-'A']--;
			visit['I'-'A']--;
			visit['V'-'A']--;
			nine[5]++;
		}
		while(visit['S'-'A']>0&&visit['N'-'A']>0&&visit['E'-'A']>0&&visit['V'-'A']){
			visit['S'-'A']--;
			visit['E'-'A']=visit['E'-'A']-2;
			visit['N'-'A']--;
			visit['V'-'A']--;
			nine[7]++;
		}
		while(visit['I'-'A']>0&&visit['N'-'A']>0&&visit['E'-'A']>0){
			visit['I'-'A']--;
			visit['E'-'A']--;
			visit['N'-'A']=visit['N'-'A']-2;
			nine[9]++;
		}
		while(visit['T'-'A']>0&&visit['H'-'A']>0&&visit['R'-'A']>0&&visit['E'-'A']>0){
			visit['T'-'A']--;
			visit['E'-'A']=visit['E'-'A']-2;
			visit['H'-'A']--;
			visit['R'-'A']--;
			nine[3]++;
		}
		while(visit['O'-'A']>0&&visit['N'-'A']>0&&visit['E'-'A']>0){
			visit['O'-'A']--;
			visit['E'-'A']--;
			visit['N'-'A']--;
			nine[1]++;
		}
		
		printf("Case #%d: ",i+1);
		for(int k=0;k<10;k++){
			while(nine[k]>0){
				printf("%d",k);
				nine[k]--;
			}
		}
		printf("\n");
	}
	return 0;
}
