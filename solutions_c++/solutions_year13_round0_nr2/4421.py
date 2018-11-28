#include <iostream>
#include <string>

using namespace std;

const int MAX = 105, INF = 1e9;
int A[MAX][MAX];


void go (int t)
{
    printf ("Case #%d: ", t);
    int N, M;
    cin >> N >> M;
    for (int i=0; i<N; i++)
	for (int j=0; j<M; j++)
	    cin >> A[i][j];
    
    bool bad = false;
    for (int k=0; k<200; k++)
    {
	bool all = true;
	int lval = INF;
	for (int i=0; i<N; i++)
	    for (int j=0; j<M; j++)
		if (A[i][j] != -1)
		{
		    all = false;
		    lval = min (lval, A[i][j]);
		}
	if (all)
	    break;
	//cout << lval << "\n";
	bool ok = false;
	for (int i=0; i<N; i++)
	{
	    int lo = INF, hi = 0;
	    for (int j=0; j<M; j++)
	    {
		if (A[i][j] != -1)
		{
		    lo = min (lo, A[i][j]);
		    hi = max (hi, A[i][j]);
		}
	    }
	    //cout << lo << " "<< hi << " " << lval << "\n";
	    if (lo == hi and lo == lval)
	    {
		for (int j=0; j<M; j++)
		    A[i][j] = -1;
		ok = true;
	    }
	}
	for (int j=0; j<M; j++)
	{
	    int lo = INF, hi = 0;
	    for (int i=0; i<N; i++)
	    {
		if (A[i][j] != -1)
		{
		    lo = min (lo, A[i][j]);
		    hi = max (hi, A[i][j]);
		}
	    }
	    //cout << lo << " "<< hi << " " << lval << "\n";
	    if (lo == hi and lo == lval)
	    {
		for (int i=0; i<N; i++)
		    A[i][j] = -1;
		ok = true;
	    }
	}
	if (!ok)
	{
	    bad = true;
	    break;
	}
    }
    if (bad)
	printf ("NO\n");
    else
	printf ("YES\n");
}

int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++)
    {
	go (i + 1);
    }
}
