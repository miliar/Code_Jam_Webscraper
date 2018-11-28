//
//  main.cpp
//  Problem_A._MagicTrick
//
//  Created by KoRNz on 4/12/2557 BE.
//  Copyright (c) 2557 KoRNz. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

vector<int> Solve() {
    
    //To choose first number of row
    int rowChosen1=0;
    cin >> rowChosen1;
    
    //store the card
    int tmp=0;
    vector<int> chosenDeq;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> tmp;
            if(i==rowChosen1-1) chosenDeq.push_back(tmp);
        }
    }
    
    //To choose second number of row
    int rowChosen2=0;
    cin >> rowChosen2;
    
    //store the card the second time
    vector<int> deq;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> tmp;
            if(i==rowChosen2-1) deq.push_back(tmp);
        }
    }

    //to check the changing
    vector<int> chosenCard;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (!chosenDeq.empty() && !deq.empty() && chosenDeq[i] == deq[j]) {
                chosenCard.push_back(deq[j]);
            }
        }
    }
    
    //return answer
    return chosenCard;
};

int main()
{
    //To insert number of testcases
    int n = 0;
    cin >> n;
    
    string* print = new string[n];
    
    //To call Solve method
    vector<int> answer;
    for (int i=0; i<n; i++) {
        answer = Solve();
        
        int num = i+1;
        ostringstream convert;
        convert << num;
        string sNum = convert.str();
        
        //store answer
        if (answer.size() > 1) {
            print[i] = "Case #" + sNum + ": " + "Bad magician!";
        }
        else if (answer.size() == 0) print[i] = "Case #" + sNum + ": " + "Volunteer cheated!";
        else if (answer.size() == 1) {
            ostringstream convert2;
            convert2 << answer[0];
            string sAnswer = convert2.str();
            
            print[i] = "Case #" + sNum + ": " + sAnswer;
        }
    }
    
    //to print
    for (int i=0; i<n; i++) {
        cout << print[i] << endl;
    }
    
    return 0;
}

