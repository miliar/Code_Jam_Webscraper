#include <cstdio>
#include <algorithm>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, n;
char cad[1004];


int main()
{
    FILE  *f;
    f = fopen("asas.txt", "w");
    cin >> t;
    for(int c = 1; c <=t; c++)
    {
        cin >> n >> cad;
        n++;
        int sol = 0;
        int aux = 0;
        for(int i = 0; i < n; i++)
        {
            if(cad[i]=='0')continue;
            if(i==0)
            {
                aux+=cad[i]-48;
            }else{
                if(aux>=i)
                {
                    aux+=cad[i]-48;
                }else{
                    sol+=i-aux;
                    aux+=i+cad[i]-48;
                }
            }
        }
        fprintf(f, "Case #%d: %d\n", c,sol);
    }
    fclose(f);


    return 0;
}





