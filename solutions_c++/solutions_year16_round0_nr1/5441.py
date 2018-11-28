#include <bits/stdc++.h>
#define endl '\n'
using namespace std;

bool used_digits[15];
int t, n, current_cnt, current_multi, current_num;

void find_digits(int a)
{
    while(a > 0)
    {
        if(!used_digits[a % 10])
        {
            used_digits[a % 10] = true;
            current_cnt++;
        }

        a /= 10;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin>>t;
    for(int cs = 1; cs <= t; cs++)
    {
        cin>>n;

        if(n == 0)
        {
            cout<<"Case #"<<cs<<": INSOMNIA"<<endl;
            continue;
        }

        memset(used_digits, 0, sizeof(used_digits));
        current_cnt = 0;
        current_multi = 2;
        current_num = n;
        while(1)
        {
            find_digits(current_num);

            if(current_cnt == 10) break;

            current_num = current_multi * n;
            current_multi++;
        }

        cout<<"Case #"<<cs<<": "<<current_num<<endl;
    }

    return 0;
}
