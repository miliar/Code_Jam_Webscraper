#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <memory.h>

using namespace std;

#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define LL long long
#define forn(a,b) for(LL a=0; a<b; a++)
#define FOR1(a,b) for(LL a=1; a<=b;a++)
#define fori(a,z,b) for(LL a=z; a<=b;a++)
#define sortV(a) sort(A.begin(), A.end())
#define file freopen("input.txt","r",stdin)
#define file2 freopen("output.txt","w",stdout)


int a[5][5];
int b[5][5];
int main()
{

    file;
    file2;
    int n;
    cin>>n;
    forn(i,n)
    {
        int x;
        cin>>x;
        x--;
        forn(j,4)
            forn(k,4)
                cin>>a[j][k];
        int y;
        cin>>y;
        y--;
        forn(j,4)
            forn(k,4)
                cin>>b[j][k];
        int c=0;
        int nom;
        forn(j,4)
            forn(k,4)
                if(a[x][j]==b[y][k]) {c++; nom=a[x][j];  }

        cout<<"Case #"<<i+1<<": ";
        if(c==1) cout<<nom<<endl;
        if(c==0) cout<<"Volunteer cheated!"<<endl;
        if(c>1) cout<<"Bad magician!"<<endl;
    }



}


