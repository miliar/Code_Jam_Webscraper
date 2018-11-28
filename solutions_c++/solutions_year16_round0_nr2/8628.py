#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>

#define LL8 100000000

using namespace std;

int TN, TC;
int size;
char line[101];

int solve(char *line, int start, int end, int dir, char pos, char neg)
{
    while (start != end && line[start] == pos)
        start += dir;
    
    if (start == end)
        return (line[end] == neg);
    
    if (line[end] == neg) {
        return solve(line, end, start, -dir, neg, pos) + 1;
    }
    else {
        while (line[end] == pos)
            end -= dir;
        
        return solve(line, end, start, -dir, neg, pos) + 2;
    }
}

int main()
{
    scanf("%d", &TN);
    for (TC=1; TC<=TN; TC++) {
        scanf("%s", line);
        int len = (int)strlen(line);
        printf("Case #%d: %d\n", TC, solve(line, len-1, 0, -1, '+', '-'));
    }
    
    return 0;
}