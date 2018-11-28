#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
bool isPalindrome(char arr[])
{
    int i, j;
    int len = strlen(arr);
    for(i=0; i<len/2; i++)
        if(arr[i]!=arr[len-i-1])
            return false;
    return true;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k, tCase=1, nCase;
    int n, m;
    char str[100], rootStr[100];
    cin >> nCase;
    while(nCase--)
    {
        scanf("%d %d", &n, &m);
        int cnt=0;
        for(i=n; i<=m; i++)
            {
                int s = sqrt(i);
                if(s*s==i)
                {
                    sprintf(str, "%d", i);
                    sprintf(rootStr, "%d", s);
                    if(isPalindrome(str) && isPalindrome(rootStr)) cnt++;
                }
            }
            printf("Case #%d: %d\n", tCase++, cnt);

    }
    return 0;
}


