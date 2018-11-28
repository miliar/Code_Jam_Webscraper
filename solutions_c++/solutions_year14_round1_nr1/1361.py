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
#include <set>
using namespace std;

bool str_cmp(string s1,string s2){ return s1 < s2;}

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

string answer(const  vector<vector<string>> & testcase ){
        vector<vector<string>> xor_bits;
        for(int i =0;i<testcase[0].size();i++){
            vector<string> bit_set;
            string xor_bit;
        
                for(int j=0;j<testcase[0].size();j++){
                    for(int k=0;k<testcase[0][i].size();k++){
                        if (testcase[0][i][k] != testcase[1][j][k]){
                            xor_bit+="1";
                        }
                        else
                            xor_bit+="0";
                    }
                   // cout<< xor_bit << "\n";
                    bit_set.push_back(xor_bit);
                    xor_bit ="";
                }
                
                xor_bits.push_back(bit_set);
                
         
        }

        //for(int i =0;i<xor_bits.size();i++){
        //    for(int j=0;j<xor_bits[0].size();j++){
        //        cout<<*xor_bits[0].begin() << "\n";
        //    }
        //}

        /*
        sort(xor_bits[0].begin(),xor_bits[0].end());
        sort(xor_bits[1].begin(),xor_bits[0].end());

        vector<string> result(testcase[0].size()*2);
        vector<string>::iterator it;

        it = set_intersection(xor_bits[0].begin(),xor_bits[0].end(),xor_bits[1].begin(),xor_bits[2].end(),result.begin());
        
        result.resize(it-result.begin());
        set<string> result_set(result.begin(),result.end());
        */
        vector<string> temp_set = xor_bits[0];

        for(int i=1;i<xor_bits.size();i++){
            vector<string> cmp_set = xor_bits[i];

            sort(temp_set.begin(),temp_set.end());
            sort(cmp_set.begin(),cmp_set.end());

            vector<string> result(testcase[0].size()*2);
            vector<string>::iterator it;

            it = set_intersection(temp_set.begin(),temp_set.end(),cmp_set.begin(),cmp_set.end(),result.begin());

            result.resize(it-result.begin());
            if(result.size() ==0){
                return "NOT POSSIBLE";
            }
            
            temp_set =  result;
            


        }
        int minsum=testcase[0][0].size();
        
        for (vector<string>::iterator it=temp_set.begin(); it!=temp_set.end(); ++it){
            int temp=0;
            for(int i=0;i<(*it).size();i++){
                if((*it)[i] == '1'){
                    temp+=1;
                }
            }

            if(temp < minsum){
                minsum = temp;
            }

        }
        stringstream  ss;
        ss << minsum;

    return ss.str();
}    


int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);



	string folder = "C:\\temp\\q1\\";
	


	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "A-small-attempt0.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<vector<string>>> list_cases;
    vector<string> list_result;


    string line, buf;
     vector<vector<string>> players;
    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            
            vector<string> row;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
            
            int i =(num_line-2)%3;
            switch(i){
            
            case 1:
            case 2:
                stringstream  ss;
                ss.str(line);
                
                while(ss >> buf){
                    //int temp=0;
                    //for(int i =0;i<buf.size();i++){
                    //    if(buf[i] == '1')
                    //        temp+= 1 << (buf.size()-i-1);
                    //}
                    row.push_back(buf);
                    //cout<< row << "\n";
                }
                //for(int i=0;i<row.size();i++){
                //    cout<< row[i] << "\n";
                //}
               players.push_back(row);
               

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




