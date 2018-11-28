#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>
using namespace std;

const int maxn=1001;

int a[maxn];

void work()
{
    int maxS,i,j,k;
    string sin;
    cin >> maxS;
    cin >> sin;
    for (i=0;i<=maxS;i++)
        a[i]=sin[i]-'0';
    int claped=0,need=0;
    for (i=0;i<=maxS;i++)
    {
        if (a[i]==0) continue;
        if (claped<i)
        {
            need+=i-claped;
            claped+=i-claped;
        }
        claped+=a[i];
        //cout << i<<" "<<claped<<endl;
    }
    cout<<need<<endl;
}

int main()
{
    int T;
    cin >> T;
    for (int cas=1;cas<=T;cas++)
    {
        cout <<"Case #"<<cas<<": ";
        work();
    }
    return 0;
}
