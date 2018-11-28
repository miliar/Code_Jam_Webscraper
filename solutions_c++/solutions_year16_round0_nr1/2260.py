#include<bits/stdc++.h>
using namespace std;

void update_visited(int& visited, int number) {
    while(number) {
        visited|=(1<<(number%10));
        number/=10;
    }
}

void solve(int value) {
    if(value==0) {
        printf("INSOMNIA\n");
        return;       
    }
    static const int done = (1<<10)-1;
    int visited = 0;
    int counter = 0;
    do {
        ++counter;
        update_visited(visited, value*counter);
        assert(value*counter>0);
    } while(visited!=done);
    
    printf("%d\n", value*counter);
}

int main() {
    int n_testcases, start_number;
    scanf("%d", &n_testcases);
    for(int i=1; i<=n_testcases; ++i) {
        printf("Case #%d: ", i);
        scanf("%d", &start_number);
        solve(start_number);
    }
    return 0;
}
