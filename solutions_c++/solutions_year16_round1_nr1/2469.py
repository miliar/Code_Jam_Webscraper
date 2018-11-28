#include <iostream>
#include <fstream>
#include <deque>
#include <string.h>
#define NMAX 1005
using namespace std;

int main()
{
    //freopen("data.in", "rt",stdin);
    //freopen("data.out", "wt", stdout);
    int T;
    scanf("%d", &T);
    for(int j = 1; j <= T; ++j) {
        char s[NMAX];
        deque<char> x;
        scanf("%s", &s);
        x.push_back(s[0]);
        for(int i = 1; i < strlen(s); ++i) {
            if(s[i] >= x.back())
                x.push_back(s[i]);
            else
                x.push_front(s[i]);
        }
        cout<<"Case #"<<j<<": ";
        for(deque<char>::reverse_iterator it = x.rbegin(); it != x.rend(); ++it)
            cout<<*it;
        cout<<'\n';
    }
    return 0;
}
