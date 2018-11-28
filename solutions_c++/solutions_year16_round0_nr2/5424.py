#include <bits/stdc++.h>
#define MAX 110

using namespace std;

int main()
{
    freopen("B-large.in", "rb", stdin);
    freopen("Output.out", "wb", stdout);

    char str[MAX];
    int n, t;
    int ans;
    int in;
    int i1, i2;

    cin>>t;
    for(int i=1; i<=t; i++){
        scanf("%s", str);
        n = strlen(str);
        ans = 0;

        for(int j = 1; j<n; j++){
           if(str[j]!= str[j-1]) ans++;
        }
        if(str[n-1] == '-') ans++;

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }


    return 0;
}
