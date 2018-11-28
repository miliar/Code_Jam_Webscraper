#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>

using namespace std;
int a[1000];
char s[1000];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    int t,ca;
    scanf("%d",&t);
    for(int ca = 1;ca <= t ; ca++){
        scanf("%s",s);
        int l = strlen(s);
        for(int i = 0 ; i < l ; i++){
            if(s[i] == '+')
                a[i] = 1;
            else a[i] = 0;
        }
        int sum = 0;
        for(int i = l-1 ; i >= 0 ; i--){
            if(a[i] == 1)
                continue;
            for(int j = 0 ; j <= i ; j++)
                a[j] = 1-a[j];
            sum++;
        }
        printf("Case #%d: ",ca);
        printf("%d\n",sum);
    }
    return 0;
}
