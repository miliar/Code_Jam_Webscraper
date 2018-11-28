#include <stdio.h>
#include <string.h>
char arr[2][101];
int main(void){
	FILE *f;
	f=fopen("pb.txt","w+");
	int t;
	scanf("%d", &t);
//	scanf("%s", arr[0]);//enter
	for(int i=1;i<=t;i++){
		int cnt=0;
		scanf("%s", arr[0]);
		int ptr=0;
		int l=strlen(arr[0]);
		int k=0;
		while(true){
			ptr=-1;
			for(int j=0;j<l;j++){
				if(arr[k][j]=='-')
					ptr=j;//가장 뒤의 - 찾는 ptr
			}
			if(ptr==-1)
				break;
			if(arr[k][0]=='+'){
				for(int j=0;j<=ptr;j++){
						arr[!k][j]=arr[k][ptr-j];
				}
				for(int j=ptr+1;j<l;j++){
						arr[!k][j]=arr[k][j];
				}
			}
			else{
				for(int j=0;j<=ptr;j++){
					if(arr[k][ptr-j]=='+')
						arr[!k][j]='-';
					else if(arr[k][ptr-j]=='-')
						arr[!k][j]='+';
				}
				for(int j=ptr+1;j<l;j++){
						arr[!k][j]=arr[k][j];
				}
			}
			
			k= !k;
			cnt++;
		}
		fprintf(f,"Case #%d: %d\n", i,cnt);
	}
	fclose(f);
	return 0;
}