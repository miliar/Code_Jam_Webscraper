#include <iostream>
#include <cstdio>

using namespace std;

int N;

int maxs;
char input[1024];
int array[1024];
int add;

void init(){
	maxs = 0;
	for(int i = 0;i < 1024;i++){
		array[i] = 0;
	}
	add = 0;
}

int main(){

	scanf("%d",&N);
	for(int n = 1;n <= N;n++){
		init();
		scanf("%d",&maxs);
		scanf("%s",input);
		//printf("%s\n",input);
		for(int i = 0;i <= maxs;i++){
			//printf("###%d\n",array[i]);
			if(array[i] + add < i){
				add += i - (array[i] + add);
			}
			array[i + 1] = array[i] + input[i] - 48;
		}
		printf("Case #%d: %d\n",n,add);
	}

	return 0;
}