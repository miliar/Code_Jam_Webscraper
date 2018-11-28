#include <cstdio>
#include <string>
#include <queue>
using namespace std;
int scanString(string* s)
{
    char a[32768];
    int rt=scanf("%s", &a);
    (*s)=string(a);
    return rt;
}

int s;
int solve()
{
    scanf("%d", &s);
    string str; scanString(&str);

    queue<int> numbers;
    for(int i=0;i<str.size();i++)
    {
        for(char j='0';j<str[i];j++)
        {
            numbers.push(i);
        }
    }

    int standing=0;
    int newbs=0;

    while(!numbers.empty())
    {
        if(numbers.front()<=standing)
        {
            standing++;
            numbers.pop();
        }
        else
        {
            standing++;
            newbs++;
        }
    }
    return newbs;
}

int t;
int main()
{
    scanf("%d", &t);
    queue<int> out;
    for(int i=0;i<t;i++)
    {
        out.push(solve());
    }
    for(int i=1;!out.empty();i++)
    {
        printf("Case #%d: %d\n", i, out.front());
        out.pop();
    }
}
/*
4
4 11111
1 09
5 110011
0 1
*/
