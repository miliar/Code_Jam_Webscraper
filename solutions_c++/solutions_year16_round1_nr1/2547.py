#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int t;
    scanf("%d\n", &t);
    for(int i=1; i<=t; i++){
        char s[1010];
        int temp;
        pair<char, int> a[1010];
        scanf("%s\n", s);
        int y=strlen(s);
        for(int j=0; j<y; j++){
            a[j].first=s[j];
            a[j].second=j;
        }
        sort(a, a+y);
        int b=99999;
        printf("Case #%d: ", i);
        for(int j=y-1; j>=0; j--){
            if(b>a[j].second){
                printf("%c", a[j].first);
                b=a[j].second;
                a[j].first=0;
            }
        }
        for(int j=0; j<y; j++){
            temp=a[j].second;
            a[j].second=a[j].first;
            a[j].first=temp;
        }
        sort(a, a+y);
        for(int j=0; j<y; j++) printf("%c", a[j].second);
        printf("\n");
    }
    return 0;
}
