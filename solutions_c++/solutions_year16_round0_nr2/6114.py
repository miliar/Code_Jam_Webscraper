#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int T,cas = 1;
    char str[150];
    freopen("C:\\Users\\L\\Downloads\\B-large.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\B-large.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        memset(str,0,sizeof(str));
        printf("Case #%d: ",cas++);
        scanf("%s",str+1);
        str[0] = 'a';
        int l = strlen(str);
        int cnt = 0;
        for(int i=1;i<l;i++)
            if(str[i] != str[i-1])
                cnt++;
        if(str[l-1] == '+')
            cnt--;
        printf("%d\n",cnt);
    }
    return 0;
}
