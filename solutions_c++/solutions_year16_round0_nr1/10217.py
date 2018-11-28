/*************************************************************************
    > File Name: a.cpp
    > Author: Guo Hengkai
    > Description: 
    > Created Time: Sat 09 Apr 2016 10:45:34 AM CST
 ************************************************************************/
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    FILE* in_file = fopen("a.in", "r");
    FILE* out_file = fopen("a.out", "w");

    int T;
    fscanf(in_file, "%d", &T);

    long long N;
    for (int i = 1; i <= T; ++i)
    {
        fprintf(out_file, "Case #%d: ", i);
        fscanf(in_file, "%lld", &N);
        if (N == 0)
        {
            fprintf(out_file, "INSOMNIA\n");
            continue;
        }

        int ans = 0;
        long long cnt = 0;
        int total = 0;
        bool flag = false;
        vector<bool> hash(10, false);
        while (!flag)
        {
            ++ans;
            cnt += N;
            long long temp = cnt;
            while (temp)
            {
                int num = temp % 10L;
                if (!hash[num])
                {
                    hash[num] = true;
                    ++total;
                    if (total >= 10)
                    {
                        flag = true;
                        break;
                    }
                }
                temp /= 10L;
            }
        }
        fprintf(out_file, "%lld\n", cnt);
    }

    fclose(in_file);
    fclose(out_file);
    return 0;
}
