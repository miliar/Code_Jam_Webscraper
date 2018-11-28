#include <iostream>
#include <cstdio>
using namespace std;

const int INF = 1000000000;

int A, N;

int motes[1024];

int solve()
{
    sort(motes, motes + N);
    
    if (A == 1) return N;
    
    int ans = INF;
    
    int curSize = A;
    int curOper = 0;
    for (int i = 0; i < N; i++)
    {
        ans = min(ans, curOper + (N - i));
        
        if (motes[i] < curSize) 
        {
            curSize += motes[i];         
            continue;
        }
        
        while (curSize <= motes[i])
        {
            curSize += curSize - 1;
            curOper++;  
        }
        
        curSize += motes[i];
    }
    
    ans = min(ans, curOper);
    
    return ans; 
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> A >> N;
        for (int i = 0; i < N; i++)
            cin >> motes[i];
        
        printf("Case #%d: %d\n", t, solve());
    }
    
    return 0;
}
