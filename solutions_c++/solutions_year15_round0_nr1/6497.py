// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

string answer(const  vector<string> & testcase ){
    int friends=0;
    
    
    int sum = atoi(testcase[1].substr(0,1).c_str());

    

    
    for ( int i =1;i< testcase[1].size();i++){
        int a=atoi(testcase[1].substr(i,1).c_str());

        if(i > sum){
            friends+=(i-sum);
            sum += (i-sum);
        }
        
        sum+=a;
    }

    stringstream ss;
    ss << friends ;
    return ss.str();


}


int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);



	string folder = "C:\\temp\\2015Q1\\";
	


	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "A-large.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<string>> list_cases;
    vector<string> list_result;


    string line, buf;

    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            vector<string> rows;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
            
           
                stringstream  ss;
                ss.str(line);
                
                while(ss >> buf)
                    rows.push_back((buf.c_str()));
                
                list_cases.push_back(rows);
     
            

            
        }
    infile.close();
	}

    //cout.precision(7);
    //cout.setf( ios::fixed, ios::floatfield );

    //for(int i =0;i<list_cases.size();i++){
    //    for(int j=0;j<list_cases[i].size();j++)
    //        cout<< list_cases[i][j] << " ";
    //    cout << "\n";
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



