#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<string> StrVector;
typedef vector<int> IntVector;


int solve2(string &s1, string &s2)
{
    int R = 0;
    //printf("%s - %s\n", s1.c_str(), s2.c_str());
    for (int i = 0; i < s1.size();) 
    {    

        if (s1.compare(s2) == 0)
            return R;

        //printf("[%d] %s - %s, %d\n", i, s1.c_str(), s2.c_str(), R);
        
        char c = s1[i];
        int n = 1;
        for (; c == s1[i + n]; n++);
        char c2 = s2[i];
        int n2 = 1;
        for (; c2 == s2[i + n2]; n2++);
        //printf("%c (%d) - %c (%d)\n", c, n, c2, n2);

        if (c != c2)
            return -1;
        if (n == n2)
            continue;
        int d = 0;
        if (n > n2) 
        {
            d = n - n2;
            s1.erase(i + n2, d);
        }
        else
        {
            d = n2 - n;
            s1.insert(i + n, d, c2);

        }
        R += d;
        i = i + n2;

    }
    return s1.compare(s2) == 0 ? R : -1;
}

void processCase(int n)
{
    
    int N;
    cin >> N;
    string s1, s2;
    cin >> s1;
    cin >> s2;

    int r = solve2(s1, s2);
            
    printf("Case #%d: ", n);
    if (r == -1)
        printf("Fegla Won");
    else
        printf("%d", r);
    printf("\n");
}            


int main(int argc, char **argv)
{
   int N = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        processCase(i + 1);

    return 0;
}