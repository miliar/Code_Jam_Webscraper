#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#define forn(i,n) for(int i=0;(i)<(n);(i)++)

using namespace std;

typedef unsigned long long ull;

int main()
{
    int T;
    freopen("B.txt","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;

    forn(i,T){
        int n;
        cin>>n;

        int fuckme[2550];

        forn(j,2550)
            fuckme[j]=0;

        forn(j,2*n-1){
            forn(k,n){
                int aux;
                cin>>aux;
                fuckme[aux]++;
            }
        }

        vector <int> vapenation;
        forn(j,2550)
            if(fuckme[j]%2)
                vapenation.push_back(j);

        sort(vapenation.begin(),vapenation.end());

        cout<<"Case #"<<i+1<<": ";
        forn(j,n){
            cout<<vapenation[j];
            if(j<n-1)
                cout<<" ";
        }
        cout<<endl;

    }
    return 0;
}
