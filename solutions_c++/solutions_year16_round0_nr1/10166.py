#include <bits/stdc++.h>

using namespace std;

long long vec[12];

void initVec()
{
    for(int x=0; x<12; x++)
    {
        vec[x] = 0;
    }
}

bool isChecked()
{
    for(int x=0; x<10; x++)
        if(!vec[x])
            return false;

    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int casos, index;
    long long n,tmp, ans;

    scanf("%d", &casos);

    for(int x=1; x<=casos; x++)
    {
        cin>>n;

        if(!n)
        {
            printf("Case #%d: INSOMNIA\n", x);
        }
        else
        {
            initVec();
            index = 0;

            while(1)
            {
                index++;
                tmp =n* index;
                ans = tmp;

                while(tmp)
                {
                    vec[tmp%10] = 1;
                    tmp/=10;
                }
                if(isChecked())
                {
                    cout<<"Case #"<<x<<": "<<ans<<"\n";
                    break;
                }
            }
        }
    }

return 0;
}
