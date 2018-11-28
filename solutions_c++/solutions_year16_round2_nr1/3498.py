#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char S[2222];
int cnt[256],len;
string nums[]={
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
int tryord[]={0,7,8,3,5,4,9,6,1,2};


int anscnt[10],used=0,solved=0;

int tt;

void dfs(int lev) {
    if (used==len) {
        solved=true;
        printf("Case #%d: ",tt);
        for (int i=0;i<10;i++) for (int j=0;j<anscnt[i];j++)
            printf("%d",i);
        printf("\n");
    }
    if (solved) return;

    for (int i=0;i<10;i++) {
        int p=tryord[i];
        bool can=1;
        for (int j=0;j<nums[p].size();j++) {
            if (!cnt[nums[p][j]]) {
                can=0;break;
            }
        }
        if (can) {
            for (int j=0;j<nums[p].size();j++) {
                cnt[nums[p][j]]--;
            }
            anscnt[p]++;
            used+=nums[p].size();
            dfs(lev+1);
            for (int j=0;j<nums[p].size();j++) {
                cnt[nums[p][j]]++;
            }
            anscnt[p]--;
            used-=nums[p].size();
        }
    }
}

int main () {
    int casen;
    scanf("%d",&casen);
    for (tt=1;tt<=casen;tt++) {
        scanf("%s",S);
        len=strlen(S);
        for (int i=0;i<len;i++) cnt[S[i]]++;

        dfs(1);

        used=solved=0;
        memset(cnt,0,sizeof cnt);
        memset(anscnt,0,sizeof anscnt);
        memset(S,0,sizeof S);

    }
}
