#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;
int cnt = 0;
int N;
void print_binary(int n) //将整型数值n二进制输出。
{
    if(n == 0) return;
    print_binary(n>>1);
    printf("%d",n&0x1);
}

int test(int t,int num){
    int ret = -1;
    long long int tmp = 0;
    long long int cur = 1;
    for(int i=0;i<16;i++){
        if((1<<i) & t)
            tmp += cur;
        cur = cur * num;
    }
    for(int i=2;i<100;i++)
        if(tmp % i == 0)
            return i;
    return ret;
}

void judge(int t){
    //printf("%d\n",t);
    vector<int> ans;
    bool suc = true;
    for(int i=2;i<=10;i++){
        int ret = test(t,i);
        if(ret != -1)
            ans.push_back(ret);
        else
            suc = false;
    }
    if(suc){
        //printf("%d\n",t);
        print_binary(t);

        for(int i=0;i<ans.size();i++)
            printf(" %d",ans[i]);
        printf("\n");

        cnt++;
    }
}
int main()
{
    int T,cas = 1;
    int J;
    freopen("C:\\Users\\L\\Downloads\\C-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\C-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        printf("Case #%d:\n",cas++);
        scanf("%d %d",&N,&J);
        for(int i=0;i<(1<<(N-2));i++){
            //printf("%d\n",(1<<15) | (i<<1) | 1);
            judge((1<<(N-1)) | (i<<1) | 1);
            if(cnt>=J)
                break;
        }

    }
    return 0;
}
