#include <cstdio>
#include <algorithm>

using namespace std;
double massN[1001], massK[1001];
bool n[1001], k[1001];

int main(){
	int T, mNum, retW, retDw;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		scanf("%d", &mNum);
		for(int j = 0; j != mNum; j++)
			scanf("%lf", &massN[j]);
		for(int j = 0; j != mNum; j++)
			scanf("%lf", &massK[j]);
		sort(massN, massN+mNum);
		sort(massK, massK+ mNum);
		retW = 0;
		for(int j = 0,k = 0; j != mNum; j++){
			while(k< mNum && massK[k] < massN[j]){
				k++;
			}
			if(k == mNum)
				break;
			else{
				k++;
				retW++;
			}
		}
		retW = mNum - retW;
		retDw = 0;
		for(int j = mNum -1 ,k = mNum -1, pre = 0; j >= pre && k>=0 ; j--){
			if(massN[j] > massK[k]){
				retDw++;
				k--;
				continue;
			}
			while( pre <= j && massN[j] < massK[k] && k >=0){
				pre++;
				k--;
			}
			if(pre <= j && k >=0){
				retDw++;
				k--;}
		}
		printf("Case #%d: %d %d\n", i, retDw, retW);			
	}
	return 0;
}

