#include<bits/stdc++.h>


using namespace std;
#define ll long long int

ll modulo(ll base, ll exponent)
{
    ll x = 1;
    ll y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) ;
        y = (y * y) ;
        exponent = exponent / 2;
    }
    return x ;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output26.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for(int k=1;k<=t;k++)
    {

        char A[1001];
        scanf(" %s",A);

         printf("Case #%d: ",k);
        int len=strlen(A);

        deque<char> ans;

        ans.push_back(A[0]);

        for(int i=1;i<len;i++)
        {
            if(A[i]>=ans.front())
                ans.push_front(A[i]);
            else
                ans.push_back(A[i]);
        }
        for (deque<char>::iterator it = ans.begin(); it != ans.end(); ++it)
             cout <<*it;
        printf("\n");
    }

}
