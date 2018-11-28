/* 
 * File:   main.cpp
 * Author: alstraumann
 *
 * Created on April 12, 2014, 11:44 AM
 */

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void Print(vector<float>& v){
    for (int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    cout << endl;
}
/*
 * 
 */
int main(int argc, char** argv) {
    ifstream in;
    in.open("test2.txt");
    int testCases, caseNum;
    in>>testCases;
    caseNum=1;
    while(caseNum<=testCases){
        vector<float> times;
        double C, F, X, CPS;
        CPS=2;
        in>>C>>F>>X;
        //cout << "C: "<<C << " F: "<<F << " X: "<< X <<endl;
        
        double bestTime=X/CPS;
        double tempTime;
        //cout << "bestTime start: "<<bestTime << endl;
        
        //cout << "tempTime start: "<<tempTime << endl;
        
        bool bestNotBeat=false;
        while(!bestNotBeat){
            //Print(times);

            times.push_back(C/CPS);

            tempTime=0;
            for (int n=0; n<times.size(); n++) 
                  tempTime += times[n];
            CPS+=F;
            tempTime+=X/CPS;
            //cout << "tempTime: "<< tempTime<<endl;

            //cout << "bestTime: "<< bestTime <<endl;
            if(tempTime<=bestTime){
                bestTime=tempTime;
            }
            else{
                bestNotBeat=true;
            }       
        }
        cout << "Case #" << caseNum << ": ";
        cout.precision(9);
        cout<< bestTime<<endl;
        caseNum++;
        
    }
    
    return 0;
}

