#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>

using namespace std;

ifstream fin("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.in");
//ofstream fout("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out");
FILE *fout;

unsigned long long A,B,K;
unsigned long long ans;

int bits[3][100];
int len[3];

void trans_to_binary(unsigned long long num, int tag)
{
    len[tag]=0;
    for (int i=0; i<100; i++)
        bits[tag][i] = 0;
    while (num>0)
    {
        bits[tag][len[tag]] = num % 2;
        num /=2;
        len[tag]++;
    }
}

int main()
{
    fout = fopen("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out", "w");
    int t;
    fin>>t;
    int i,j,k,p,r;
    int N;
    unsigned long long states[2][2][2], states_new[2][2][2];
    int max_va, max_vb, max_vk;
    int temp_a,temp_b,temp_k;
    int tag_a, tag_b, tag_k;
    
    for (i=1; i<=t; i++)
    {
        fin>>A>>B>>K;
        if (K>=A && K>=B)
        {
            ans = A*B;
        }
        else
        {
            trans_to_binary(A,0);
            trans_to_binary(B,1);
            trans_to_binary(K,2);
            for (j=0;j<2;j++)
                for (k=0;k<2;k++)
                    for (p=0;p<2;p++)
                    {
                        states[j][k][p] = 0;
                    }
            states[0][0][0] = 1;
            if (len[0]>len[1]) N = len[0]; else N = len[1];
            for (r=0; r<N; r++)
            {
                for (j=0;j<2;j++)
                {
                    max_va = (j>0)? bits[0][r] : 2;
                    
                    for (k=0;k<2;k++)
                    {
                        max_vb = (k>0)? bits[1][r] : 2;
                        for (p=0;p<2;p++)
                        {
                            max_vk = (p>0)? bits[2][r] : 2;
                            states_new[j][k][p] = 0;
                            for (temp_a=0; temp_a<2; temp_a++)
                                for (temp_b=0; temp_b<2; temp_b++)
                                {
                                    temp_k = temp_a & temp_b;
                                    if (temp_a>max_va || temp_b>max_vb || temp_k>max_vk) continue;
                                    tag_a = (temp_a == max_va);
                                    tag_b = (temp_b == max_vb);
                                    tag_k = (temp_k == max_vk);
                                    states_new[j][k][p] += states[tag_a][tag_b][tag_k];
                                }
                        }
                    }
                }
                for (j=0; j<2; j++)
                    for (k=0; k<2; k++)
                        for (p=0; p<2; p++)
                            states[j][k][p] = states_new[j][k][p];
            }
            ans = states[1][1][1];
        }
        fprintf(fout,"Case #%d: %llu\n",i, ans);
    }
    fclose(fout);
    return 0;
}