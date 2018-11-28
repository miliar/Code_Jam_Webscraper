#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

main(){

    ifstream in;
    ofstream out;
    in.open("input.in");
    out.open("output.out");

    int numOfCases = 0;
    in >> numOfCases;
    cout << "Num of cases: " << numOfCases <<endl;
    system("pause");

    int blocks = 0;


    vector<double> table1;
    vector<double> table2;
    double temp;

    int countDWar = 0;
    int countWar = 0;


    for(int t=0 ;t<numOfCases; t++){

        countDWar = 0;


        in >> blocks;

        for(int i=0; i<blocks; i++){
            in >> temp;
            table1.push_back(temp);
        }
        for(int i=0; i<blocks; i++){
            in >> temp;
            table2.push_back(temp);
        }

        sort(table1.begin(),table1.end());
        sort(table2.begin(),table2.end());

        int i=0;
        int j=0;
        while(i<blocks){
            if(table1[i] > table2[j]){
                i++;
                j++;
                countDWar++;
            }
            else{
                i++;
            }
        }

        countWar = 0;
        i=0;
        j=0;
        for(i=0; i<blocks; i++){
            for(j=0 ; j<table2.size(); j++){
                if(table1[i]<table2[j]){
                    break;
                }
            }
            if(j == table2.size()){
                table2.erase(table2.begin());
                countWar++;
            }
            else{
                table2.erase(table2.begin()+j);
            }
        }


        out << "Case #" << t+1 << ": " << countDWar << " " << countWar << endl;

        table1.clear();
        table2.clear();
    }

}
