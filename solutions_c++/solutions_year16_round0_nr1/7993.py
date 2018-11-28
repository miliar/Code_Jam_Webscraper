#include<stdio.h>
#define IN in

int main(void)
{
	int i,j,k,t;
	int T;
	int n;
	int cnt;
	int flag[100];

	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("A-large.out","w");

	fscanf(IN,"%d", &T);

	for(t = 1; t <= T; t++)
	{
		for(k = 0; k <= 10; k++)
			flag[k] = 0;
		fscanf(IN,"%d",&n);
		cnt = 0;
		i = 0;
		while(1){
			if (n == 0) break;
			int chk = 1;
			for(k = 0; k < 10; k++)
			{
				//printf("%d ", flag[k]);
				if(flag[k] == 0){
					chk = 0;
					break;
				}
			}
			//printf("\ni = %d, chk = %d\n",i,chk);

			if(chk == 1) break;
			cnt++;
			i += n;

			j = i;
			while(1){
				k = j % 10;
				flag[k] = 1;
				j /= 10;
				if(j == 0) break;
			}
		}

		if (n == 0) {
			fprintf(out,"Case #%d: INSOMNIA\n",t);
		}
		else{
			fprintf(out,"Case #%d: %d\n",t,i);
		}
		//printf("Case #%d: %d\n",t,i);
	}

	fclose(in);
	fclose(out);

	return 0;
}