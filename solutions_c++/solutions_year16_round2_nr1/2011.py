//
//  main.cpp
//  R1B_a
//
//  Created by CCHo on 2016/4/30.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    int cases;
    
    ifstream read("A-large.in");
    ofstream write("answer_A-large.txt");
//    ifstream read("large.in");
//    ofstream write("answer_A-large.txt");
    
    read >> cases;
    for (int c = 1; c <= cases; c++)
    {
        string X;
        read >> X;
        
        int num[10] = {0};
        
        for (int i=0; i<X.length(); i++)
        {
        
        switch(X[i]) {
            case 'Z': num[0]++;
                break;
            case 'O': num[1]++;
                break;
            case 'W': num[2]++;
                break;
            case 'R': num[3]++;
                break;
            case 'U': num[4]++;
                break;
            case 'F': num[5]++;
                break;
            case 'X': num[6]++;
                break;
            case 'V': num[7]++;
                break;
            case 'G': num[8]++;
                break;
            case 'N': num[9]++;
                break;
            default:
                break;
        }
        }
        
        num[1] = num[1] - num[0] - num[2] - num[4];
        num[3] = num[3] - num[0] - num[4];
        num[5] = num[5] - num[4];
        num[7] = num[7] - num[5];
        num[9] = (num[9]-num[1]-num[7])/2;
        
        
        write << "Case #" << c << ": ";
        for (int i=0; i<10; i++)
        {
            for (int j=0; j<num[i]; j++)
            {
                write << i;
            }
        }
        write << endl;
    }
    write.close();
    
    return 0;
}