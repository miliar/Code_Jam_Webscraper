#include <cstdio>
#include <cstdlib>
#include <cstring>
int num;
int num1;
int num2;
int main(){
	int numcount = 0;
	scanf("%d", &num);
	for(int i = 0; i< num; i++){
		numcount = 0;
		scanf("%d", &num1);
		scanf("%d", &num2);
		for(int i = num1; i <= num2; i++){
			char buffer[10];
			itoa(i, buffer, 10);
			int length = strlen(buffer);
			int key = 1;
			for(int a = 0; a<length/2 && key == 1; a++){
				if(buffer[a]!= buffer[length-1-a]){
					key = 0;
				}
			}
			if(key == 1){
				int key2 = 0;
				for(int j = 1; j <= i && key2 == 0; j++){
					if(j*j == i){
						char buffer[10];
						itoa(j, buffer, 10);
						int length = strlen(buffer);
						int key = 1;
						for(int a = 0; a<length/2 && key == 1; a++){
							if(buffer[a]!= buffer[length-1-a]){
								key = 0;
							}
						}
						if(key == 1){
							key2 = 1;
						}
					}
				}
				if(key2 == 1){
					numcount ++;
				}
			}
		}
		printf("Case #%d: ", i + 1);
		printf("%d",numcount);
		printf("\n");
	}
	//scanf("%d", &num);
}