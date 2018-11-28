#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <set>
using namespace std;

int a[2000], use_time;

int max_value(int d){
    int m = a[1];
    int j = 1;
    for (int i = 2; i <= d; i++){
        if (a[i] > m){
            m = a[i];
            j = i;
        }
    }
    return j;
}

void try_d(int t, int d){
    //cout << d << endl;
    int max_x = max_value(d);

    if (a[max_x] <= 3){
        use_time = (use_time == 0? (t + a[max_x]) : min(t + a[max_x], use_time));
        return ;
    }

    for (int i = 1; i <= d; i++){
        a[i] -= 1;
    }
    try_d(t + 1, d);
    for (int i = 1; i <= d; i++){
        a[i] += 1;
    }

    int tmp = a[max_x];
    int tmp2;
    tmp2 = (tmp > 4 ? 3 : 2);
    for (int i = tmp2; i <= (tmp - tmp2); i++){
        a[max_x] = tmp - i;
        a[d + 1] = i;
        try_d(t + 1, d + 1);
    }
    a[max_x] = tmp;
}

int main(){
    //freopen("a.txt", "r", stdin);
    //freopen("B-small-attempt2.in", "r", stdin);freopen("b.txt","w",stdout);
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++){
        int d;
        scanf("%d", &d);
        for (int i = 1; i <= d; i++){
            scanf("%d", &a[i]);
        }
        use_time = 0;
        try_d(0, d);
        /*int tmp;
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
        use_time += tmp;*/
        printf("Case #%d: %d\n", k, use_time);
    }

	return 0;
}
