
#include <iostream>
#include <string>
#include <stdio.h>
#include <math.h>

bool is_palindromes(char str[1024])
{
	int length = strlen(str);
	for (int i = 0 ; i < length ;++i) {
		if (str[i] != str[length - i - 1]) {
			return false;
		}
	}
	return true;
}

bool is_square(int m)//pass test
{
    int t = sqrt((double)m); 
    if(t * t == m){
        return true;
    }
    return false;
}

void main()
{
	FILE* fh = fopen("F:\\TestProject\\UnitTest\\Square\\C-small-attempt1.in", "r");
	if (fh == NULL)
	{
		return ;
	}

	FILE* fo = fopen("F:\\TestProject\\UnitTest\\Square\\C-small-attempt1.out", "w");
	if (fo == NULL)
	{
		return ;
	}

	int n_case = 0;
	fscanf (fh, "%d\n", &n_case);

	for (int run = 1 ; run <= n_case ; ++run) {
		int lower = 0;
		int upper = 0;

		fscanf (fh, "%d %d\n", &lower, &upper);

		int cnt = 0;
		int limit = sqrt((double)upper);
		for (int i = ceil(sqrt((double)lower)) ; i <= limit ; ++i) {
			char str[1024];
			double power = pow((double)i, 2);
			int c_power = (int)power;
			//itoa(c_power, str, 1024);
			sprintf (str, "%d", i);
			std::cout << str << std::endl;
			if (!is_palindromes(str)) {
				continue;
			}
			sprintf (str, "%d", c_power);
			if (!is_palindromes(str)) {
				continue;
			}
			++cnt;
		}

		
		/*for (int iter = lower ; iter <= upper ; ++iter) {
			if (!is_square(iter)) {
				continue;
			}
			
			char str[1024];
			if (!is_palindromes(itoa(iter, str, 1024))) {
				continue;
			}
			++cnt;
		}*/

		fprintf (fo, "Case #%d: %d\n", run, cnt);
	}
	fclose(fh);
	fclose(fo);
}