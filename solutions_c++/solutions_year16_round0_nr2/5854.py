#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;

bool hpy(string num)
{
    for(int i = 0; i < num.size(); ++i)
    {
        if(num[i] != '+')
            return false;
    }
    return true;
}
int main()
{
    int t;
    scanf("%d", &t);
    FILE * pFile;
    pFile = fopen ("ans.txt", "w");
    int x = 1;
    while(t--)
    {
        string a;
        cin >> a;
        int total = 0; 
        while(!hpy(a))
        {
            int beg = 0;
            int end = 0;
            char first = a[0];        
            for(int i = 1; i < a.size(); ++i)
            {
                if(a[i] == first)
                {
                    end++;
                }
                else
                    break;
            }
            for(int q = 0; q <= end;q++)
            {
                if(a[q] == '+')
                    a[q] = '-';
                else
                    a[q]= '+';
            }
            total++;
        }
        fprintf(pFile,"Case #%d: %d\n",x,total);
        x++;
    }
    return 0;
}

