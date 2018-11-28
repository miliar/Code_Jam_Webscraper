//
//  main.cpp
//  Algorithm
//
//  Created by Luke Lee on 2016. 4. 9..
//  Copyright (c) 2016년 Luke Lee. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

bool checked[10];

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
        fill(checked, checked + 10, false);
        
        int n;
        fscanf(fin, "%d", &n);
        
        fprintf(fout, "Case #%d: ", _tc);
        
        if (n > 0)
        {
            int i;
            for (i = 1; ; i++)
            {
                for (int nn = i * n; nn > 0; nn /= 10)
                {
                    checked[nn % 10] = true;
                }
                
                bool all_checked = true;
                for_each(checked, checked + 10, [&](bool p) -> void { all_checked &= p; });
                if (all_checked) break;
            }
            
            fprintf(fout, "%d\n", i * n);
        }
        else
        {
            fprintf(fout, "INSOMNIA\n");
        }
    }
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}
