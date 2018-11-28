#include "sys.h"
#include "debug.h"


#include <stdio.h>
#include <stdlib.h>

#include <iostream>

#include <string>

#include <fstream>

#include <mpreal.h>

using namespace std;

int main(int argc, char **argv) {
    Debug( dc::notice.on() );             // Turn on the NOTICE Debug Channel.
    Debug( libcw_do.on() );               // Turn on the default Debug Object.

    Dout(dc::notice, "Starting");;

    mpfr::mpreal::set_default_prec(2048);
    
    
    int number_test=0;




    if(argc != 2 ) {
        cerr << "Only one parameter <filename>\n";
        exit(1);
    }

    ifstream inpf;

    inpf.open(argv[1]);
    if(!inpf.is_open()) {
        cerr << "Error opening file " << argv[1] << endl;
        exit(1);
    }

    char ch;
    char line[255];
    // Get Testcase number
    inpf.getline(line,253);

    Dout(dc::notice, "First line read :[" << line <<"]" );

    number_test=atoi(line);

    if(number_test <=0 ) {
        cerr << "There must be one test, at least\n";
        exit(1);
    }

    int i=0;
    while(i<number_test) {
        Dout(dc::notice, "Test : "<<i+1);
	cout << "Case #"<<i+1<<": ";
	mpfr::mpreal cost;
	mpfr::mpreal gain;
	mpfr::mpreal goal;
	
	/*
	cost.setPrecision(2048);
	gain.setPrecision(2048);
	goal.setPrecision(2048);
	*/
	
	string rl;
	inpf.getline(line,253);
	rl=line;
	Dout(dc::notice, "Line read :"<<rl);
	int idx=0;
	int ord=0;
	string nb="";
	while(idx < rl.size()) {
		if(rl[idx] == ' ') {
			switch(ord) {
				case 0:
					cost=nb;
					break;
				case 1:
					gain=nb;
					break;
				case 2:
					goal=nb;
					break;
			}
			ord++;
			nb="";
		} else {
			nb+=rl[idx];			
		}
		idx++;
	}
	switch(ord) {
		case 0:
			cost=nb;
			break;
		case 1:
			gain=nb;
			break;
		case 2:
			goal=nb;
			break;
	}
	ord++;
	nb="";
	if(ord!=3) {
		cerr << "Error missing parameter ["<<ord<<"]\n";
		exit(1);
	}
	Dout(dc::notice,"cost=["<<cost<<"] gain=["<<gain<<"] goal=["<<goal<<"]");
	
	Dout(dc::notice,"Solving");
	
	int go=1;
	long nb_fab=0;
	long step=0;
/*	long double rate=2;
	long double cur_time=0;
	long double time_to_goal_no_fab;
	long double time_to_goal_with_fab;
	long double time_to_next_fab;
	long double fab_time=cost/2;
	long double nb_cookies=0;*/


	mpfr::mpreal rate=2;
	mpfr::mpreal cur_time=0;
	mpfr::mpreal time_to_goal_no_fab;
	mpfr::mpreal time_to_goal_with_fab;
	mpfr::mpreal time_to_next_fab;
	mpfr::mpreal fab_time;
	mpfr::mpreal nb_cookies=0;
	
	/*
	rate.setPrecision(2048);
	cur_time.setPrecision(2048);
	time_to_goal_no_fab.setPrecision(2048);
	time_to_goal_with_fab.setPrecision(2048);
	time_to_next_fab.setPrecision(2048);
	fab_time.setPrecision(2048);
	nb_cookies.setPrecision(2048);
	*/
	
	fab_time=cost/2;
	
	/*
	mpfr::mpreal x;
	mpfr::mpreal y;
	
	x=3;
	y=5;
	x=y/x;
	*/
	
	while(go) {
		// Next Step
		time_to_next_fab=cost/rate;
		cur_time+=time_to_next_fab;
		
		// Have to choose
		time_to_goal_no_fab=cur_time+(goal)/rate;
		time_to_goal_with_fab=cur_time+cost/(rate) +  goal/(rate+gain);
		Dout(dc::notice,"cur_time=["<<cur_time<<"] nb_fab=["<<nb_fab<<"] rate=["<<rate<<"] time_to_next_fab=["<<time_to_next_fab<<"] time_to_goal_no_fab=["<<time_to_goal_no_fab<<"] time_to_goal_with_fab=["<<time_to_goal_with_fab<<"]");
		if(time_to_goal_no_fab > time_to_goal_with_fab ) {
			nb_fab++;
			rate=rate+gain;
		} else {
			cur_time += (goal-cost)/rate;
			go=0;
		}
	}
	Dout(dc::notice,"Time Found : ["<<cur_time.toString(10)<<"]");
	cout << cur_time.toString(10)<<endl;
        i++;
    }


    Dout(dc::notice, "Ending");
    return 0;
}
