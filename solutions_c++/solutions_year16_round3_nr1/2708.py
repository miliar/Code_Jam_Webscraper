#include<iostream>
#include<stdio.h>
#include<queue>
using namespace std;

typedef pair<int, int> ii;

main() {
    int T, sum = 0;
    scanf(" %d", &T);

    for (int t=1 ; t<=T ; t++) {
        int n, arr[1005];

        priority_queue< pair<int, int> > Q;

        scanf(" %d", &n);
        for (int i=0, temp ; i<n ; i++) {
            scanf(" %d", &temp);
            Q.push(ii(temp, i));
            sum+=temp;
        }

        printf("Case #%d: ", t);

        if (sum%2) {
            ii curr = Q.top();
            Q.pop();
            printf("%c ", curr.second+'A');
            curr.first--;
            if (curr.first)
                Q.push(curr);
            sum--;
        }

        while (sum) {
            ii curr = Q.top();
            Q.pop();
            printf("%c", curr.second+'A');
            curr.first--;
            if (curr.first)
                Q.push(curr);
            sum--;

            curr = Q.top();
            Q.pop();
            printf("%c ", curr.second+'A');
            curr.first--;
            if (curr.first)
                Q.push(curr);
            sum--;
        }
        printf("\n");
    }
}
