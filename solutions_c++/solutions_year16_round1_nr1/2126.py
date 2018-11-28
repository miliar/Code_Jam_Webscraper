#include <stdio.h>
#include <deque>

int t;
char s[1010];
std :: deque <char> D;

int main()
{
    freopen("/Users/IohcEjnim/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/IohcEjnim/Downloads/result.txt", "w", stdout);
    int tn, i;
    
    scanf("%d", &t);
    
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%s", s);
        
        D.push_back(s[0]);
        for (i = 1; s[i]; i++)
        {
            if (s[i] >= D.front()) D.push_front(s[i]);
            else D.push_back(s[i]);
        }
        
        printf("Case #%d: ", tn);
        while (!D.empty())
        {
            printf("%c", D.front());
            D.pop_front();
        }
        puts("");
    }
}