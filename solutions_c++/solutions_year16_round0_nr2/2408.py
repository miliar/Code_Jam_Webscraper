#include<stdio.h>
#include<string.h>
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");
int A()
{
	char D[110] = { 0, }, Temp[110] = { 0, };
	fscanf(in, "%s", D);
	int i, end, len = strlen(D) ,cnt=0, t;

	end = len - 1;
	for (;;) {
		/// ������ �� �� ã��
		for (;end>=0;) {
			if (D[end] == '-')break;
			end--;
		}

		if (end < 0) break;
		/// �պκ� -�� �����
		if (D[0] == '+') {
			cnt++;
			for (i = 1;i<=end; i++) {
				if (D[i] == '-') break;
			}
			for (i = i - 1; i >= 0; i--) {
				D[i] = '-';
			}
		}


		/// �պκ� -�� �� ���� ã��

		for (i = 0; i <= end; i++) {
			if (D[i] == '+')break;
		}

		// Dġȯ ���ְ�
		for (i = 0; i <= end; i++) {
			Temp[i] = D[i];
		}
		cnt++;
		for (i = 0; i <= end; i++) {
			if (Temp[end - i] == '+') D[i] = '-';
			else D[i] = '+';
		}
		
	}
	fprintf(out,"%d\n", cnt);
	return 0;
}

int main()
{
	int T,i=1; fscanf(in,"%d",&T);

	while (T--) {
		fprintf(out,"Case #%d: ",i++);
		A();
	}

	return 0;
}