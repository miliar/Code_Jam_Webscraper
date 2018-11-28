#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int main(){
	freopen("A-small-attempt1.in","r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int casenum = 0;casenum < t;++casenum){
		int a = 0;
		int r;
		scanf("%d",&r);
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++){
				int tmp;
				scanf("%d",&tmp);
				if (i+1 == r){
					
					
					a = a|(1<<tmp);
				}
			}
		scanf("%d",&r);
		int count = 0;
		int ans = 0;
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++){
				int tmp;
				scanf("%d",&tmp);
				if (i+1 == r){
					
					if (a & (1<<tmp)){
						count++;
						ans = tmp;
					}
				}
			}
		printf("Case #%d: ",casenum+1);
		if (count == 0){
			cout <<"Volunteer cheated!\n";
		}else if (count == 1){
			cout <<ans<<endl;
		}else{
			cout <<"Bad magician!"<<endl;
		}
	}
	return 0;
}