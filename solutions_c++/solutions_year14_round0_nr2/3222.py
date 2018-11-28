//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <vector>
#include <sstream>
using namespace std;

const double base_rate = 2.0;

double answer(const  vector<double> & testcase ){
       
    double farm_cost,farm_rate,target, seconds,current_rate;

    farm_cost = testcase[0];
    farm_rate = testcase[1];
    target = testcase[2];


    seconds=0.0;

    current_rate = base_rate;
    while(true){
        if (target/(current_rate+farm_rate)< (target-farm_cost)/current_rate){
            seconds +=farm_cost/current_rate;
            current_rate+=farm_rate;
        }
        else{
            seconds += target/current_rate;
            break;
        }
    }

   
    return seconds;
}    


int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);



	string folder = "C:\\temp\\2014Q2\\";
	


	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "test.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<double>> list_cases;
    vector<string> list_result;


    string line, buf;

    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            vector<double> rows;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
            stringstream  ss;
            ss.str(line);
                
            while(ss >> buf)
                rows.push_back(atof(buf.c_str()));

            list_cases.push_back(rows);
        }
    infile.close();
	}

    cout.precision(7);
    cout.setf( ios::fixed, ios::floatfield );
    outfile.precision(7);
    outfile.setf( ios::fixed, ios::floatfield );

    //for(int i=0;i<list_cases.size();i++){
    //    for(int j=0;j<list_cases[i].size();j++){
    //        cout<< list_cases[i][j]<< ",";
    //    }
    //    cout<<"\n";

    //}

    for(int i=0;i<num_test;i++){
        outfile << "Case #" << i+1 << ": " << answer(list_cases[i]) << "\n";
    }

    outfile.close();   





    //for(int i =0;i<answers.size();i++){
    //    for(int j=0;j<answers[i].size();j++){
    //        cout << answers[i][j];
    //    
    //    }
    //    cout<<"\n";
    //}

	timer_end = time(NULL);
    cout << list_cases.size() << "," << num_test << "\n";
	cout  << '\n' << difftime(timer_end,timer_begin);
	system("PAUSE");
	return 0;
}



