/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: mate
 *
 * Created on April 9, 2016, 6:16 PM
 */

#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    int T = 0;
    scanf ("%d", &T);
    fprintf (stderr, "Doing %d testcases", T);
    
    for (int t = 0; t < T; ++t)
    {
        int N = 0;
        scanf("%d", &N);
        
        if (N == 0)
        {
            printf ("Case #%d: INSOMNIA\n", t+1);
        } else {
            unsigned int digits = 0;
            int i = 1;
            while (1)
            {
                int iN = i*N;
                if (iN < N)
                {
                    fprintf (stderr, "ERROR, overflow\n");
                    return 0;
                }
                while (iN > 0)
                {
                    digits |= 1 << (iN%10);
                    iN /=10;
                }
                if (digits == 0x03ff)
                {
                    fprintf (stderr, "%d: i=%d, iN=%d\n", N, i, i*N);
                    printf ("Case #%d: %d\n", t+1, i*N);
                    break;
                }
                ++i;
            }
        }
    }
    
/*    
    for (int N = 1; N <= 1000000; ++N)
    {
        unsigned int digits = 0;
        int i = 1;
        while (1)
        {
            int iN = i*N;
            if (iN < N)
            {
                printf ("ERROR, overflow\n");
                return 0;
            }
            while (iN > 0)
            {
                digits |= 1 << (iN%10);
                iN /=10;
            }
            if (digits == 0x03ff)
            {
                printf ("%d: i=%d, iN=%d\n", N, i, i*N);
                break;
            }
            ++i;
        }
        
    }
*/    
    return 0;
}

