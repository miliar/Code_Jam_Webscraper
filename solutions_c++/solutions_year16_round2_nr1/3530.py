#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

int ans[10];
int cnt[1010];
//char s[1010];
char s[1010] = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE";

char sn[][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int main()
{
    int T,ca=1;
    scanf("%d\n",&T);
    while(T--)
    {
        scanf("%s",s);
        printf("Case #%d: ",(ca++));
        int len = strlen(s);
        memset(ans,0,sizeof(ans));
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<len;i++)
        {
            cnt[s[i]]++;
        }
        ans[0] = cnt['Z'];
        ans[8] = cnt['G'];
        ans[4] = cnt['U'];
        ans[2] = cnt['W'];
        ans[6] = cnt['X'];
        ans[5] = cnt['F'] - ans[4];
        ans[3] = cnt['H'] - ans[8];
        ans[7] = cnt['S'] - ans[6];
        ans[1] = cnt['O'] - ans[0] - ans[2] - ans[4];
        ans[9] = cnt['I'] - ans[5] - ans[6] - ans[8];

        for(int i=0;i<10;i++)
        {
            for(int j=0;j<ans[i];j++)
            {
                printf("%d",i);
            }
        }
        printf("\n");
    }
    return 0;
}

/*
Case #1: E 9
F 2
G 1
H 2
I 4
N 4
O 4
R 3
S 2
T 3
U 1
V 2
W 1
X 1
Z 1
char sn[][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
*/















