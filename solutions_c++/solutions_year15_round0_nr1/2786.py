#include <cstdio>
#include <vector>

using namespace std;

bool check(vector<int>& shy){
	int clapping=0;
	for(int i=0;i<shy.size();i++){
		if(clapping<i){return false;}
		clapping+=shy[i];
	}
	return true;
}

char buff[10009];

int main(){
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		int smax;
		scanf("%d",&smax);
		scanf("%s",buff);
		vector<int>shy;
		for(int j=0;j<=smax;j++){
			shy.push_back(buff[j]-'0');
		}
		int k=0;
		while(true){
			if(check(shy)){
				printf("Case #%d: %d\n",tc,k);
				break;
			}
			k++;
			shy[0]++;
		}
	}
}
