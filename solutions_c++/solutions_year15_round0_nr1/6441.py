#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int T, smax, rpta, tmp, aux, maxi;
    char shyness[1002];
    int _shyness[1002];

    cin>>T;

    for(int tc = 1 ; tc <= T ; ++tc)    {
        cin>>smax>>shyness;
        rpta = 0;
        _shyness[0] = shyness[0] - '0';
        maxi = 0;
        for(int i = 1 ; i < strlen(shyness) ; ++i){
            _shyness[i] = shyness[i] - '0';
            _shyness[i] += _shyness[i-1];
            maxi = max(maxi, i - _shyness[i-1]);
        }
        if(maxi<0) maxi = 0;
        printf("Case #%d: %d\n", tc, maxi);
    }

    return 0;
}
