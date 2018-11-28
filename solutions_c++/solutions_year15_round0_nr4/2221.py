#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <set>
using namespace std;

int p[2000];
multiset<int> a;

int main(){
    //freopen("a.txt", "r", stdin);
    //freopen("D-small-attempt0.in", "r", stdin);freopen("b.txt","w",stdout);
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++){
        /*int d;
        int tmp;
        scanf("%d", &d);
        a.clear();
        for (int i = 1; i <= d; i++){
            scanf("%d", &tmp);
            a.insert(tmp);
        }

        multiset<int>::iterator it;
        int use_time = 0;
        while(1){
            it = a.end();
            it--;
            tmp = *it;
            if (tmp <= 3) break;

            a.erase(it);
            a.insert(tmp / 2);
            a.insert(tmp - tmp / 2);
            use_time++;
        }
        use_time += tmp;
        printf("Case #%d: %d\n", k, use_time);*/

        printf("Case #%d: ", k);
        int x, r, c;
        char ans;
        cin >> x >> r >> c;
        if (r > c){
            int tmp = c;
            c = r;
            r = tmp;
        }
        if (x == 1)
            ans = 'g';
        else if (x == 2){
            if ((r * c) % 2 != 0){
                ans = 'r';
            }
            else ans = 'g';
        }
        else if (x == 3){
            if (r == 2 && c == 3) ans = 'g';
            else if (r == 3 && c == 3) ans = 'g';
            else if (r == 3 && c == 4) ans = 'g';
            else ans = 'r';
        }
        else{
            if (r == 3 && c == 4) ans = 'g';
            else if (r == 4 && c == 4) ans = 'g';
            else ans = 'r';
        }

        if (ans == 'g') puts("GABRIEL");
        else puts("RICHARD");
    }

	return 0;
}
