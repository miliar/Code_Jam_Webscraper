/*
 * A.cpp
 *
 * Created by: Ashik <ashik@KAI10>
 * Created on: 08-05-2016
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back
#define MAX 1000000

struct olo{
    int first, second;
    bool operator < (const olo &p)const{
        return first > p.first;
    }
};

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);

	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
        int N;
        scanf("%d", &N);

        olo a[N];
        for(int i=0; i<N; i++){
            scanf("%d", &a[i].first);
            a[i].second = i+'A';
        }

        printf("Case #%d: ", ++cs);

        sort(a, a+N);
        while(a[0].first != 1){
            while(a[0].first>a[1].first){
                putchar(a[0].second);
                putchar(' ');
                a[0].first--;
            }
            if(a[0].first == 1) break;
            putchar(a[0].second);
            putchar(a[1].second);
            putchar(' ');

            a[0].first--;
            a[1].first--;

            sort(a, a+N);
        }

        int strt;
        if(N%2){
            putchar(a[0].second);
            putchar(' ');
            strt = 1;
        }
        else strt = 0;

        putchar(a[strt].second);
        putchar(a[strt+1].second);

        for(int i=strt+2; i<N; i+=2){
            putchar(' ');
            putchar(a[i].second);
            putchar(a[i+1].second);
        }
        puts("");
	}

	return 0;
}
