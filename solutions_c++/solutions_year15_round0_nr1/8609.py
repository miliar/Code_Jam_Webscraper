#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("fileNameLarge.out","w",stdout);

    int t;
    cin >> t;
    for(int T=1 ; T<=t ; T++)
    {
        int n;
        string s;
        cin >> n >> s;

        long long int counter = 0, friends = 0;

        for(int i=0 ; i<s.size() ; i++)
            if(i <= counter)
                counter += s[i]-48;
            else
                friends++, counter++, i--;

        cout << "Case #" << T << ": " << friends << endl;
    }

    return 0;
}
