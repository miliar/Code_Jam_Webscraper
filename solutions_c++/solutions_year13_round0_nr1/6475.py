
#include <iostream>
#include <string>
#include <stdio.h>

void main()
{
	FILE* fh = fopen("F:\\TestProject\\UnitTest\\Jam\\Release\\A-large.in", "r");
	if (fh == NULL)
	{
		return ;
	}

	FILE* fo = fopen("F:\\TestProject\\UnitTest\\Jam\\Release\\A-large.out", "w");
	if (fo == NULL)
	{
		return ;
	}

	char n[100];
	fgets (n , 100 , fh);

	int n_case = atoi(n);

	for (int cnt = 1 ; cnt <= n_case ; ++cnt) 
	{
		char matric[4][4];
		for (int row = 1 ; row <= 4 ; ++row) {
			char in[10];
			fgets (in, 10, fh);
			matric[row-1][0] = in[0];
			matric[row-1][1] = in[1];
			matric[row-1][2] = in[2];
			matric[row-1][3] = in[3];
		}

		if (cnt != n_case) {
			char in[10];
			fgets (in, 10, fh);
		}

		int c_x;
		int c_o;
		int c_e = 0;
		bool end = false;

		for (int row = 1 ; row <= 4 ; ++row) {
			c_x = 0;
			c_o = 0;
			for (int col = 1 ; col <= 4 ; ++col) {
				if (matric[row-1][col-1] == 'O') {
					++c_o;
				}
				else if (matric[row-1][col-1] == 'X') {
					++c_x;
				}
				else if (matric[row-1][col-1] == 'T') {
					++c_o;
					++c_x;
				}
				else if (matric[row-1][col-1] == '.') {
					++c_e;
				}
				//std::cout << matric[row-1][col-1];
			}
			std::cout << "c_x : " << c_x << ", c_o : " << c_o << ", c_e : " << c_e << std::endl;
			if (c_o == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'O', "won");
				end = true;
				goto end;
			}
			else if (c_x == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'X', "won");
				end = true;
				goto end;
			}
		}

		int r_x = 0;
		int r_o = 0;
		for (int col = 1 ; col <= 4 ; ++col) {
			r_x = 0;
			r_o = 0;
			for (int row = 1 ; row <= 4 ; ++row) {
				if (matric[row-1][col-1] == 'O') {
					++r_o;
				}
				else if (matric[row-1][col-1] == 'X') {
					++r_x;
				}
				else if (matric[row-1][col-1] == 'T') {
					++r_o;
					++r_x;
				}
				//std::cout << matric[row-1][col-1];
			}
			if (r_o == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'O', "won");
				end = true;
				goto end;
			}
			else if (r_x == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'X', "won");
				end = true;
				goto end;
			}
			std::cout << "r_x : " << r_x << ", r_o : " << r_o << std::endl;
		}

		int x = 0;
		int o = 0;
		for (int col = 1 ; col <= 4 ; ++col) {
			for (int row = 1 ; row <= 4 ; ++row) {
				if (col != row) {
					continue;
				}
				if (matric[row-1][col-1] == 'O') {
					++o;
				}
				else if (matric[row-1][col-1] == 'X') {
					++x;
				}
				else if (matric[row-1][col-1] == 'T') {
					++o;
					++x;
				}
				//std::cout << matric[row-1][col-1];
			}

			if (o == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'O', "won");
				end = true;
				goto end;
			}
			else if (x == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'X', "won");
				end = true;
				goto end;
			}
			//std::cout << "r_x : " << r_x << ", r_o : " << r_o << ", r_e : " << r_e << std::endl;
		}

		int xx = 0;
		int oo = 0;
		for (int col = 1 ; col <= 4 ; ++col) {
			for (int row = 1 ; row <= 4 ; ++row) {
				if ((col + row) != 5) {
					continue;
				}
				if (matric[row-1][col-1] == 'O') {
					++oo;
				}
				else if (matric[row-1][col-1] == 'X') {
					++xx;
				}
				else if (matric[row-1][col-1] == 'T') {
					++oo;
					++xx;
				}
				//std::cout << matric[row-1][col-1];
			}

			if (oo == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'O', "won");
				end = true;
				goto end;
			}
			else if (xx == 4) {
				fprintf (fo, "Case #%d: %c %s\n", cnt, 'X', "won");
				end = true;
				goto end;
			}
			//std::cout << "r_x : " << r_x << ", r_o : " << r_o << ", r_e : " << r_e << std::endl;
		}
end:
		if (end) {
			continue;
		}
		if (c_e == 0) {
			fprintf (fo, "Case #%d: Draw\n", cnt);
		}
		else {
			fprintf (fo, "Case #%d: Game has not completed\n", cnt);
		}
	}
	fclose(fh);
	fclose(fo);
}