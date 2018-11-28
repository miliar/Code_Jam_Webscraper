/**
 * @file deceitful_war_large.cpp
 *
 * @breif Solving the 'Decietful War' problem - large data set
 */
#include <iostream>

#include <stdio.h>
#include <stdlib.h>

using namespace std;

// for qsort
int compare_doubles(const void* a, const void* b)
{
    double d1 = *(const double*) a;
    double d2 = *(const double*) b;
    if (d1 < d2) return -1;
    else if (d2 < d1) return 1;
    else return 0;
}

int main()
{
    const int kMaxBlocks = 1000;
    double Naomis[kMaxBlocks];
    double Kens[kMaxBlocks];
    int test_cases;
    cin >> test_cases;
    for (int t = 1; t <= test_cases; ++t) {
        int block_num;
        // read input
        cin >> block_num;
        double weight = 0.0;
        for (int i = 0; i < block_num; ++i) {
            cin >> weight;
            Naomis[i] = weight;
        }
        for (int i = 0; i < block_num; ++i) {
            cin >> weight;
            Kens[i] = weight;
        }
        // doing
        // sort first
        qsort((void *)Naomis, block_num, sizeof(double), compare_doubles);
        qsort((void *)Kens, block_num, sizeof(double), compare_doubles);
        // counting
        int deceitful_opt = 0;  // Naomi's score when playing Decietful War
        int n = 0;  // index for Naomis
        int k = 0;  // index for Kens
        while (k < block_num) {  // count all pairs that Naomi could deceit and win
            while (n < block_num && Naomis[n] < Kens[k]) n++;
            if (n == block_num) break;
            deceitful_opt++;
            k++; n++;
        }
        int opt = block_num;  // Naomi's score when playing War
                              // that Naomi knows all the weights does not
                              // affect the final score
        n = k = block_num - 1;
        while (k >= 0) {  // count all pairs that Ken could win
            while (n >= 0 && Kens[k] < Naomis[n]) n--;
            if (n < 0) break;
            opt--;
            k--; n--;
        }
        // output
        printf("Case #%d: %d %d\n", t, deceitful_opt, opt);
    }
}
