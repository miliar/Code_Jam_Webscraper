#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <locale>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <climits>
#include <cfloat>
#include <map>
#include <functional>
using namespace std;
const double PI = acos(0.0) * 2.0;

FILE* output;
int car_N, idxArr[10];
char car[10][105];

int main() // Google Code Jam 2014 Round 1C
{
    output = fopen("myOutput.txt", "w");

    int tc_N;
    scanf("%d", &tc_N);

    for(int tc=1; tc<=tc_N; tc++)
    {
        int ans = 0;
        for(int i=0; i<10; i++) idxArr[i] = i; // 초기화

        scanf("%d", &car_N);

        for(int i=0; i<car_N; i++) scanf("%s", car[i]);

        do
        {
            bool valid = true, abt[26] = {false,}; // 알파벳 각각 한번이라도 들어왔는지
            char totString[10005] = {0};

            for(int i=0; i<car_N; i++) strcat(totString, car[idxArr[i]]);
            
            int sz = strlen(totString);
            char nowCh = '0';

            for(int i=0; i<sz; i++)
                if(totString[i] != nowCh) // 새로운 char 들어옴
                {
                    if(abt[totString[i]-'a']) // 이미 들어온 적이 있는 char
                    {
                        valid = false;
                        break;
                    }

                    nowCh = totString[i]; // 바꿔주고
                    abt[nowCh-'a'] = true;
                }

            if(valid) ans++;
        }
        while(next_permutation(idxArr, idxArr+car_N));

        fprintf(output, "Case #%d: %d\n", tc, ans);
    }

    fclose(output);

    return 0;
}