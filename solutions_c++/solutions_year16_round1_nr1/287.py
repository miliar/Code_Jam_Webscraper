#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <deque>
using namespace std;
typedef long long ll;

char str[1005];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("alarge.txt","w",stdout);
    int T,Case=1;
    for(scanf("%d",&T);Case<=T;Case++){
        scanf("%s",str);
        int len=strlen(str);
        deque<char> s;
        s.push_back(str[0]);
        for(int i=1;i<len;i++){
            if(str[i]>=s[0])s.push_front(str[i]);
            else s.push_back(str[i]);
        }
        printf("Case #%d: ",Case);
        for(int i=0;i<len;i++)putchar(s[i]);
        puts("");
    }
    return 0;
}

