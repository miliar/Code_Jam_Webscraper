#include<stdio.h>
#include<stdlib.h>
typedef struct node{
	int val;
	node *next;
}node;
int main(void)
{
	int T, N, arr[1000], score1, score2;
	double tmp;
	FILE *fp, *fp2;
	node *naomi = (node*)malloc(sizeof(node)), *kenzi = (node*)malloc(sizeof(node)), *tnode, *wnode;
	naomi->next = NULL;
	kenzi->next = NULL;
	fp = fopen("D-small-attempt0.in", "rt");
	fp2 = fopen("output.txt", "wt");
	fscanf(fp, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fp, "%d", &N);
		for (int j = 0; j < 1000; j++)
			arr[j] = 0;
		for (int j = 0; j < N; j++)
		{
			fscanf(fp, "%lf", &tmp);
			arr[(int)(tmp * 1000)]=1;
		}
		wnode = naomi;
		for (int j = 0; j < 1000; j++)
		{
			if (arr[j] == 1)
			{
				tnode = (node*)malloc(sizeof(node));
				tnode->val = j;
				tnode->next = NULL;
				wnode->next = tnode;
				wnode = wnode->next;
			}
		}
		for (int j = 0; j < 1000; j++)
			arr[j] = 0;
		for (int j = 0; j < N; j++)
		{
			fscanf(fp, "%lf", &tmp);
			arr[(int)(tmp * 1000)] = 1;
		}
		wnode = kenzi;
		for (int j = 0; j < 1000; j++)
		{
			if (arr[j] == 1)
			{
				tnode = (node*)malloc(sizeof(node));
				tnode->val = j;
				tnode->next = NULL;
				wnode->next = tnode;
				wnode = wnode->next;
			}
		}
		tnode = naomi->next;
		wnode = kenzi->next;
		score1 = 0;
		while (wnode != NULL && tnode != NULL)
		{
			while (tnode != NULL && tnode->val < wnode->val)
				tnode = tnode->next;
			if (tnode != NULL && tnode->val > wnode->val)
			{
				score1++;
				tnode = tnode->next;
			}
			wnode = wnode->next;
		}
		wnode = naomi->next;
		tnode = kenzi->next;
		score2 = 0;
		while (wnode != NULL && tnode != NULL)
		{
			while (tnode != NULL && tnode->val < wnode->val)
				tnode = tnode->next;
			if (tnode != NULL && tnode->val > wnode->val)
			{
				score2++;
				tnode = tnode->next;
			}
			wnode = wnode->next;
		}
		fprintf(fp2, "Case #%d: %d %d\n", i + 1, score1, N-score2);
	}
	fclose(fp);
	fclose(fp2);

	return 0;
}