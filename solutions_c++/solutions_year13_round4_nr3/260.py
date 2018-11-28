#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;
typedef long long ll;
const int MAXN = 2100;

int N;
int xinc[MAXN];
int xdec[MAXN];

int ans[MAXN];
bool use[MAXN];
bool found;

ifstream fin ("C.in");
ofstream fout ("C.out");

void solve (int cval)
{
    if (found) return;
    
    if (cval == N)
    {
        for (int i = N - 2; i >= 0; i--)
        {
            int bval = 1;
            for (int j = i + 1; j < N; j++)
                if (ans[i] > ans[j])
                    bval = max (bval, xdec[j] + 1);
            if (bval != xdec[i])
                return;
        }
        
        found = true;
        return;
    }
    
    for (int i = 1; i <= N; i++)
    {
        if (!use[i])
        {
            int bval = 1;
            for (int j = 0; j < cval; j++)
                if (ans[j] < i)
                    bval = max (bval, xinc[j] + 1);
            if (bval != xinc[cval])
                continue;
            
            use[i] = true;
            ans[cval] = i;
            solve (cval+1);
            
            if (found) return;
            use[i] = false;
        }
    }
}

int main()
{
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
    for (int i = 0; i < MAXN; i++)
        use[i] = false;
    found = false;
    
    fout << "Case #" << test + 1 << ": ";
    
    fin >> N;
    for (int i = 0; i < N; i++)
        fin >> xinc[i];
    for (int i = 0; i < N; i++)
        fin >> xdec[i];
    
    solve (0);
	
	for (int i = 0; i < N; i++)
	{
		if (i) fout << " ";
	    fout << ans[i];
	}
	fout << "\n";
	
	}
	return 0;
}
