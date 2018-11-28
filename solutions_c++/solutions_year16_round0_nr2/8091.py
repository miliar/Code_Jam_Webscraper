#include<stdio.h>
#include<string.h>
#define IN in

int main()
{
	int T;
	char set[500];
	char cur_set[500];
	char copy_set[500];
	char work_set[500];
	int i,j,k,p;
	int n;
	int cnt;

	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.out","w");
	fscanf(IN,"%d",&T);
	
	for(int t = 0; t < T; t++)
	{
		fscanf(IN, "%s",set);

		n = (int)strlen(set);
		strcpy(cur_set, set);
		cnt = 0;

		for(i = 0; i < n; i++)
		{
			for(p = n - 1; p >= 0; p--)
			{
				if(cur_set[p] == '-') break;
			}
			if(p < 0) break;
			//printf("P= %d\n",p);

			cnt++;
			int cnt_rear = -1;
			int cnt_front = -1;
			p++;
			for(j = 0; j < p; j++)
			{
				if(j == 1 && cur_set[0] != cur_set[1] && n > 2) j++;
				strcpy(work_set, cur_set);
				for(k = 0; k <= j; k++)
				{
					work_set[j - k] = (cur_set[k] == '-') ? '+' : '-';
				}

				int temp_rear = 0;
				for(k = n - 1; k >= 0; k--)
				{
					if(work_set[k] == '-') break;
					temp_rear++;
				}

				int temp_front = 0;
				for(k = 0; k < n; k++)
				{
					if(work_set[k] == '+') break;
					temp_front++;
				}

				//printf("Work_SET : %s\n",work_set);

				if(temp_rear > cnt_rear) {
					cnt_rear = temp_rear;
					cnt_front = temp_front;
					strcpy(copy_set, work_set);
				}
				else if(temp_rear == cnt_rear && cnt_front < temp_front) {
					cnt_rear = temp_rear;
					cnt_front = temp_front;
					strcpy(copy_set, work_set);
				}
			}
			strcpy(cur_set, copy_set);
			//printf("Cur_SET : %s\n",cur_set);
		}

		fprintf(out,"Case #%d: %d\n",t+1, cnt);
		//printf("Case #%d: %d\n",t+1, cnt);
	}
	fclose(in);
	fclose(out);

	return 0;
}