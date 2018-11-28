//
//  main.cpp
//  Algorithm
//
//  Created by Luke Lee on 2016. 4. 9..
//  Copyright (c) 2016년 Luke Lee. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cstring>

#define L 100

using namespace std;

char pancake[L + 1];

int main(int argc, const char * argv[])
{
    // insert code here...
    FILE* fin = fopen("/Users/luke0201/Desktop/input.txt", "r");
    FILE* fout = fopen("/Users/luke0201/Desktop/output.txt", "w");
    if (fin && fout)
    {
        printf("Successfully opened.\n");
    }
    else
    {
        printf("Failed to open.\n");
        exit(0);
    }
    
    int tc;
    fscanf(fin, "%d", &tc);
    for (int _tc = 1; _tc <= tc; _tc++)
    {
        fscanf(fin, "%s", pancake);
        
        int l = (int)strlen(pancake);
        
        int cnt = (pancake[l - 1] != '+');
        for (int i = 1; i < l; i++)
        {
            cnt += (pancake[i] != pancake[i - 1]);
        }
        
        fprintf(fout, "Case #%d: ", _tc);
        
        fprintf(fout, "%d\n", cnt);
    }
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}
