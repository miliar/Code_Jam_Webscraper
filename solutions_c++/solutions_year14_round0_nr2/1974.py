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
#include <iomanip>

using namespace::std;



int main(int argc, const char * argv[])
{
    int nums;
    ifstream myfile("/Users/cjjia/Documents/Work/Google Code Jam/Qualification Round 2 Cookies/CloneGraph/B-large.in");
    /*
     When C/cook + X/(cook+F) > X/cook, we don't buy a farm...
     or C*(cook + F) > X*F
     
     */
    cout.setf(ios::fixed);
    myfile >> nums;
    for(int num=0; num<nums; num++){
        double paraC, paraF, paraX;
        myfile >> paraC >> paraF >> paraX;
        long double time=0;
        //int farms = (paraX/paraC-1.0)*paraF;
        //cout << farms;
        int farms = ((paraX/paraC-1.0)*paraF-2.0)/paraF+1;
        farms = farms < 0 ? 0 : farms;
        
        time = paraX/(paraF*farms+2.0);
        while(farms>0){
            time += paraC/(paraF*(--farms)+2.0);
        }
        cout << "Case #" << num+1 << ": ";

        cout<<setprecision(7) << time << endl;
    }
    return 0;
}


