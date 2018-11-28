
#include <iostream>
#include <fstream>
#include <istream>
//#include <string>   /* length */
//#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>  /* atoi */
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
int N_test, i_1, i_2, i_3, i_4, N_soluce, N_trace;

char C_soluce[20];	
int N_answ1, N_answ2, N_len, N_card[4], N_card2;

F_param.open("Q2014A.par");
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
	sprintf (C_soluce ,  "Volunteer cheated!");
	N_soluce = 0;
	F_in.getline(line_in, 4);
	N_answ1 = atoi(line_in);if (N_trace == 1){sprintf(line_log, "N_answ1:%d, ", N_answ1 );F_log << line_log;}
	for (i_2 = 0; i_2 < 4 ; i_2++){
		if (N_answ1 != i_2+1)F_in.getline(line_in, 15);
		else for (i_3 = 0; i_3 < 4 ; i_3++){
			if (i_3 == 3) F_in.getline(line_in, 4, '\n');
			else F_in.getline(line_in, 4, ' ');	
			N_card[i_3] =  atoi(line_in);if (N_trace == 1){sprintf(line_log, "N_card %d:%d, ", i_3, N_card[i_3] );F_log << line_log;}
			
		}
	}
	if (N_trace == 1){F_log << "\n";}
	F_in.getline(line_in, 4);
	N_answ2 = atoi(line_in);if (N_trace == 1){sprintf(line_log, "N_answ2:%d, ", N_answ2 );F_log << line_log;}
	for (i_2 = 0; i_2 < 4 ; i_2++){
		if (N_answ2 != i_2+1)F_in.getline(line_in, 15);
		else for (i_3 = 0; i_3 < 4 ; i_3++){
			if (i_3 == 3) F_in.getline(line_in, 4, '\n');
			else F_in.getline(line_in, 4, ' ');	
			N_card2 =  atoi(line_in);if (N_trace == 1){sprintf(line_log, "N_card %d:%d, ", i_3, N_card2 );F_log << line_log;}
			for (i_4 = 0 ; i_4 < 4; i_4++){
				if (N_card2 == N_card[i_4]){
					if (N_soluce == 0) {N_soluce++;sprintf (C_soluce ,  line_in);}
					else sprintf (C_soluce ,  "Bad magician!");
				}
				if (N_trace == 1){sprintf(line_log, "N_card %d:%s \n", N_card[i_4], C_soluce );F_log << line_log;}
			}	
		}
	}
	if (N_trace == 1){F_log << "\n";}
	sprintf(line_out, "Case #%d: %s\n", i_1, C_soluce );F_out << line_out;
	
}
F_param.close();
F_log.close();
F_in.close();
F_out.close();
}