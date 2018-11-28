/*
* @Author: Comzyh
* @Date:   2016-05-28 22:00:13
* @Last Modified by:   Comzyh
* @Last Modified time: 2016-05-28 23:01:43
*/

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
//
char ans[1 << 12];
struct Seq
{
    char str[1 << 12];
    int index;
    Seq()
    {
        index = 0;
    }
    void push(char c)
    {
        str[index++] = c;
    }
};
Seq SP, SR, SS;
void dfs(Seq &s, char c, int deep)
{
    if (!deep)
    {
        s.push(c);
        return;
    }
    if (c == 'P')
    {
        dfs(s, 'P', deep - 1);
        dfs(s, 'R', deep - 1);
    }
    if (c == 'R')
    {
        dfs(s, 'R', deep - 1);
        dfs(s, 'S', deep - 1);
    }
    if (c == 'S')
    {
        dfs(s, 'S', deep - 1);
        dfs(s, 'P', deep - 1);
    }
}
void outputdfs(char c, int deep)
{
    if (!deep)
    {
        putchar(c);
        return;
    }
    if (c == 'P')
    {
        outputdfs('P', deep - 1);
        outputdfs('R', deep - 1);
    }
    if (c == 'R')
    {
        outputdfs('R', deep - 1);
        outputdfs('S', deep - 1);
    }
    if (c == 'S')
    {
        outputdfs('P', deep - 1);
        outputdfs('S', deep - 1);
    }
}
int T, N, R, P, S;
char gotwin(const char *str, int index, int deep)
{
    if (!deep)
        return str[index];
    char a = gotwin(str, index * 2, deep - 1);
    char b = gotwin(str, index * 2 + 1, deep - 1);
    if (a == 'R' && b == 'S' || a == 'S' && b == 'R')
        return 'R';
    if (a == 'S' && b == 'P' || a == 'P' && b == 'S')
        return 'S';
    if (a == 'P' && b == 'R' || a == 'R' && b == 'P')
        return 'P';
}
void sort(char *str, int deep)
{
    if (!deep)
        return ;
    int half = 1 << (deep - 1);
    sort(str, deep - 1);
    sort(str + half, deep - 1);
    if (strcmp(str, str + half) > 0)
        for (int i = 0; i < half; i ++)
            swap(str[i], str[half + i]);
}
bool test(Seq &s)
{
    int nR = 0, nP = 0, nS = 0;
    for (int i = 0; i < 1 << N; i++)
    {
        if (s.str[i] == 'P')
            nP ++;
        if (s.str[i] == 'R')
            nR ++;
        if (s.str[i] == 'S')
            nS ++;
    }
    if (nP == P && nR == R && nS == S)
    {
        memcpy(ans, s.str, sizeof(char) * (1 << N));
        sort(ans, N);
        for (int i = 0; i < 1 << N; i ++)
            putchar(ans[i]);
        return true;
    }
    return false;
}
int main()
{
    dfs(SP, 'P', 12);
    dfs(SR, 'R', 12);
    dfs(SS, 'S', 12);
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        scanf("%d", &N);
        scanf("%d%d%d", &R, &P, &S);
        printf("Case #%d: ", TT);
        bool answer = test(SP) || test(SR) || test(SS);
        if (!answer)
            printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}