//Karol Rozycki B
#include<cstdio>
#include<algorithm>
#define MAX 110
using namespace std;

int z,n,m;
int IN[MAX][MAX];

bool check(int a, int b){
	bool first=true;
	for(int j=0;j<m;j++){
		if(IN[a][j]>IN[a][b]){
			first=false;
			break;
		}
	}
	bool second=true;
	for(int i=0;i<n;i++){
		if(IN[i][b]>IN[a][b]){
			second=false;
			break;
		}
	}
	return (first || second);
}

int main(){
	scanf("%i",&z);
	for(int g=1;g<=z;g++){
		scanf("%i %i",&n,&m);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%i",&IN[i][j]);
			}
		}
		bool spr=1;
		for(int i=0;i<n;i++){
			if(!spr){
				break;
			}
			for(int j=0;j<m;j++){
				spr=check(i,j);
				if(!spr){
					break;
				}
			}
		}
		printf("Case #%i: ",g);
		if(spr){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
	return 0;
}

