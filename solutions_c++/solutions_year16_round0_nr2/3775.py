#include <bits/stdc++.h>
using namespace std;
char line[200];
int main()
{
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        gets(line);
        int n = strlen(line);
        int cont = 1;
        for(int i = 0; i<n-1; i++)
        {
            if(line[i]!=line[i+1]) cont++;
        }
        int solution = 0;
        if(cont==1)
        {
            if(line[0]=='+') solution = 0;
            else solution = 1;
        }
        else
        {
            if(line[n-1]=='+') cont--;
            solution = cont;
        }
        printf("Case #%d: %d\n", t, solution);
    }
}
/*
bitset<2000> visited;
long long solution[2000];
int n;


int main()
{
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        gets(line);
        n = strlen(line);
        int cont = 1;
        for(int i = 0; i<n-1; i++)
        {
            if(line[i]!=line[i+1]) cont++;
        }
        int solution = 0;
        if(cont==1)
        {
            if(line[0]=='+') solution = 0;
            else solution = 1;
        }
        else
        {
            if(line[n-1]=='+') cont--;
        }
        printf("Case #%d: %d\n", t, cont);
    }
}*/
