#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int T,S,total,c=1,i,f;
    char p[1010];
    cin >> T;
    while(T--)
    {
        cin >> S >> p;
        total = 0;
        f = 0;
        if(p[0] == '0')
        {
            total += 1;
            f += 1;
        }
        else
            total += p[0]-48;

        for(i=1; i<=S; i++)
        {
            if(p[i] != '0')
            {
                if(i > total)
                {
                    f += i-total;
                    total += (p[i]-48)+ (i-total);
                }
                else
                    total += p[i]-48;
            }
        }
        cout << "Case #" << c++ << ": " << f << endl;
    }
}
