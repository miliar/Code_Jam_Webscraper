/* 
 * File:   main.cpp
 * Author: kapil
 *
 * Created on 11 April, 2015, 10:32 PM
 */

#include <cstdlib>
#include <cassert>
#include <cstdio>
#include <cstring>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T, S_max;
    char dist[1007];
    scanf("%d", &T);
    for(int case_no = 1; case_no<=T; case_no++)
    {
        scanf("%d %s", &S_max, dist);
        
        assert(strlen(dist) == S_max+1);
        long long sum = 0, ans = 0, extra = 0;
        for(int shyness=0; shyness<=S_max; shyness++)
        {
            extra = 0;
            if(shyness>sum)
                extra = shyness - sum;
            sum += (dist[shyness] - '0') + extra;
            ans += extra;
        }
        printf("Case #%d: %d\n", case_no, ans);
    }
    return 0;
}

