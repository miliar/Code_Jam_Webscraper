#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
const int N = 110;
char d[N];

int main()
{
    int T;
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    cin >> T;

    for(int _=1;_<=T;_++){
        cin >> d;
        int l = strlen(d);
        int ans=1;
        for(int i=1;i<l;i++) if(d[i] !=d[i-1]) ans++;
        if (d[l-1] == '+') ans--;
        printf("Case #%d: %d\n",_,ans);
    }

    return 0;
}

