#include <bits/stdc++.h>
#define LL long long
#define x first
#define y second
#define pb push_back
#define mod 1000000007
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int c = 1;
    while(t--){
        LL s, n, i;
        string str;
        scanf("%lld", &s);
        cin>>str;
        LL cnt = 0;
        LL p = 0;
        for(i=0; i<(s+1); i++){
            if(i==0) p += str[i]-'0';
            else{
                if(p<i){
                    cnt += (i-p);
                    p += (i-p) + str[i]-'0';
                }
                else {
                    p += str[i]-'0';
                }
            }
        }
        cout<<"Case #"<<c<<": "<<cnt<<endl;
        c++;
    }
    return 0;
}
