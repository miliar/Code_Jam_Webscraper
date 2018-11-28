
#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <string.h>  /* strlen */
//#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>  /* atoi, atof */
#include <math.h>       /* round, floor, ceil, trunc */
using namespace std;

int main ()
{
ifstream F_param;
ifstream F_in;
ofstream F_log;
ofstream F_out;

char line_in[1010], line_out[20], line_log[1500], line_par[150];
char fn_in[50], fn_log[50], fn_out[50];
long int N_test, N_soluce, i_1, i_2, i_3, i_4, i_5, N_trace;

char c_audience[1001];//, c_shylvlnbr;
long int n_shylvl, n_stand;//, n_shylvlnbr, n_audnbr;

F_param.open("cj2015qala.par");
F_param.getline (line_par, 25);
sprintf(fn_in, "%s.in", line_par );
sprintf(fn_log, "%s.log", line_par );
sprintf(fn_out, "%s.out", line_par );

F_param.getline (line_par, 2);
N_trace = atoi(line_par);

F_in.open(fn_in);
F_out.open(fn_out);
F_log.open(fn_log);

F_in.getline (line_in, 10);
N_test = atoi(line_in);
if (N_trace == 1)F_log << N_test << '\n';
for (i_1 = 1; i_1 <= N_test;i_1++){
	N_soluce = 0;
	F_in.getline(line_in, 10, ' ');
	n_shylvl = atoi(line_in);if (N_trace == 1){sprintf(line_log, "n_shylvl:%d ", n_shylvl );F_log << line_log;}
	F_in.getline(c_audience, 1010);if (N_trace == 1){sprintf(line_log, "c_audience:%s \n", c_audience );F_log << line_log;}
	n_stand=0;
	for (i_2 = 0; i_2 < strlen(c_audience); i_2++){
		//n_shylvlnbr = c_audience[i_2]-'0';if (N_trace == 1){sprintf(line_log, "n_shylvlnbr:%d ", n_shylvlnbr );F_log << line_log;}
		//n_stand += n_shylvlnbr;if (N_trace == 1){sprintf(line_log, "n_stand:%d ", n_stand );F_log << line_log;}
		n_stand += c_audience[i_2]-'0';//if (N_trace == 1){sprintf(line_log, "n_stand:%d ", n_stand );F_log << line_log;}
		if (N_soluce + n_stand <= i_2){N_soluce+= i_2 - (N_soluce + n_stand)+1 ;}
	}
	sprintf(line_out, "Case #%d: %d\n", i_1, N_soluce );F_out << line_out;
	if (N_trace == 1){F_log << line_out;}
}
F_param.close();
F_log.close();
F_in.close();
F_out.close();
}