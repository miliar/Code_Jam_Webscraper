#include <bits/stdc++.h>>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    cin >> t;

    for(int i=0; i<t; i++)
    {
        vector <bool> d(10);
        long long n, k=0;
        cin >> n;

        if(n==0)
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        else
        {
            int sum=0;
            for(int j=1; sum<55; j++)
            {
                k = n*j;
                int x = k;
                while(x>0)
                {
                    if(!d[x%10])
                    {
                        sum += x%10+1;
                        d[x%10] = true;
                    }
                    x/=10;
                }
            }

            cout << "Case #" << i+1 << ": " << k << endl;
        }
    }
}
