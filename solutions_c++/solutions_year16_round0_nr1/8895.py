#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
    FILE *fin = freopen("a-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("a-large.out", "w", stdout);

    LL t, n;

    cin>>t;
    for(LL i=1; i<=t; i++)
    {
        int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        LL tt=0;
        cin>>n;
        LL j=1;
        LL res;
        while(tt != 10 && n != 0)
        {
            LL var = n*j++;
            LL temp =var;
            while(var != 0)
            {
                LL num;
                num = var%10;
                var = var/10;
                for(LL k=0;  k<10; k++)
                {
                    if(arr[k] == num)
                    {
                        arr[k] = 11;
                        tt++;
                    }
                }
                if(tt == 10)
                {
                    res = temp;
                    break;
                }
            }
        }
        if(tt == 10)
            cout<<"Case #"<<i<<": "<<res<<"\n";
        else
            cout<<"Case #"<<i<<": INSOMNIA\n";
    }

    return 0;
}
