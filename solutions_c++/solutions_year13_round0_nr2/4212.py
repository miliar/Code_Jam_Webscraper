#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>

using namespace std;



int main(void)
{
	unsigned long N;
	int I, J, i, j, p;
	int g[100][100], max[2][100];


	//unsigned long lRides, lSeats, nGroups, lEuros;
	//vector<int> vGroup;

	freopen("B-large.in", "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("prova.in", "rt", stdin);
	freopen("data.out", "wt", stdout);

	cin >> N;


	unsigned long n;
	for (n=1;n<=N;n++)
	{
        p=1;
        cin >> I >> J;
        for (i=0; i<I; i++)
            for (j=0; j<J; j++)
                cin >> g[i][j];

        for (i=0; i<I; i++)
            for (j=0; j<J; j++) if (g[i][j]>max[0][i]) max[0][i] = g[i][j];

        for (j=0; j<J; j++)
            for (i=0; i<I; i++) if (g[i][j]>max[1][j]) max[1][j] = g[i][j];

        for (i=0; i<I; i++)
            for (j=0; j<J; j++) if (g[i][j]<max[0][i] && g[i][j]<max[1][j]) p=0;



        cout << "Case #" << n;
        if (p) cout << ": YES"; else cout << ": NO";
        cout << endl;

        for (i=0; i<I; i++) max[0][i]=0;
        for (j=0; j<J; j++) max[1][j]=0;
   	}
}
