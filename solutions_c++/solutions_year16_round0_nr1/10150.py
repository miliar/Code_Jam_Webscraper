#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll ara[10];
ll digit (ll a)
{

    while (a!=0){
        ll t=a%10;
        ara[t]=1;
        a/=10;
    }

}
bool test (ll ara[])
{
    for (int i=0; i<10; i++){
        if (ara[i]==1){
            continue;
        }
        else {
            return false;
        }
    }
    return true;
}
int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("output-large.txt", "w", stdout);
    ll T, N, c=1, i;
    cin >> T;
    while (T--){
        cin >> N;
        memset (ara, 0, sizeof (ara));
        if (N==0){
            cout << "Case #" << c++ << ": " << "INSOMNIA" << endl;
        }
        else {

            digit (N);
            i=0;
            digit((i+1)*N);
            while (test (ara)!=true){
                i++;
                digit((i+1)*N);
            }
            cout << "Case #" << c++ << ": " << (i+1)*N << endl;
        }
    }

    return 0;
}

