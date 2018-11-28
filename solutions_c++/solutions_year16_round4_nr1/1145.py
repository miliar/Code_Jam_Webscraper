#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef vector<int> data;

data solve(int n, int w)
{
    data ans(3, 0);
    
    if( n==0 )
        ans[w]=1;
    else
    {
        data l=solve(n-1, w);
        data r=solve(n-1, (w+2)%3);
        
        for(int i=0; i<3; i++)
            ans[i]=l[i]+r[i];
    }
    
    return ans;
}

string print(int n, int w)
{
    static const char* s="RPS";
    
    if( n==0 )
        return string(1, s[w]);
    else
    {
        string l=print(n-1, w);
        string r=print(n-1, (w+2)%3);
        return min(l, r)+max(l, r);
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    
    for(int cases=1; cases<=N; cases++)
    {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans="ZZZ";
        
        for(int i=0; i<3; i++)
        {
            data tmp=solve(n, i);
            
            if( r==tmp[0] && p==tmp[1] && s==tmp[2] )
                ans=min(ans, print(n, i));
        }
        
        if( ans=="ZZZ" )
            ans="IMPOSSIBLE";
        
        printf("Case #%d: %s\n", cases, ans.c_str());
    }
}