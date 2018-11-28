// TicTacToeTomek.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <vector>
#include <sstream>
using namespace std;

string magic(const  vector<vector<int>> & cards,vector< int> answers ){
    vector<int> magic_cards = cards[answers[0]];
    vector<int> magic_answers;

    //check if cheated
    int occur =0;
    int answer;
    for(int k=0;k<4;k++){
        for(int m = 0;m<magic_cards.size();m++){
            if (cards[4+answers[1]][k] == magic_cards[m]){
                occur++;
                answer=magic_cards[m];
                
            }
        }
    }
    if(occur == 0)
        return "Volunteer cheated!";
    else if(occur == 1){
        stringstream ss;
        ss << answer;
        return ss.str();
    }
    else{

        return "Bad magician!";
    }


    

}    

int _tmain(int argc, _TCHAR* argv[])
{
	time_t timer_begin,timer_end;
	timer_begin = time(NULL);


	string folder = "C:\\temp\\2014Q1\\";
	
	fstream outfile,infile;
	outfile.open(folder + "outfile.out",fstream::out);
	infile.open(folder+ "A-small-attempt0.in",fstream::in);

	int num_test=0, num_line=0;
	vector<vector<vector<int>>> list_cards;
    vector<string> list_result;
    vector<vector<int>> cards,answers;
    vector<int> answer;

    string line, buf;

    if (infile.is_open()){
	    while ( getline (infile,line) ){
            num_line++;
            vector<int> rows;
            
            if(num_test == 0){
                num_test = atoi(line.c_str());
                continue;
            }
  
            switch((num_line -2) % 10){
            case 0:

                
                answer.push_back(atoi(line.c_str())-1);
                
                if(!cards.empty()){
                    list_cards.push_back(cards);
                    cards.clear();
                }
 
                break;
            case 5:
                answer.push_back(atoi(line.c_str())-1);
                answers.push_back(answer);
                answer.clear();
                break;
            case 1:
            case 2:
            case 3:
            case 4:
            case 6:
            case 7:
            case 8:
            case 9:
                stringstream  ss;
                ss.str(line);
                
                while(ss >> buf)
                    rows.push_back(atoi(buf.c_str()));

                cards.push_back(rows);
                break;
            }
            
            
            
            
        }
    infile.close();
	}

    list_cards.push_back(cards);

    for(int i=0;i<num_test;i++){
        outfile << "Case #" << i+1 << ": " << magic(list_cards[i], answers[i]) << "\n";
    }

    outfile.close();   





    for(int i =0;i<answers.size();i++){
        for(int j=0;j<answers[i].size();j++){
            cout << answers[i][j];
        
        }
        cout<<"\n";
    }

	timer_end = time(NULL);
    cout << list_cards.size() << "," << answers.size() << "," << num_test << "\n";
	cout  << '\n' << difftime(timer_end,timer_begin);
	system("PAUSE");
	return 0;
}



