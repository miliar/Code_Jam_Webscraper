#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <locale>
#include <iomanip>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(void)
{
    cin.sync_with_stdio(0);

    ifstream cin("A-large.in");
    ofstream cout("A-large.out");

    long long T, k;
    string audience;
    long long Smax;

    cin>>T;
    for(k=0;k<T;k++)
    {
        cin >> Smax;
        cin >> audience;
        long long addedAudience = 0;
        long long stoodAudience = 0;

        for (long long i = 0; i <= Smax; i++) {
            if (stoodAudience < i) {
                long long needAdd = i - stoodAudience;
                addedAudience += needAdd;
                stoodAudience += needAdd;
            }

            long long nowStandAudience = audience[i] - '0';
            stoodAudience += nowStandAudience;

        }


        cout<<"Case #"<<k+1<<": "<<addedAudience;
        cout<<"\n";
    }
    return 0;
}
