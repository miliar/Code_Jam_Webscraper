//
//  main.cpp
//  codejam
//
//  Created by XiaDsh on 4/13/14.
//  Copyright (c) 2014 XiaDsh. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{

    int a[4][4],b[4][4];
    int t = 0, n1, n2, index;
    
    ifstream in("//Users//Tony//Documents//A-small-attempt1.in.txt");
    ofstream out("//Users//Tony//Documents//A-outfile");
    
    if (!in.is_open() || !out.is_open()) {
        cout<<"Error Filepath!!"<<endl;
        return 1;
    }
    
    in>>t;
    
    for (int i = 0; i<t; i++) {
        in>>n1;
        for (int j = 0; j<4; j++) {
            in>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
        }
        in>>n2;
        for (int j = 0; j<4; j++) {
            in>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
        }
        
        index = -1;
        n1 --;
        n2 --;
        for (int k = 0; k< 4; k++) {
            for (int m = 0; m < 4 ; m++){
                if (a[n1][k] == b[n2][m]) {
                    index = index == -1 ? k : -2;
                }
            }
        }
        out<<"Case #"<<i+1<<": ";
        if (index > -1) {
            out<<a[n1][index]<<endl;;
        }
        else if (index == -2)
        {
            out<<"Bad magician!"<<endl;
        }
        else
        {
            out<<"Volunteer cheated!"<<endl;
        }
        
    }
    cout<<"success!!"<<endl;
    return 0;
}

