#include <bits/stdc++.h>

using namespace std;

int T,N,J,mycount = 0,limit;
vector<int> ans;

bool judge_prime( int& k, vector<bool>& v, vector<int>& ans)
{
    int residue = 1, sum = 0;
    for(int i = N-1; i>=0; --i)
    {
        if( v[i] ) sum += residue, sum = sum%2;
        residue = (residue*k)%2;
    }
    if( !sum ) { ans.push_back(2); return false; }
    for(int n = 3; n<=10000;  n += 2 )
    {
        int residue = 1, sum = 0;
        for(int i = N-1; i>=0; --i)
        {
            if( v[i] ) sum += residue, sum = sum%n;
            residue = (residue*k)%n;
        }
        if( !sum ) { ans.push_back(n); return false; }
    }
    return true;
}
int main()
{
    scanf("%d%d%d",&T,&N,&J);
    vector<bool> check(N,false);
    limit = (1<<(N-1));
    check[0] = check[N-1] = true;
    printf("Case #1:\n");
    while( mycount<J )
    {
        bool is_prime = false;
        for(int i = 2; i<=10; ++i)
        {
            if( judge_prime(i,check,ans) ) { is_prime = true; break; }
        }
        if( !is_prime )
        {
            for(int i = 0; i<N; ++i)
                printf("%d", (int)check[i]);
            for(int i = 0; i<9; ++i)
                printf(" %d", ans[i]);
            printf("\n");
            ++mycount;
        }
        ans.clear();
        ans.resize(0);
        for(int i = N-2; i>=1; --i)
            if( !check[i] )
            {
                check[i] = true;
                for(int j = i+1; j<N-1; ++j)
                    check[j] = false;
                break;
            }
    }
}



