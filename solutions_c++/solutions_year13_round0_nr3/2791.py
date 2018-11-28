#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

int T,t;

int check(long long x)
{
    char tmp[100];
    sprintf(tmp,"%I64d",x);
    for (int i = 0; i<strlen(tmp); i++){
        if (tmp[i]!=tmp[strlen(tmp)-i-1]) return 0;
    }
    return 1;
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    cin>>T;
    while (t<T){
        t++;
        long long a,b;
        long long ans = 0;
        cin>>a>>b;
        for (long long i = a; i<=b; i++){
            long long si = (long long)sqrt((double)i);
            if ((i==si*si) && check(i) && check(si)) ans++;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
