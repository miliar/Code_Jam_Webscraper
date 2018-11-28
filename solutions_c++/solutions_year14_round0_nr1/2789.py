#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    int tc , a , x, nc = 1;
    cin >> tc;

    while(tc--){
        set<int> s;
        cin >> a;

        for(int i = 1; i <= 4; ++i)
            for(int k = 0; k < 4; ++k)
            { cin >> x;
                if(i == a)
                    s.insert(x);
            }
        cin >> a;
        int c = 0 , ans ;
        for(int i = 1; i <= 4; ++i)
            for(int k = 0; k < 4; ++k)
            { cin >> x;
                if(i == a){
                    if(s.find(x) != s.end())
                    {   ans = x;
                        c++;
                    }
                }
            }

        printf("Case #%d: ",nc++);
        if(c == 0) puts("Volunteer cheated!"); else
        if(c == 1) cout<<ans<<endl; else
                  puts("Bad magician!");

    }


return 0;
}
