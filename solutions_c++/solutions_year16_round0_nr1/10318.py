#include <iostream>
#include <stdio.h>
using namespace std;

bool num[11];

void pp(int tmp)
{
    int n = tmp;
    while(n)
    {
        num[n%10]=true;
        n/=10;
    }
}

bool check()
{
    for(int i=0;i<10;i++)
    {
        //printf("Now check num %d\n",i);
        if(!num[i]) return false;
    }
    return true;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("ProbA.txt","w",stdout);
    
    int n;
    int k=0;
    cin >> n;
    
    int t;
    int ans;
    
    while(k!=n)
    {
        k++;
        printf("Case #%d: ",k);
        
        for(int i=0;i<10;i++)
        {
            num[i] = false;
        }
        
        cin >> t;
        ans = 0;
        
        if(!t)
        {
            //printf("t is zero\n");
            cout << "INSOMNIA" <<endl;
            continue;
        }
        
        while(!check())
        {
            ans+=t;
            pp(ans);
        }
        
        cout << ans << endl;
    }
}