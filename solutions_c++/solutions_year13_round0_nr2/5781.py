#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <windows.h>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <map>
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define FORD(i,j,k) for(int i=j; i>=k; i--)
#define sc(a) int a; scanf(" %d", &a)
#define sca(a) scanf(" %d", &a)
#define pr(a) printf("%d", a)
#define prll(a) printf("%lld", a)
#define prn printf("\n")
#define pro printf(" ")
using namespace std;

void zadanie(int qq)
{
    sc(n);
    sc(m);
    bool wyn=1;
    int tab[100][100];
    FOR(i,0,n)
        FOR(j,0,m)
            sca(tab[i][j]);
    FOR(i,0,n){
        if (!wyn) break;
        int maq=0;
        FOR(j,0,m) if(tab[i][j]>maq) maq=tab[i][j];
        FOR(j,0,m) if(tab[i][j]<maq){
            FOR(k,0,n) if (tab[k][j]>tab[i][j]){wyn=0;break;} 
            }
        }
    if (wyn) printf("Case #%d: YES\n", qq); else printf("Case #%d: NO\n", qq);
    return;           
	}
	
int main()
{
	sc(p);
	for (int i=1;i<=p;i++)
		{zadanie(i);}
	//system("pause");
    return 0;
	}
