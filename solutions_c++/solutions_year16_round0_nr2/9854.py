#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;

char str[1000];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%s",str);
        int len = strlen(str);
        int cnt = 1;
        bool right_start;
        if( str[0]== '+' ) right_start = true;
        else right_start = false;
        char cur = str[0];
        for(int j=1;j<len;j++){
            if( str[j] != cur ){
                cnt ++;
                cur = str[j];
            }
        }
        //printf("cnt=%d right_start = %d\n",cnt,right_start);
        printf("Case #%d: %d\n",i, right_start?(cnt%2==0?cnt:cnt-1):(cnt%2==0?cnt-1:cnt));
    }

    return 0;
}
