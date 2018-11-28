#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <vector>

using namespace std;

int main() {
	
	int tt,n,v;
	double na[1000+10],ke[1000+10];
	cin>>tt;
	
	for(int t = 1;t<=tt;t++){
		printf("Case #%d: ",t);
		
		int vet1[4][4];
		int vet2[4][4];
		map<int,int> hash;
		int ans1,ans2,has2 = 0,isBad = 0,ans;
		cin>>ans1;
		for(int i = 0;i<4;i++) for(int j = 0;j<4;j++) cin>>vet1[i][j];
		cin>>ans2;
		for(int i = 0;i<4;i++) for(int j = 0;j<4;j++) cin>>vet2[i][j];
		for(int i = 0;i<4;i++) hash[vet1[ans1-1][i]]++;
		for(int i = 0;i<4;i++) hash[vet2[ans2-1][i]]++;
		for(map<int,int>::iterator it = hash.begin();it!=hash.end();it++){
			//cout<<it->first<< " " <<it->second<<endl;
			if(it->second == 2 && !has2){
				has2 = 1;
				ans = it->first;
			}else if(it->second == 2 && has2){
				isBad = 1;
				break;
			}
		}

		if(isBad){
			printf("Bad magician!\n");
		}else if(has2){
			printf("%d\n", ans);
		}else{
			printf("Volunteer cheated!\n");
		}
	}
	
	return 0;
}