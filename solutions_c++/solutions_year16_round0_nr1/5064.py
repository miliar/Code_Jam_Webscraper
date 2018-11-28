#include<bits/stdc++.h>
#define INF 0x7fffffff

using namespace std;

int mat[(int)1e6+1][10];
int xpto[(int)1e6+1];


int qualONumero(int n, int initial, int i)
{
    if(n<10)
    {
        int a = mat[i][n];
        mat[i][n] = min(mat[i][n], initial) ;
        xpto[i]+= mat[i][n] != a;
        return n;
    }

    int x = n - qualONumero(n/10, initial, i) * 10;
    int a = mat[i][x];

    mat[i][x] = min(mat[i][x],  initial);
    xpto[i]+= a != mat[i][x];
    return n;
}

string toString(int n)
{
    stringstream ss;
    ss << n;
    string x;
    ss >> x;

    return x;

}

bool have(int n, int k)
{
    string str = toString(n);
    return count(str.begin(), str.end(), k+'0');
}

int main()
{
    for(int i=0; i<(int)1e6+1; i++ )
        for(int j=0;j<10; j++)
                mat[i][j] = INF;


    for(int i=0; i<(int)1e6+1; i++ )
    {
        for(int j=1;j<1000; j++)
        {
            if(xpto[i] < 10)
            qualONumero(i*j,i*j, i);
        }
    }


    int t;
    int cases =1;
    while(scanf("%d", &t)!=EOF)
    {
        while(t--)
        {
            printf("Case #%d: ", cases++);
            int hi = -INF;
            int x; scanf("%d", &x);

            for(int i=0; i<10; i++)
            {
                hi = max(hi, mat[x][i]);
            }

            if(hi == INF) printf("INSOMNIA\n");
            else printf("%d\n", hi);
        }
    }
    return 0;
}
