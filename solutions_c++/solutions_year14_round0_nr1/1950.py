//
//  main.cpp
//  Google Code Jam Qualification Round 1
//
//  Created by Chunjing Jia on 4/11/14.
//  Copyright (c) 2013 Chunjing Jia. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
using namespace::std;



int main(int argc, const char * argv[])
{
    int nums;
    ifstream myfile("/Users/cjjia/Documents/Work/Google Code Jam/Qualification Round 1 Magic Trick/CloneGraph/A-small-attempt0.in");
    myfile >> nums;
    for(int num=0; num<nums; num++){
        vector<vector <int> > A(4, vector<int>(4));
        vector<vector <int> > B(4, vector<int>(4));
        int l1, l2;
        myfile >> l1;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                myfile >> A[i][j];
            }
        }
        myfile >> l2;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                myfile >> B[i][j];
            }
        }
        
        int res, casenum = 0;
        for(int i=0; i<4; i++){
            if(find(B[l2-1].begin(), B[l2-1].end(), A[l1-1][i]) != B[l2-1].end()) {
                casenum++;
                res = A[l1-1][i];
            }
        }
              
        if(casenum == 1) {
            cout << "Case #" << num+1 << ": " << res << endl;
        } else if (casenum == 0 ){
            cout << "Case #" << num+1 << ": Volunteer cheated!" << endl;
        } else if(casenum >1){
            cout << "Case #" << num+1 << ": Bad magician!" << endl;
        }
        
    }
    
    return 0;
}

