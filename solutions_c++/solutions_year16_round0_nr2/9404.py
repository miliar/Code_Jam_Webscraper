#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<char> pan;

void virar()
{
    for(int i=0; i<pan.size(); i++)
    {
        if(pan[i] == '+')
        pan[i] = '-';
        else
        pan[i] = '+';
    }
}
int main()
{
    int n, m, i, j, cont;
    string s;
    scanf("%d", &m);
    for(i=0;i<m;i++)
    {
            cont = 0;
            cin>>s;
            for(j=0;j<s.size();j++)
            {
                pan.push_back(s[j]);
            }

        while(!pan.empty())
        {
            if(pan.back() == '-')
            {
                virar();
                cont ++;
            }
            pan.pop_back();
        }
        pan.clear();
        printf("Case #%d: %d\n", i+1,cont);

    }
    return 0;
}
