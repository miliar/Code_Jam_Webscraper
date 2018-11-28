#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;
int n;
char s[250][250];
int f[250][250];
int ind[250];
int nr;

void cit()
{
    scanf("%d\n", &n);
    for (int i=0; i<n; i++)
        scanf("%s\n", &s[i]);
}

void formare()
{
    char aux;
    for (int i=0; i<n; i++)
        for (int j=0; j<strlen(s[i]); j++)
        {
            aux=s[i][j];
            f[i][++f[i][0]]++;
            while (s[i][++j]==aux)
                f[i][f[i][0]]++;
            j--;
        }
}

int verif()
{
    char aux;
    int num;
    for (int i=0; i<n; i++)
        if (f[0][0]!=f[i][0])
            return 0;
    for (int j=0; j<f[0][0]; j++)
    {
        aux=s[0][ind[0]];
        for (int i=0; i<n; i++)
        {
            num=0;
            while (s[i][ind[i]]==aux)
            {
                num++;
                ind[i]++;
            }
            if (num==0)
                return 0;
        }
    }
    return 1;
}

void sol()
{
    formare();
    if (!verif())
    {
        printf("Fegla Won");
        return;
    }
    nr=0;
    double m;
    int medie;
    int dif;
    for (int j=1; j<=f[0][0]; j++)
    {
        m=0;
        for (int i=0; i<n; i++)
            m+=f[i][j];
        medie=round(m/(n*1.0));
        for (int i=0; i<n; i++)
        {
            dif=abs(medie-f[i][j]);
            nr+=dif;
        }
    }
    printf("%d", nr);
}

void reset()
{
    for (int i=0; i<200; i++)
        for (int j=0; j<200; j++)
            f[i][j]=0;
    for (int i=0; i<200; i++)
        ind[i]=0;
    for (int i=0; i<200; i++)
        for (int j=0; j<200; j++)
            s[i][j]=0;
}

int main()
{
    freopen("rep.in", "r", stdin);
    freopen("rep.out", "w", stdout);
    int T;
    scanf("%d\n", &T);
    for (int r=1; r<=T; r++)
    {
        printf("Case #%d: ", r);
        reset();
        cit();
        sol();
        printf("\n");
    }
    return 0;
}
