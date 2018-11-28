#include <list>
using namespace std;
#include <stdio.h>
#include <string.h>

const int MAX = 1010;
int test, n;
char s[MAX];

int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int ii = 1; ii <= test; ++ii){
        scanf("%s", s + 1);
        printf("Case #%d: ", ii);
        n = strlen(s + 1);
        list <char> li;
        li.push_back(s[1]);
        for (int i = 2; i <= n; ++i)
        if (s[i] >= *li.begin())
            li.push_front(s[i]);
        else
            li.push_back(s[i]);

        for (list <char>::iterator it = li.begin(); it != li.end(); ++it)
                printf("%c", *it);

        printf("\n");
    }
    return 0;
}

