#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
bool cakes[110];

void flip(int lastindx)
{
    bool tmp[110];
    for(int i=0; i<=lastindx; i++)
        tmp[i] = cakes[i];

    int indx = 0;
    for(int i=lastindx; i>=0; i--)
    {
        cakes[indx] = !tmp[i];
        indx++;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large_output.out", "w", stdout);
    int cases;
    string inp;

    cin>>cases;
    for(int ca=1; ca<=cases; ca++)
    {
        int cnt = 0;
        cin>>inp;
        for(int i=0; i<inp.size(); i++)
            cakes[i] = (inp[i] == '+' ? 1 : 0);

        int indx = inp.size() - 1;
        while(indx>=0 && cakes[indx]==1)
            indx--;

        while(indx>=0)
        {
            if(cakes[0]==1)
            {
                cnt++;
                int i=0;
                while(i<indx && cakes[i]==1)
                    i++;

                flip(i-1);
            }
            else
            {
                cnt++;
                flip(indx);
            }

            while(indx>=0 && cakes[indx]==1)
                indx--;
        }

        printf("Case #%d: %d\n", ca, cnt);
    }

    return 0;
}
