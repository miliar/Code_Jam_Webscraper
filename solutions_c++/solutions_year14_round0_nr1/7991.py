#include<cstdio>
#include<iostream>

#define NUM 4

void readRow(int c, int row[])
{
	int dummy;
    for(int i=1;i<=NUM;i++)
	{
		for(int j=0;j<NUM;j++)
		{
			if(c == i){
				scanf("%d ", &row[j]); 
			}
			else{
				scanf("%d ", &dummy);
			}
		}
	}
}

int getCommonElementsCount(int row1[], int row2[], int &elem)
{
	int count = 0;
	for(int i=0;i<NUM; i++)
	{
		for(int j=0;j<NUM;j++)
		{
			if(row1[i] == row2[j])
			{
				elem = row1[i];
				count++;
			}
		}
	}
	return count;
}

int main()
{
	int ntc;
	int row1[NUM], row2[NUM];
	int c1, c2;
	scanf("%d", &ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		scanf("%d", &c1);
		readRow(c1, row1);
		scanf("%d", &c2);
		readRow(c2, row2);
		int elem;
		int count = getCommonElementsCount(row1, row2, elem);
		if(count == 1){
			printf("Case #%d: %d\n", tc, elem);
		}else if(count > 1) {
			printf("Case #%d: Bad magician!\n", tc);
		} else {
			printf("Case #%d: Volunteer cheated!\n", tc);
		}
	}
}