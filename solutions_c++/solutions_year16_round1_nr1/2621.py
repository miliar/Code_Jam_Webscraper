#include <bits/stdc++.h>
using namespace std;

char S[1003];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);

    int T;
    cin >> T;

    for(int test=1; test<=T; test++)
    {
        scanf(" %s", S);

        string R;

        for(int i=0; S[i]!='\0'; i++)
        {
            if(S[i]<R[0])
                R.push_back(S[i]);
            else
                R.insert(R.begin(), S[i]);
        }

        printf("Case #%d: ", test);
        cout << R << endl;
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
