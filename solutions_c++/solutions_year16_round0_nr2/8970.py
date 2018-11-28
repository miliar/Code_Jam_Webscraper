#include<bits/stdc++.h>
using namespace std;

#define ll long long int
#define pb push_back
#define sf scanf
#define pf printf
#define F first
#define S second
#define M 105
#define MOD 1e9+7

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int test, loc, cnt, j;
    bool prove;
    string str;

    sf("%d", &test);
    for(int i=0; i<test; i++)
    {
        cin >> str;

        cnt=0;
        while(1)
        {
            prove=true;
            for(j=str.size()-1; j>=0; j--)
            {
                if(str[j]=='-')
                {
                    prove=false;
                    cnt++;
                    for( ;j>=0; j--)
                    {
                        if(str[j]=='-')
                        {
                            str[j]='+';
                        }
                        else
                        {
                            str[j]='-';
                        }
                    }
                    break;
                }
            }

            if(prove)
            {
                break;
            }
        }

        pf("Case #%d: %d\n", i+1, cnt);
    }
    return 0;
}
