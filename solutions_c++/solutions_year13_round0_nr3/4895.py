#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define FILE_IN "C-small-attempt0.in"
#define FILE_OUT "C-small-attempt0.out"

void write_out(int case_num, double out_num)
{
	FILE *file = fopen(FILE_OUT, "a");
	fprintf(file, "Case #%d: %.lf\n", case_num, out_num);
	fclose(file);
}

void write_out(int case_num, char *out_str)
{
	FILE *file = fopen(FILE_OUT, "w");
	fprintf(file, "Case #%d: %s\n", case_num, out_str);
	fclose(file);
}

int is_palindrome(double num)
{
	char str[65536];
	sprintf(str, "%.f", num);
	char *p1 = str;
	char *p2 = str+strlen(str)-1;
	
	while(p1<=p2)
	{
		if(*p1!=*p2)
			return 0;
		p1++;
		p2--;
	}
	return 1;
}

double my_sqrt(double num)
{
	double temp = sqrt(num);

	temp = floor(temp);
	if(pow(temp, 2.0)==num)
		return temp;
	else
		return 0;
}

int main()
{
	FILE *file = fopen(FILE_IN, "r");
	int case_num, i=0;
	fscanf(file, "%d", &case_num);
	while(i<case_num)
	{
		double sNum, eNum;
		double out_num = 0;
		fscanf(file, "%lf %lf", &sNum, &eNum);
		while(sNum<=eNum)
		{
			if(is_palindrome(sNum))
			{
				double son = my_sqrt(sNum);
				if(son!=0 && is_palindrome(son))
					out_num++;
			}
			sNum++;
		}
		//printf("Case #%d: %.lf\n", i+1, out_num);
		write_out(i+1, out_num);
		i++;
	}
	fclose(file);
	system("pause");
	return 0;
}