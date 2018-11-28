#include <cstdio>
#include <vector>

using namespace std;
int arr1[5];
int arr2[5];

int main(){
	int T, first, sec;
	int cnt, ans,tmp;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		scanf("%d", &first);
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++){
				scanf("%d", &tmp);
				if( (j+ 1) == first)
					arr1[k] = tmp;
			}

		scanf("%d", &sec);
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++){
				scanf("%d", &tmp);
				if( (j+ 1) == sec)
					arr2[k] = tmp;
		}
		cnt = 0, ans = -1;
		for(int j = 0; j< 4; j++){
			for(int k = 0; k < 4; k++){
				if(arr1[j] == arr2[k]){
					cnt++;
					ans = arr1[j];
				}
			}
		}
		printf("Case #%d: ", i);
		if(cnt==1 && ans != -1)
			printf("%d\n", ans);
		else if (cnt > 1){
			printf("Bad magician!\n");
		}
		else 
			printf("Volunteer cheated!\n");
	}
}
