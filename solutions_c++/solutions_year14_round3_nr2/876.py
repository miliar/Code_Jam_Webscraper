#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

bool used[101];
bool used_char[30];
char in_str[101][101];
char last_char;
int k;

int discover(int level)
{
    if (level == k)
        return 1;

    int ans = 0,i,j;

    for (i=0; i<k; i++){
        if (!used[i]){
            int len = strlen(in_str[i]);
            char cur_last_char = last_char;

            for (j=0; j<len; j++){
                if (cur_last_char == in_str[i][j]){
                    continue;
                }
                else{
                    cur_last_char = in_str[i][j];
                }

                if (used_char[in_str[i][j]-'a'])
                    break;
            }
            if (j<strlen(in_str[i]))
                continue;

            for (j=0; j<len; j++){
                used_char[in_str[i][j]-'a'] = true;
            }
            used[i] = true;
            cur_last_char = last_char;
            last_char = in_str[i][len-1];

            ans += discover(level+1);

            last_char = cur_last_char;
            used[i] = false;
            for (j=0; j<len; j++){
                if (last_char != in_str[i][j]){
                    used_char[in_str[i][j]-'a'] = false;
                }
            }
        }
    }

    return ans;
}

int main(void)
{
    int t,i,j,n;
    char temp[101];
    char cur;
    int cnt,flag;

    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");

    fscanf(in,"%d",&n);

    for (t=0; t<n; t++){

        fscanf(in,"%d\n",&k);
        printf("%d\n",k);

        for (i=0; i<30; i++)
            used_char[i] = false;

        flag = 0;
        for (i=0; i<k; i++){
            cnt = 0;
            fscanf(in,"%s",temp);
            for (j=0; j<strlen(temp); j++){
                if (j>0 && temp[j] == temp[j-1])
                    continue;

                if (j>0 && temp[j] != temp[j-1] && used_char[temp[j]-'a']){
                    flag = 1;
                }

                in_str[i][cnt] = temp[j];
                used_char[temp[j]-'a'] = true;
                cnt++;
            }
            in_str[i][cnt] = '\0';

            printf("%s\n",in_str[i]);

            for (j=0; j<30; j++)
                used_char[j] = false;
        }

        if (flag == 1){
            fprintf(out,"Case #%d: 0\n",t+1);
            continue;
        }

        for (i=0; i<101; i++)
            used[i] = false;

        last_char = 0;
        fprintf(out,"Case #%d: %d\n",t+1,discover(0));
    }

    return 0;
}
