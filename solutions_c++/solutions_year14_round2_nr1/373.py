#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxN = 102;
const int maxL = 102;
ifstream fin("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.in");
//ofstream fout("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out");
FILE *fout;


typedef struct
{
    char letter;
    int num;
} T1;

T1 skel[maxL][maxN];
int skel_len[maxN];


bool myComp(const T1& a, const T1& b)
{
    return a.num<b.num;
}

int main()
{
    fout = fopen("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out", "w");
    int t;
    fin>>t;
    int i,j,k;
    for (i=1; i<=t; i++)
    {
        int n;
        string temp;
        
        fin>>n;
        for (j=0; j<n; j++)
        {
            fin>>temp;
            skel_len[j] = 1;
            skel[0][j].letter = temp[0];
            skel[0][j].num = 1;
            for (k=1; k<temp.length(); k++)
            {
                if (temp[k] == temp[k-1])
                {
                    skel[skel_len[j]-1][j].num++;
                } else
                {
                    skel[skel_len[j]][j].letter = temp[k];
                    skel[skel_len[j]][j].num = 1;
                    skel_len[j]++;
                }
            }
        }
        
        fprintf(fout, "Case #%d: ", i);
        int has_ans = 1;
        for (j=1; j<n; j++)
        {
            if (skel_len[j]!=skel_len[0])
            {
                has_ans = 0;
                break;
            }
            
            for (k=0; k<skel_len[0]; k++)
            {
                if (skel[k][j].letter != skel[k][0].letter)
                {
                    has_ans = 0;
                    break;
                }
            }
            if (has_ans == 0) break;
        }
        
        if (has_ans == 0)
        {
            fprintf(fout, "Fegla Won\n");
            continue;
        }
        
        int ans = 0;
        int mid = (n+1)/2-1;
        int cur_v;
        
        for (k=0; k<skel_len[0]; k++)
        {
            sort(skel[k], skel[k]+n, myComp);
            cur_v = skel[k][mid].num;
            for (j=0; j<n; j++)
                ans += abs(skel[k][j].num-cur_v);
        }
        fprintf(fout, "%d\n", ans);
    }
    
    fclose(fout);
    return 0;
}