#include<stdio.h>
#include<iostream>
#include <fstream>

using namespace std;

int main(){
    int testcases;
    cin >> testcases;
    ofstream outputfile ("output.txt");
    //if(outputfile.is_open()){
    //    cout << "File opened! \n";

    //}
    
    int firstans;
    int secondans;
    int firstarr[4][4];
    int secondarr[4][4];
    int multiples = 0;
    int ans = 0;
    int casenum = 0;
    string output = "";

    for(int h = 0; h < testcases; h++){
        //cout << "h is " << h << endl;
        multiples = 0;
        ans = 0;
        cin >> firstans;
        //cout << firstans << endl;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> firstarr[i][j];
                //cout << firstarr[i][j] << endl;
            }
        }
        cin >> secondans;
        //cout << secondans << endl;

        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> secondarr[i][j];
            }
        }
        
        for(int i = 0; i < 4; i++){
            int case1 = firstarr[firstans-1][i];
            for(int j = 0; j < 4; j++){
                int case2 = secondarr[secondans-1][j];
                if(case1==case2){
                    multiples++;
                    ans = case1;
                }   
            }
        }
        if(multiples == 1){
            output = to_string(ans);
        }
        else if(multiples>1){
            output = "Bad magician!";
        }
        else if(multiples == 0){
            output = "Volunteer cheated!";
        }
        casenum = h + 1;
        cout << "Case #" << casenum << ": " << output<<"\n";
        //printf("Case #%d: %s",h+1,output);
        
    }
    outputfile.close();
    //cout << "Done!\n";
    
    return 0;
}