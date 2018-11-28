#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
using namespace std;

typedef long long ll;
int T,k;

char str[1200];

int top,tmp;
int main()
{
    int ca = 1;
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    scanf("%d",&T);
    while (T--){
    scanf("%s%d",str,&k);
    //cout<<"hdwiaoido"<<endl;

    int cnt =0 ;
    int len = strlen(str);
    bool flag = true;

    for (int i = 0 ; i < len ; i ++)
    {
        if (str[i]=='-'){
            cnt ++;
            if (i+k>len){
                flag = false;}
            else
                for (int j = i ; j < i+ k ; j ++)
                    str[j] = (str[j]=='-')?'+':'-';
    }
    }
    printf("Case #%d: ",ca++);
    if (flag)
        printf("%d\n",cnt);
    else
        printf("IMPOSSIBLE\n");
    }

}

