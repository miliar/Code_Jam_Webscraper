#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define ull unsigned long long int
#define ll long long int
#define print_v(v, l)    for (ull i=0; i<l;i++) cout << v[i]; cout << endl;
#define print_pair(p) cout << "(" << p.first << ", " << p.second << ")" << endl;
#define sort_asc(v, b, e) sort(v+b, v+e);
#define sort_dsc(v, b, e) sort(v+b, v+e, std::greater<int>());
#define ssort_asc(v, b, e) stable_sort(v+b, v+e);
#define ssort_dsc(v, b, e) stable_sort(v+b, v+e, std::greater<int>());
#define DEBUG {cout << "DEBUG" << endl;exit(-1);}

#define DIM 4

char A[DIM][DIM];

char winner(int p)
{
	if(p==2*2*2*5 || p==2*2*2*2)
		return 'X';
	else if(p==3*3*3*5 || p==3*3*3*3)
		return 'O';
	else
		return 'N';
}

bool completed()
{
    for(int i=0; i < DIM; i++)
        for(int j=0; j < DIM; j++)
            if(A[i][j]=='.')
                return false;
    return true;
}

void who_won()
{
    int i, j;
	for(i=0; i < DIM; i++)
	{
        int prod_r=1;
		for(j=0; j < DIM; j++)
		{
			if(A[i][j]=='X')
				prod_r*=2;
			else if(A[i][j]=='O')
				prod_r*=3;
			else if(A[i][j]=='T')
				prod_r*=5;
		}
        //cout << "R: " << prod_r << endl;
		char w=winner(prod_r);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}

	for(i=0; i < DIM; i++)
	{
        int prod_c=1;
		for(j=0; j < DIM; j++)
		{
			if(A[j][i]=='X')
				prod_c*=2;
			else if(A[j][i]=='O')
				prod_c*=3;
			else if(A[j][i]=='T')
				prod_c*=5;
		}
        //cout << "C: " << prod_c << endl;
		char w=winner(prod_c);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}

    int prod_d=1;
	for(i=0; i < DIM; i++)
	{
		if(A[i][i]=='X')
			prod_d*=2;
		else if(A[i][i]=='O')
			prod_d*=3;
		else if(A[i][i]=='T')
			prod_d*=5;

        //cout << "D: " << prod_d << endl;
		char w=winner(prod_d);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}

    prod_d=1;
	for(i=0; i < DIM; i++)
	{
		if(A[i][DIM-1-i]=='X')
			prod_d*=2;
		else if(A[i][DIM-1-i]=='O')
			prod_d*=3;
		else if(A[i][DIM-1-i]=='T')
			prod_d*=5;

        //cout << "D: " << prod_d << endl;
		char w=winner(prod_d);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}


	if(completed())
	{
		cout << "Draw" << endl;
	}
	else
		cout << "Game has not completed" << endl;
}

int main (int argc, char *argv[])
{

    #ifdef DEBUGGING
      freopen("input.in","r",stdin);
      freopen("output.out","w",stdout);
    #endif

    int T;
    cin >> T;
    for(int i=0; i < T; i++)
    {
        for(int j=0; j < DIM; j++)
            for(int k=0; k < DIM; k++)
                cin >> A[j][k];

        cout << "Case #" << i+1 << ": ";
        who_won();
    }


    return 0;
}

