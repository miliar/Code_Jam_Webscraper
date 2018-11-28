// OminousOmino.cpp : Defines the entry point for the console application.
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

string answer(const  vector<int> & testcase ){
    string ss="GABRIEL";
    int X= testcase[0];
    int R= testcase[1];
    int C= testcase[2];

    if (X >=7)
        ss = "RICHARD";
    if (X > R && X > C)
        ss = "RICHARD";
    if (R*C-X < 0 || (R*C % X !=0))
        ss = "RICHARD";
    if ( ((X+1)/2 > R) || ((X+1)/2 > C ))
        ss = "RICHARD";
    if (X>=4 && (R<=2 || C<=2))
        ss = "RICHARD";
    
   // ss << friends ;
    return ss;


}


int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);



	string folder = "C:\\temp\\2015Q4\\";
	


	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "D-small-attempt2.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<int>> list_cases;
    vector<int> list_result;


    string line, buf;

    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            vector<int> rows;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
            
           
                stringstream  ss;
                ss.str(line);
                
                while(ss >> buf)
                    rows.push_back((atoi(buf.c_str())));
                
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





