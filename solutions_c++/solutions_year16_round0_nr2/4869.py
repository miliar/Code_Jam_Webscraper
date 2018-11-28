#define _CRT_SECURE_NO_WARNINGS

#define max(a,b) ((a) > (b) ? (a) : (b))
#include<stdio.h>
#include<queue>

using namespace std;
typedef long long ll;

typedef priority_queue<int> PQ;
struct Data{ PQ q; int t; };
Data data[100][100];

void swap(char* str, int pp, int pplen)
{
    for(int g = 0;g < pplen;++g){
        int pg = pp - g;
        if (str[pg] == '+'){
            str[pg] = '-';
        }else{
            str[pg] = '+';
        }
    }
    for(int g = 0;g < pplen/2;++g){
        char c = str[pp - g];
        str[pp - g] = str[pp - pplen + 1 + g];
        str[pp - pplen + 1 + g] = c;
    }
}

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        ll ans = 0;
        char str[200] = {};
        scanf("%s", str);

        ll len = strlen(str);

        // 全部プラスの状態から、
        // 逆に初期状態にたどり着けるようにすればよさそう。
        // あぁ、まて、それは、末尾のプラスを削った上で、
        // 残りの部分のプラマイ切り替え回数と同じだ。

        char cs = '+';
        for(int di = 0;di < len;++di){
            int pos = len - 1 - di;
            if (str[pos] == cs) {
                continue;
            }
            // 切り替わり発見
            cs = cs == '+' ? '-' : '+';
            ++ans;
        }

        printf("Case #%d: %lld\n",r+1,ans);
    }

}
