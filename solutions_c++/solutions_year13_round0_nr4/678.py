#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>

#define F(A, B) for(A=0;A<B;A++)
#define Fo(A, B) for(A=1;A<=B;A++)

using namespace std;

int seqb[201];

int montar(int n, int q)
{
    int i;
    int tot=(1<<n);
    F(i, q)
    {
        tot+=(1<<seqb[i]);
    }
    return tot;
}

int main()
{
    int t, disp[201], q, ca, tipo[201], n, k, l, w, passou[201], i, j;
    int *estados = new int[2100000];
    vector<int> v[201];
    scanf("%i", &t);
    Fo(i, t)
    {
        estados = new int[2100000];
        scanf("%i %i", &k, &n);
        q=0;
        F(j,201)
        {
            disp[j] = 0;
        }
        F(j,k)
        {
            scanf("%i", &ca);
            disp[ca]++;
        }
        Fo(j,n)
        {
            v[j].clear();
            passou[j] = 0;
            scanf("%i", &ca);
            tipo[j] = ca;
            scanf("%i", &ca);
            F(l, ca)
            {
                scanf("%i", &w);
                v[j].push_back(w);
            }
        }
        int possivel = 1;
        while(possivel>0)
        {
            int entrou = 0;
            /*printf("Passou - %i\n", possivel);
            Fo(j, n)
            {
                printf("%i - %i - %i\n", j, passou[j], disp[tipo[j]]);
            }
            system("PAUSE");*/
            for(j=possivel;j<=n;j++)
            {
                if(passou[j] == 0 && disp[tipo[j]]>0 && estados[montar(j, q)]==0)
                {
                    entrou = 1;
                    disp[tipo[j]]--;
                    seqb[q] = j;
                    passou[j] = 1;
                    estados[montar(j, q)]=1;
                    for(l=0;l<v[j].size();l++)
                    {
                        disp[v[j][l]]++;
                    }
                    q++;
                    break;
                }
            }
            if(entrou==0)
            {
                if(q!=n && q!=0)
                {
                    possivel = seqb[q-1]+1;
                    q--;
                    j = seqb[q];
                    disp[tipo[j]]++;
                    passou[j] = 0;
                    for(l=0;l<v[j].size();l++)
                    {
                        disp[v[j][l]]--;
                    }
                }
                else
                {
                    break;
                }
            }
            else
            {
                /*printf("Passou\n");
                Fo(j, n)
                {
                    printf("%i - %i\n", j, passou[j]);
                }
                printf("\n");*/
                possivel = 1;
            }
        }
        printf("Case #%i: ", i);
        if(q == 0)
        {
            printf("IMPOSSIBLE");
        }
        else
        {
            F(j, q)
            {
                printf("%i ", seqb[j]);
            }
        }
        printf("\n");
    }
    return 0;
}
