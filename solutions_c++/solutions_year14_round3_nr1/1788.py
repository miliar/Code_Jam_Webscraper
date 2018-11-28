#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <sstream>
#include <utility>

using namespace std;

int solve();

int main()
{
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	int sol = solve();
       
	cout << "Case #" << i << ": ";
	if(sol == -1)
	{
	    cout << "impossible" << endl;
	}
	else 
	{
	    cout << sol << endl;
	}
    }

    return 0;
}

int gcd(int a, int b) 
{
    if(b == 0)
    {
	return a;
    }
    else
    {
	return gcd(b, a % b);
    }
}


pair<int,int> substract(pair<int,int> A, pair<int,int> B)
{
    int div = gcd(A.second, B.second);

    A.first *= (B.second/div);
    A.second *= (B.second/div);

    B.first *= (A.second/div);
    B.second *= (A.second/div);

    return pair<int,int>(A.first - B.first, B.second);
}

int solve()
{
    int P,Q;
    char ignore;
    cin >> P >> ignore >> Q;
    
    int Qc = Q;

    while(Qc % 2 == 0)
    {
	Qc /= 2;
    }
    if(gcd(Qc, P) != Qc)
    {
	return -1;
    }

    int count = 1;

    pair<int,int> pq(P,Q);
    while(true)
    {
	pair<int,int> res = substract(pq, pair<int,int>(1, (1<<count)));
	if(res.first >= 0)
	{
	    return count;
	}
	count++;
    }

    return count;
}
