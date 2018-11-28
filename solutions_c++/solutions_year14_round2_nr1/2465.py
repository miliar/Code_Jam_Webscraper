#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main(){
	int t, n, cases, i, j, cont;
	char str1[110], str2[110];

	scanf("%d", &t);

	for(cases = 1; cases <= t; cases++){
		scanf("%d", &n);

		scanf("%s", str1);
		scanf("%s", str2);

		int a = strlen(str1);
		int b = strlen(str2);
		int index1 = 0, index2 = 0;
		cont = 0;
		while(1){
			if(str1[index1] == '\0' && str2[index2] == '\0'){
				printf("Case #%d: %d\n", cases, cont);
				break;
			}

			int c1 = 0, c2 = 0;

			char aux = str1[index1];
			if(str1[index1] == str2[index2]){
				while(str1[index1] == aux){
					c1++;					
					index1++;
				}while(str2[index2] == aux){
					index2++;
					c2++;				
				}

				if((c1 > 1 || c2 > 1) && c1 != c2)
				cont += abs(c1 - c2);
			}else {
				printf("Case #%d: Fegla Won\n", cases);
				break;
			}
		}
	}
}
