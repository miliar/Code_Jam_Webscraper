#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    int t,i,j,k;
    scanf("%d",&t);
    getchar();
    for(i=0;i<t;i++)
    {
        string s;
        getline(cin,s);
        int length = s.length();
        int seg = 1;
        for(j=1;j<length;j++)
        {
            if(s[j]!=s[j-1])
            {
                seg++;
            }
        }
        if(s[length-1]=='+')
        {
            seg--;
        }
        printf("Case #%d: %d\n",i+1,seg);
    }
}
