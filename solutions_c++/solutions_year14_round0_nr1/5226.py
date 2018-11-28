//
//  main.cpp
//  realthing
//
//  Created by Abhishek Anand on 13/04/14.
//  Copyright (c) 2014 AbhishekAnand. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[])
{

    ofstream out ("A.txt");
    int n;
    cin >> n;
    for(int i = 0; i <n; i++){

        int a, b;
        int c[4][4];
        int d[4][4];
        cin >> a;
        for(int x = 0; x <4; x++){
            for(int y = 0; y<4; y++){

                cin >> c[x][y];
            }
        }
        cin>> b;
        for(int x = 0; x <4; x++){
            for(int y = 0; y<4; y++){

                cin >> d[x][y];
            }
        }
        int answer=0;
        int value;
        for(int x = 0; x <4; x++){

            for(int y = 0; y<4; y++){
                if(c[a-1][x]==d[b-1][y]){

                    answer++;
                    value=c[a-1][x];
                }

            }
        }
        if(answer ==1){

            out << "Case #" << i+1 << ": " << value<< "\n";
        }else if( answer == 0){
            out<< "Case #" << i+1 << ": Volunteer cheated!" << "\n";

        }else{

            out << "Case #" << i +1<< ": Bad magician!"<< "\n";
        }
    }return 0;
}
