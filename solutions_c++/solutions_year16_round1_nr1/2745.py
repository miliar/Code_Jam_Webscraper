#include <cstdio>
#include <deque>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int t;
char s[1000+1];
deque <char> d;

int main(){
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        d.clear();
        scanf("%s", s);
        
        d.push_back(s[0]);
        for(int j=1; s[j]; j++){
            if(s[j] >= d.front())
                d.push_front(s[j]);
            else
                d.push_back(s[j]);
        }
        
        printf("Case #%d: ", i);
        for(int j=0; s[j]; j++)
            printf("%c", d[j]);
        printf("\n");
    }
    
    return 0;
}