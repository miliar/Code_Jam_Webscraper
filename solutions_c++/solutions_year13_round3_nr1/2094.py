#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <set>
using namespace std;

char vowels[] = {'a', 'e', 'i', 'o', 'u'};
char name[1000001];
set<int> markset;
set<int>::iterator it;
int dist[1000001];
int n;

bool isvowel(char ch){
    int i;
    for(i = 0; i < 5; i++){
        if(ch == vowels[i])
            return true;
    }
    return false;
}

void markcons(int L){
    int i, j;

    markset.clear();
    for(i = 0; i < L; i++){
        for(j = i; j < i + n && j < L; j++){
            if(isvowel(name[j])){
                break;
            }
        }
        if (j == i + n){
            markset.insert(j - 1);
        }
    }
    // printf("markset: ");
    // for (it = markset.begin(); it != markset.end(); it++){
    //     printf("%d ", *it);
    // }
    // puts("");
}

long long nvalue(){
    int i, j;
    int L = strlen(name);
    long long value = 0;

    markcons(L);
    for(i = 0; i < L; i++){
        it = markset.lower_bound(i + n - 1);
        if (it != markset.end()){
            value += L - *it;
            // printf("i %d, i+n-1 %d, L %d, it %d, value+ %d\n", i, i + n - 1, L, *it, L - *it);
        }
    }
    // printf("%lld\n", value);
    return value;
}

int main(){
    int T, i;
    long long value;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    
    scanf("%d", &T);
    for (i = 0; i < T; i++){
        scanf("%s", name);
        scanf("%d", &n);
        value = nvalue();
        printf("Case #%d: %lld\n", i+1, value);
    }

    return 0;
}