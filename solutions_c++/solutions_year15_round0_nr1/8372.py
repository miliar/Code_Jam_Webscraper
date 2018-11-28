//
//  main.cpp
//  codejam1
//
//  Created by KangCheol on 2015. 4. 11..
//  Copyright (c) 2015년 KangCheol. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
#define NUM_MAX 1000

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream input("/Users/Cheol/Desktop/Programming/algorithm/codejam1/codejam1/input.txt");
    ofstream output("/Users/Cheol/Desktop/Programming/algorithm/codejam1/codejam1/output.txt");
    
    int case_n, max_s, sum, ans;
    char num[NUM_MAX+10];
    
    input >> case_n;
    
    for(int i=1 ; i<=case_n ; i++)
    {
        ans=0;
        max_s=0;
        sum=0;
        input >> max_s;
        input >> num;
        for(int j=0 ; j<=max_s ; j++)
        {
            if(sum<j)
            {
                ans+=j-sum;
                sum+=j-sum;
            }
            sum+=(int)num[j]-48;
        }
        
        output << "Case #" << i <<": " << ans << endl;
    }
    
    return 0;
}
