// Main.cpp : Defines the entry point for the console application.
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

bool desc_sort (double i,double j) { return (i>j); }

int get_num( vector<double>  vec_1, vector<double>  vec_2){
    int num =0;
    bool is_break = true;
    double value;
    while(vec_1.size()>0){
        
        value=vec_1.front();
        vec_1.erase(vec_1.begin());
        for(int k=0;k<vec_2.size();k++){
            if(value>vec_2[k]){
                num++;
                
                vec_2.erase(vec_2.begin()+k);
                
                is_break = false;
                break;
            }
        }
        if(is_break)
            break;
    }
    return num;


}

string answer(const  vector<vector<double>> & testcase ){
    vector<double> naomi = testcase[0];
        
    vector<double> ken = testcase[1];
    sort(naomi.begin(),naomi.end(),desc_sort);
    sort(ken.begin(),ken.end(),desc_sort);

    int num_decv=0,num_war=0;

    num_decv = get_num(naomi,ken);
    num_war = naomi.size()-get_num(ken,naomi);

    stringstream ss;
    ss << num_decv << " " << num_war;
    return ss.str();

}    


int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);



	string folder = "C:\\temp\\2014Q4\\";
	


	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "test.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<vector<double>>> list_cases;
    vector<string> list_result;


    string line, buf;
     vector<vector<double>> players;
    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            vector<double> rows;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
            
            int i =(num_line -2)%3;
            switch(i){
            
            case 1:
            case 2:
                stringstream  ss;
                ss.str(line);
                
                while(ss >> buf)
                    rows.push_back(atof(buf.c_str()));
                
                players.push_back(rows);

                if(i ==2){
                    list_cases.push_back(players);
                    players.clear();
                }
                break;
            }
            

            
        }
    infile.close();
	}

    cout.precision(7);
    cout.setf( ios::fixed, ios::floatfield );


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




