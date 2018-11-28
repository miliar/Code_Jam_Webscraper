#include<cstdio>
#include<cstring>

using namespace std;

bool chk[20];

FILE *fp = fopen("input.txt", "r");
FILE *fp2 = fopen("o.txt", "r");


int main(){
	int t;
	fscanf(fp, "%d", &t);
	int index=1;
	while (t--) {
		memset(chk, false, sizeof(chk));
		int f;
		fscanf(fp, "%d", &f);
		
		int a;
		for (int i=1; i<=4; i++) {
			for (int j=0; j<4; j++) {
				fscanf(fp, "%d", &a);
				if (i==f) {
					chk[a]=true;
				}
			}
		}
		int cnt=0;
		int num,s;
		fscanf(fp, "%d", &s);
		for (int i=1; i<=4; i++) {
			for (int j=0; j<4;j++) {
				fscanf(fp, "%d", &a);
				if (i==s && chk[a]==true){
					cnt++;
					num=a;
				}
			}
		}
		printf("Case #%d: ", index);index++;
		if (cnt==1) {
			printf("%d\n", num);
		}
		else if(cnt==0){
			printf("Volunteer cheated!\n");
		}
		else {
			printf("Bad magician!\n");
		}

	}
	
	
	return 0;
}