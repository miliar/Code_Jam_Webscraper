//
//  main.cpp
//  codeJam
//
//  Created by Zurab Kachukhashvili on 4/13/13.
//  Copyright (c) 2013 Zurab Kachukhashvili. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int k;
    ifstream ifs("input.txt");
    ofstream ofs("output.txt");
    ifs>>k;
    
    for (int p = 0; p < k; p++)
    {
        bool isPossable(true);
        int l, m;
        ifs>>l>>m;
        
        int **data=new int*[l];
        for (int i = 0 ; i < l ; i++) {
            data[i] = new int[m];
            for (int r = 0; r<m ; r++) {
                ifs>>data[i][r];
            }
        }
        
        
        for (int i = 0; i < l; i++) {
            for (int r = 0; r< m ; r++) {
                int currentHeight(data[i][r]);
                
                bool horizont(true),vertical(true);

                for (int h=0; h<l; h++) {
                    if (currentHeight < data[h][r]) {
                        horizont = false;
                        break;
                    }
                }
                for (int v=0; v<m ; v++) {
                    if (currentHeight < data[i][v]) {
                        vertical = false;
                        break;
                    }
                }
                
                if (horizont == false && vertical == false) {
                    isPossable = false;
                    break;
                }
            }
            if (!isPossable) {
                break;
            }
        }

        if (isPossable) {
            ofs<<"Case #"<<p+1<<": YES"<<endl;
        }
        else
        {
            ofs<<"Case #"<<p+1<<": NO"<<endl;
        }
    }
    
    
    return 0;
}

