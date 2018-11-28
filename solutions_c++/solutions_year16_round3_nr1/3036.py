#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <random>
#include <iostream>
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#endif

using namespace std;
typedef pair<int, int> ii;
int nTest;
priority_queue <ii> PQ;
int n;

int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        while (!PQ.empty()) PQ.pop();
        scanf("%d", &n);
        int sum = 0;
        for (int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            sum += x;
            PQ.push(ii(x, i));
        }
        int poped = 0;
        

        while (!PQ.empty()){
            if (PQ.size() == 2 && sum - poped == PQ.top().first * 2){
                int cnt = PQ.top().first;
                int c1 = PQ.top().second;
                PQ.pop();
                int c2 = PQ.top().second;
                for (int i = 0; i < cnt; i++){
                    printf("%c%c ", 'A' + c1, 'A' + c2);
                }
                break;
            } else {
                ii temp = PQ.top();
                PQ.pop();
                printf("%c ", temp.second + 'A');
                temp.first--;
                if (temp.first > 0) PQ.push(temp);
                poped++;
            }
        }
        printf("\n");

    }
    

    return 0;
}