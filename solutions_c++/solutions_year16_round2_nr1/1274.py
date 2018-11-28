#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

int main()
{
    int T,cas = 1;
    int J;
    string str;
    freopen("C:\\Users\\L\\Downloads\\A-large.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\A-large.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        cin>>str;
        int cnt[256] = {0};
        int ans[10] = {0};
        for(int i=0;i<str.size();i++){
            cnt[str[i]]++;
        }
        if(cnt['Z'] > 0){
            ans[0] += cnt['Z'];
            cnt['Z'] -= ans[0];
            cnt['E'] -= ans[0];
            cnt['R'] -= ans[0];
            cnt['O'] -= ans[0];
        }
        if(cnt['U'] > 0){
            ans[4] += cnt['U'];
            cnt['F'] -= ans[4];
            cnt['O'] -= ans[4];
            cnt['U'] -= ans[4];
            cnt['R'] -= ans[4];
        }
        if(cnt['R'] > 0){
            ans[3] += cnt['R'];
            cnt['T'] -= ans[3];
            cnt['H'] -= ans[3];
            cnt['R'] -= ans[3];
            cnt['E'] -= 2*ans[3];
        }
        if(cnt['G'] > 0){
            ans[8] += cnt['G'];
            cnt['E'] -= ans[8];
            cnt['I'] -= ans[8];
            cnt['G'] -= ans[8];
            cnt['H'] -= ans[8];
            cnt['T'] -= ans[8];
        }
        if(cnt['T'] > 0){
            ans[2] += cnt['T'];
            cnt['T'] -= ans[2];
            cnt['W'] -= ans[2];
            cnt['O'] -= ans[2];
        }
        if(cnt['O'] > 0){
            ans[1] += cnt['O'];
            cnt['O'] -= ans[1];
            cnt['N'] -= ans[1];
            cnt['E'] -= ans[1];
        }
        if(cnt['X'] > 0){
            ans[6] += cnt['X'];
            cnt['S'] -= ans[6];
            cnt['I'] -= ans[6];
            cnt['X'] -= ans[6];
        }
        if(cnt['S'] > 0){
            ans[7] += cnt['S'];
            cnt['S'] -= ans[7];
            cnt['E'] -= ans[7];
            cnt['V'] -= ans[7];
            cnt['E'] -= ans[7];
            cnt['N'] -= ans[7];
        }
        if(cnt['F'] > 0){
            ans[5] += cnt['F'];
            cnt['F'] -= ans[5];
            cnt['I'] -= ans[5];
            cnt['V'] -= ans[5];
            cnt['E'] -= ans[5];
        }
        if(cnt['I'] > 0){
            ans[9] += cnt['I'];
            cnt['N'] -= ans[9];
            cnt['I'] -= ans[9];
            cnt['N'] -= ans[9];
            cnt['E'] -= ans[9];
        }
        printf("Case #%d: ",cas++);
        for(int i=0;i<10;i++)
            while(ans[i]--)
                printf("%d",i);
        puts("");
    }
    return 0;
}
