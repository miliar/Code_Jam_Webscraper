//
//  main.cpp
//  codeJam2013
//
//  Created by Guillaume Derval on 13/04/13.
//  Copyright (c) 2013 Guillaume Derval. All rights reserved.
//

#include <iostream>
#include <fstream>

int main(int argc, const char * argv[])
{
    std::ifstream finput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/B-large.in");
    std::ofstream foutput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/out.out");
    
    std::istream& input = finput;
    std::ostream& output = foutput;
    
    int T;
    input >> T;
    for(int test = 0; test < T; test++)
    {
        int N,M;
        input >> N >> M;
        
        int* lines = new int[N];
        int* col = new int[M];
        int** height = new int*[N];
        
        bool possible = true;
        
        for(int i = 0; i < N; i++)
        {
            lines[i] = 0;
            height[i] = new int[M];
        }
        
        for(int i = 0; i < M; i++)
            col[i] = 0;
        
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < M; j++)
            {
                input >> height[i][j];
                
                lines[i] = std::max(lines[i], height[i][j]);
                col[j] = std::max(col[j], height[i][j]);
            }
        }
        
        for(int i = 0; i < N && possible; i++)
        {
            for(int j = 0; j < M && possible; j++)
            {
                possible = (lines[i] == height[i][j] && col[j] >= height[i][j]) || (col[j] == height[i][j] && lines[i] >= height[i][j]);
            }
        }
        
        output << "Case #" << (test+1) << ": ";
        if(possible)
            output << "YES";
        else
            output << "NO";
        output << std::endl;
    }
    
    finput.close();
    foutput.close();
    return 0;
}

