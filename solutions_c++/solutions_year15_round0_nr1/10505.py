#include<stdio.h>
#include<iostream>
using namespace std;

int main() {
    int T, s, guest;
    int sList[1005];
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>T;
    char str[1005];
    for(int j=1; j<=T; j++) {
        guest = 0;
        scanf("%d ",&s);
        gets(str);
        for(int i=0; i<=s; i++){
            if(str[i]!=' ')
                sList[i]=str[i]-48;
        }
        int sum = 0;
        for(int i=0; i<=s; i++){
            if(sList[i]!=0 && sum<i){
                guest+=(i - sum);
                sum += guest;
            }
            sum += sList[i];
        }
        printf("Case #%d: %d\n",j, guest);
    }
}
