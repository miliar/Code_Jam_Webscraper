//
//  main.cpp
//  Magic Trick
//
//  Created by Alexandru Andronache on 9/1/13.
//  Copyright (c) 2013 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T, N;
std::vector<std::string> words;
std::vector<int> pos;
std::vector<int> sizes;

long long rez = 0;

int main()
{
    fscanf(f, "%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        words.clear();
        pos.clear();
        sizes.clear();
        rez = 0;
        
        fscanf(f, "%d\n", &N);
        for (int i = 0; i < N; ++i)
        {
            char sir[200];
            fgets(sir, 200, f);
            words.push_back(sir);
            pos.push_back(0);
        }
        
        while(true)
        {
            sizes.clear();
            char letter = words[0][pos[0]];
            bool isSol = true;
            int size = 0;
            while (letter == words[0][pos[0]])
            {
                pos[0]++;
                size++;
            }
            sizes.push_back(size);
            for (int i = 1; i < N; ++i)
            {
                if (words[i][pos[i]] != letter)
                {
                    isSol = false;
                }
                else
                {
                    int size = 0;
                    while (letter == words[i][pos[i]])
                    {
                        pos[i]++;
                        size++;
                    }
                    sizes.push_back(size);
                }
            }
            if (!isSol)
            {
                fprintf(g, "Case #%d: Fegla Won\n", t);
                break;
            }
            int sum = 0;
            for (int i = 0; i < N; ++i)
            {
                sum += sizes[i];
            }
            int med = sum / N;
            for (int i = 0; i < N; ++i)
            {
                rez = rez + abs(med - sizes[i]);
            }
            int nr = 0;
            for (int i = 0; i < N; ++i)
            {
                if (words[i][pos[i]] == '\n')
                {
                    nr++;
                }
            }
            if ((nr > 0) && (nr != N))
            {
                fprintf(g, "Case #%d: Fegla Won\n", t);
                break;
            }
            else if (nr == N)
            {
                fprintf(g, "Case #%d: %lld\n", t, rez);
                break;
            }
        }
    }
    
    fclose(f);
    fclose(g);
}


