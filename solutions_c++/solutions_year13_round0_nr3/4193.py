#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <set>
using namespace std;
int s[105];
set<long long> pset;
set<long long>::iterator pit;
int hw(long long inte)
{
    int len=0;
    while (inte>0)
        { s[++len]=inte%10;inte /=10;};
    for (int i=1; i<=len/2; i++)
        if (s[i]!=s[len-i+1])
            return 0;
    return 1;
}

int main()
{
    int cnt=0;
    pset.insert(0);
    ifstream fin("output.txt");
    /*
    for (long long i=(long long)1; i<=(long long)10000010; i++)
        if (hw(i) && hw(i*i))
            pset.insert(i);
            */
    long long t;
    for (int i=0; i<40; i++)
    {
        fin>>t;
        pset.insert(t);
    }
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);

    //cout << pset.size() << endl;;
    int T;
    cin >> T;
    for (int icase=1; icase<=T; icase++)
    {
        long long a,b;
        cin >> a >> b;
        int ans=0;

        pit=pset.begin();
        while ( *pit < ceil(sqrt(a)) ) pit++;
        pit--;
        while ( *pit <= floor(sqrt(b)) ) {pit++; ans++;}
        ans--;

        cout << "Case #" << icase << ": ";
        cout << ans << endl;
    }

}
