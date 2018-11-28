#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int cases = 1;cases <= t;cases++){
        string panCakes;
        cin >> panCakes;
        int length = panCakes.length();
        int boundaries = 0;
        char prev = panCakes[0];
        for(int i = 1;i < length;i++){
            if(prev != panCakes[i]){
                boundaries++;
                prev = panCakes[i];
            }
        }
        if(prev == '-')
            boundaries++;
        printf("Case #%d: %d\n", cases, boundaries);
    }
    return 0;
}
