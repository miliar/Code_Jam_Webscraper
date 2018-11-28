#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int i = a; i < b; i++)
bitset<102> a(0);
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out2.txt", "w", stdout);
    int t,pos=0;
    scanf("%d ", &t);
    for(int tc = 1; tc <= t; tc++)
    {
        string s;
        getline(cin,s);
        int ln = 0;
        a.reset(); pos=0;
        for(int i = 0; s[i] != '\0'; i++,ln++){ if(s[i] == '-')a.set(i,1);}
        int ans = 0;
        while(a.any() == true)
        {
            pos=0; ans++;
            if(a.test(pos) == 1){
                while(a.test(pos) && pos<ln){pos++;}
                For(i,0,pos)a.set(i,0);
            }
            else{
                while(a.test(pos) == 0 && pos<ln){pos++;}
                For(i,0,pos)a.set(i,1);
            }
        }
        printf("Case #%d: %d\n", tc, ans);
    }

    return 0;
}
