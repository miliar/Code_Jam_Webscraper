#include <iostream>

int main() {
	FILE *fp = fopen("A-small-attempt0.in","r");
	int T = 0;
	fscanf(fp, "%d", &T);
	//fread(&T,sizeof(int),1,fp);
	for (int i=1;i<=T;i++) {
		int first,second,tmp;
		int row1[4],row2[4];
		printf("Case #%d: ",i);
		
		fscanf(fp, "%d", &first);
		for (int x =1;x<=4;x++) {
			for (int y=0;y<4;y++) {
				if (x<=first)
					fscanf(fp, "%d", &row1[y]);
				else
					fscanf(fp, "%d", &tmp);
			}
		}

		fscanf(fp, "%d", &second);
		for (int x =1;x<=4;x++) {
			for (int y=0;y<4;y++) {
				if (x<=second)
					fscanf(fp, "%d", &row2[y]);
				else
					fscanf(fp, "%d", &tmp);
			}
		}

		int count = 0;
		int number = 0;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				if (row1[i]==row2[j]) {
					count++;
					number = row1[i];
				}
			}
			//printf("%d %d %d %d\n",row1[0],row1[1],row1[2],row1[3]);
			//printf("%d %d %d %d\n",row2[0],row2[1],row2[2],row2[3]);
		}
		if (count==0)
			printf("Volunteer cheated!");
		else if (count==1)
			printf("%d",number);
		else
			printf("Bad magician!");

		if (i!=T)
			printf("\n");
	}
	
	return 0;
}