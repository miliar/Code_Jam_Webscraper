#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
    //freopen("data.in", "rt", stdin);
    //freopen("data.out", "wt", stdout);
    char s[105];
    int T ;
    scanf("%d", &T);
    for(int i = 1; i <= T; ++i) {
            scanf("%s\n", s);
            int solution = 0;
            int length = strlen(s);
            for(int i = 0; i < length; ++i) {
                if(i > 0) {
                    if(s[i] == '-' && s[i-1] == '+')
                        solution += 2;
                }
                else
                    if(s[i] =='-')
                        solution++;
            }
            cout<< "Case #"<< i << ": " << solution << '\n';
    }
    return 0;
}
