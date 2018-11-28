#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool visited[10];
int cnt = 0;
void parse(long long n){
    if(n < 10){
        if(!visited[n]){
            cnt++;
            visited[n] = 1;
        }
        return;
    }
    int x = n%10;
    if(!visited[x]){
        cnt++;
        visited[x] = 1;
    }
    parse(n/10);
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    int c = 1;
    while(t--){
        cout << "Case #" << c++ <<": ";
        long long n; cin >> n;
        if(n == 0){
            cout << "INSOMNIA\n";
            continue;
        }

        memset(visited, 0, sizeof visited);
        cnt = 0;
        int i = 1;
        long long ans ;

        while(cnt < 10){
            parse((long long)i*n);
            ans = (long long)i * n;
            i++;
        }
        cout << ans << "\n";
    }

    return 0;
}
