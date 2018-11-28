#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int testCase;
    freopen("/Users/qianjay/Documents/algorithm/pa/in", "r", stdin);
    freopen("/Users/qianjay/Documents/algorithm/pa/out", "w", stdout);
    
    scanf("%d",&testCase);
    for (int id=1; id <= testCase; id++) {
        printf("Case #%d: ",id);
        char line[128];
        scanf("%s",line);
        int cnt=0;
        int len=(int)strlen(line);
        for (int i=0; i<len-1; i++) {
            if (line[i]!=line[i+1]) {
                cnt++;
            }
        }
        if (line[len-1]=='-') {
            cnt++;
        }
        printf("%d\n",cnt);
    }
    return 0;
}