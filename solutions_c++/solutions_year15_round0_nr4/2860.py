#define _CRT_SECURE_NO_DEPRECATE

//��Ҫ:�ļ�Ҫ����Դ�ļ����ļ�������.
/*
fin = fopen("data.in", "r");
fout = fopen("data.out", "w");

fscanf(fin, "%d", &temp);
fprintf(fout, "%d", temp);

fclose(fin);
fclose(fout);
*/
/*��Ŀ˵��:R��ѡһ��ͼ��,G����Ҫͬһ��Rѡ��ͼ��
��������*/

#include <stdio.h>

int main(){
	FILE *fin, *fout;
	fin = fopen("D-small-attempt2.in", "r");
	fout = fopen("data.out", "w");

	int T = 0, k = 1;
	fscanf(fin, "%d", &T);
	while (T)
	{
		int x = 0, r = 0, c = 0;
		int flag = 0;

		fscanf(fin, "%d %d %d", &x, &r, &c);

		if ((r*c) % x != 0)//���������Ĳ����������RӮ
			goto R;

		else if (x > r*c)
			goto R;

		else if (x == 1)
			goto G;

		else if (r*c <= 2)//x=2,��������ѱ�����
			goto G;

		else if (x == 2 && ((r*c) % 2 == 0))
			goto G;

		else if (x == 2 && ((r*c) % 2 != 0))
			goto R;

		//�ų���x=2�����
		else if ((r == 1) || (c == 1))
			goto R;
		else if (r == 2 && c == 2)
			goto R;

		else if ((r == 3 && c == 2) || (r == 2 && c == 3))
			goto G;

		else if ((r == 2 && c == 4) || (r == 4 && c == 2))//�Գ�
			goto R;	

		else if (r == 3 && c == 3)
			goto G;

		else if ((r == 3 && c == 4) || (r == 4 && c == 3))
			goto G;
		else
			goto G;

	R:fprintf(fout, "Case #%d: RICHARD", k);
		flag = 1;
		if (!flag){
		G:fprintf(fout, "Case #%d: GABRIEL", k);
		}
		k++;
		T--;
		if (T){
			fprintf(fout, "\n");
		}
	}

	fclose(fin);
	fclose(fout);

	return 0;
}