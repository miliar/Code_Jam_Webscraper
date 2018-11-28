//
//  main.cpp
//  R1C_a
//
//  Created by CCHo on 2016/5/8.
//  Copyright © 2016年 UCD. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream read("A-large.in");
//    ofstream write("answer_A-small.txt");
    //    ifstream read("A-large-practice.in");
        ofstream write("answer_A-large.txt");
    
    int Ts;
    
    read >> Ts;
    for (int t = 1; t <= Ts; t++)
    {
        write << "Case #" << t << ": ";
        int N, big1, big2;
        read >> N;
        int total = 0;
        vector<int> P;
        for (int i=0; i<N; i++)
        {
            int ps;
            read >> ps;
            P.push_back(ps);
            
            total += ps;
        }
        
        if (P[0]>P[1])
        {
            big1 = 0;
            big2 = 1;
        }
        else
        {
            big1 = 1;
            big2 = 0;
        }
        for (int i=2; i<N; i++)
        {
            int tmp;
            if (P[i]>=P[big1])
            {
                tmp = big1;
                big1 = i;
                big2 = tmp;
            }
            else if (P[i]>P[big2])
            {
                big2 = i;
            }
        }
        
        int tmp = 0;
        int index = 0;
        while (tmp<total) {
            if (P[big1]>=P[big2]+2)
            {
                write << (char)('A'+big1) << (char)('A'+big1) << " ";
                P[big1] -= 2;
                tmp += 2;
            }
            else if (P[big1]==P[big2]+1)
            {
                write << (char)('A'+big1) << " ";
                P[big1] -= 1;
                tmp += 1;
            }
            else
            {
                
                while (index<N)
                {
                    if (index==big1 || index == big2)
                        index++;
                    else
                    {
                        while (P[index]>0)
                        {
                            write << (char)('A'+index) << " ";
                            P[index]--;
                            tmp++;
                        }
                        index++;
                    }
                }
                
                while (P[big1]>0)
                {
                    write << (char)('A'+big1) << (char)('A'+big2) << " ";
                    P[big1]--;
                    tmp += 2;
                }
                
            }
        }
        
        write << endl;
    }
    write.close();
    
    return 0;
}