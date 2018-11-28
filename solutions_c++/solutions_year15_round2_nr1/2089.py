#include<bits/stdc++.h>

using namespace std;

vector < int > global;
const long long INF = 1e7;
int reversee(int n)
{
    int aux = 0;
    while(n != 0)
    {
        aux *= 10;
        aux += (n%10);
        n /=10;
    }
    return aux;
}

int backtrack(int pasos, int num , int objetivo)
{
    if(num == objetivo)
    {
        return pasos;
    }
    else if(num > objetivo)
    {
        return INF;
    }
    else
    {
        int res,res2;
        res = res2 = INF;
        if(global[num] == -1)
        {
            int a = reversee(num);
            if(a > num)
                res2 = backtrack(pasos+1,a,objetivo);
            res = backtrack(pasos+1,num+1,objetivo);
            global[num] = min(res,res2) - pasos;
        }
        return global[num] + pasos;
    }
}

int main()
{
    int casos;
    scanf("%d",&casos);
    for(int i = 0 ; i < casos ; i++)
    {
        int n;
        scanf("%d",&n);
        global.assign(n+1,-1);
        printf("Case #%d: %d\n",i+1,backtrack(0,1,n)+1);
    }
    return 0;
}
