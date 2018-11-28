#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <sstream>

using namespace std;
int dig[10]={0};
int num = 10;

long long solve(string s){
    long long cot = 0;

    int cur = -1;

    if(s[0]=='+')
        cur = 1;

    for(int i = 1; i< s.size(); i++)
    {
        if (s[i] == '+')
        {
            if (cur == -1)
            {
                cot++;
                cur = 1;
            }
        }
        else
        {
            if (cur ==1)
            {
                cot++;
                cur = -1;
            }
        }
    }

    if (cur == -1)
        cot++;

    return cot;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    long long t;
    cin>> t;
    for(long long i = 1; i<=t; i++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<i<<":"<<" "<<solve(s)<<endl;
    }
    return 0;
}
