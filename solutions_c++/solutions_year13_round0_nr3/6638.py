#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int N;

void solve_problem(int t_case)
{
    int A, B;
    int res = 0;
    cin >> A >> B;
    
    for(int i=A;i<=B;i++)
    {
        if(i == 1 || i == 4 || i == 9 || i == 121 || i == 484)
            res++;
    }
    cout << "Case #" << t_case << ": " << res << endl;
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    
    cin >> N;
    
    for(int i=0;i<N;i++)
    {
        solve_problem(i+1);
    }
}