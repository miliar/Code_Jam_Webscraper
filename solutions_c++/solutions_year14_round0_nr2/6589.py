
#include <iostream>
#include <fstream>
#include <istream>
//#include <string>   /* length */
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

char line_in[400], line_out[150], line_log[150], line_par[150];
char fn_in[50], fn_log[50], fn_out[50];
int N_test, i_1, i_2, i_3, i_4, N_trace;

double F_soluce, F_capa, F_cost, F_prod, F_targ, F_next, F_delta, F_elapse;
int N_farm;

F_param.open("Q2014B.par");
F_param.getline (line_par, 50);
sprintf(fn_in, "%s.in", line_par );
sprintf(fn_log, "%s.log", line_par );
sprintf(fn_out, "%s.out", line_par );

F_param.getline (line_par, 2);
N_trace = atoi(line_par);

F_in.open(fn_in);
F_log.open(fn_log);
F_out.open(fn_out);

F_in.getline (line_in, 10, '\n');
N_test = atoi(line_in);
if (N_trace == 1)F_log << N_test << '\n';
for (i_1 = 1; i_1 <= N_test;i_1++){
	F_capa = 2; N_farm = 0; F_elapse = 0 ;
	F_in.getline(line_in, 15, ' ');
	F_cost = atof(line_in);if (N_trace == 1){sprintf(line_log, "cost:%f, ", F_cost );F_log << line_log;}
	F_in.getline(line_in, 15, ' ');
	F_prod = atof(line_in);if (N_trace == 1){sprintf(line_log, "prod:%f, ", F_prod );F_log << line_log;}
	F_in.getline(line_in, 15);
	F_targ = atof(line_in);if (N_trace == 1){sprintf(line_log, "targ:%f, ", F_targ );F_log << line_log;}
	F_next = F_targ/2;if (N_trace == 1){sprintf(line_log, "base target :%f \n", F_next );F_log << line_log;}
	do{
		F_soluce = F_next;
		F_delta = F_cost / F_capa;
		N_farm++;
		F_capa = 2 + F_prod * N_farm;if (N_trace == 1){sprintf(line_log, "F_capa:%f, ", F_capa );F_log << line_log;}
		F_elapse += F_delta;
		F_next = F_elapse + F_targ / F_capa;if (N_trace == 1){sprintf(line_log, "F_next:%.7f, ", F_next );F_log << line_log;}
	} while (F_soluce > F_next);
	if (N_trace == 1){F_log << "\n";}
	sprintf(line_out, "Case #%d: %.7f\n", i_1, F_soluce );F_out << line_out;
	
}
F_param.close();
F_log.close();
F_in.close();
F_out.close();
}