#include <iostream>
#include <vector>

using namespace std;

void degenerate(char *original, char *degen) {
	char tmp = 'A';
	int offset = 0;
	for (int i=0;i<=100;i++) {
		if (original[i]=='\0')
			break;
		else {
			if (i==0) {
				tmp = original[i];
				degen[offset] = tmp;
				offset++;
			} else {
				if (original[i]!=tmp) {
					tmp = original[i];
					degen[offset] = tmp;
					offset++;
				}
			}
			//tmp = original[i];
		}
	}
}

int degenerate1(char *val1, char *val2,char *degen) {
	int step = 0;

	int offset1 = 0;
	int offset2 = 0;

	for (int i=0;i<=100;i++) {
		if (degen[i]=='\0')
			return step;
		else {
			int flag1=0;
			for (int j=offset1;j<=100;j++) {
				if (val1[j]==degen[i]) {
					flag1++;
					offset1++;
				} else {
					break;
				}
			}

			int flag2=0;
			for (int j=offset2;j<=100;j++) {
				if (val2[j]==degen[i]) {
					flag2++;
					offset2++;
				} else {
					break;
				}
			}

			int val = (flag1>flag2)?(flag1-flag2):(flag2-flag1);
			step = step + val;
		}
	}

	return step;
}

int main() {
	FILE *fp = fopen("A-small-attempt5.in","r");
	//FILE *fp = fopen("test.txt","r");
	int T = 0;
	fscanf(fp, "%d", &T);
	//fread(&T,sizeof(int),1,fp);
	for (int i=1;i<=T;i++) {
		//int first,second,tmp;
		//int row1[4],row2[4];
		printf("Case #%d: ",i);
		//int N,L;
		int n;
		fscanf(fp, "%d", &n);
		//fscanf(fp, "%d %d", &N,&L);

		char str[100][101] = {'\0'};
		fgets (str[0] , 120 , fp);
		for (int j=0;j<n;j++) {
			//fscanf(fp, "%1d", &str[j][y]);
			fgets (str[j] , 120 , fp);
		}
		
		int poss = -1;

		//first assume n=2
		char degen[100][101] ={'\0'};
		degenerate(str[0],degen[0]);
		degenerate(str[1],degen[1]);
		if (strcmp (degen[0],degen[1])==0) {
			poss = degenerate1(str[0],str[1],degen[0]);
		}
		//end assume n=2

		if (poss<0)
			printf("Fegla Won");
		else
			printf("%d",poss);

		if (i!=T)
			printf("\n");
	}
	
	return 0;
}