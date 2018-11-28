#include<cstdio>
#include<cstring>

char s[1001];

int indexx[1001];
int last = 0;
int first = 0;
int temp = 0;

int main(){	
	int t;
	scanf("%d", &t);
	int k = 1;
	while(t--){
		printf("Case #%d: ", k);
		first = -1;
		last = 0;
		temp = 0;
		for(int i=0;i<1000;i++){
			indexx[i] = 0;
		}
		scanf("%s", s);
		int l = strlen(s);
		for(int i=0;i<l;i++){
			if(i == 0){
				indexx[i] = 0;
				last++;
			}
			else if(s[i] < s[temp]){
				indexx[i] = last++;
			}
			else{
				indexx[i] = first--;
				temp = i;
			}
		}
		for(int i=0;i<l;i++){
			int b = 0;
			for(int j=0;j<l;j++){
				if(indexx[j] < indexx[b]){
					b = j;
				}
			}	
			printf("%c", s[b]);
			indexx[b] = 1000000000;
		}
		printf("\n");
		k++;
	}	
}