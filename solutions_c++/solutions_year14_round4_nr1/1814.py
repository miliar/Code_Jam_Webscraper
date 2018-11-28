#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<algorithm>

using namespace std;

typedef long long ll;

int map[2000];

int main(void){

    int T;
    scanf("%d",&T);

    for(int round = 0;round < T;++round){
        int ans = 0;
        int N,X;
        scanf("%d %d",&N,&X);
        for(int i = 0;i < N;++i){
            scanf("%d",map+i);
        }
        sort(map,map+N);

        int rem = N;
        while(rem>1){
            int mi,mz;
            mi = -1;
            mz = -1;
            for(int i = 0;i < N;++i){
                if(map[i]==0)continue;
                for(int z = i+1;z < N;++z){
                    if(map[z]==0)continue;
                    if(map[i]+map[z] == X){
                        mi = i;
                        mz = z;
                        goto NEXT;
                    }
                    if(map[i]+map[z] > X){
                        break;
                    }
                    if(mi < 0 || (map[i]+map[z] > map[mi] + map[mz])){
                        mi = i;
                        mz = z;
                    }
                }
            }
NEXT:
            if(mi < 0 ){
                // ‘g‚Ý‡‚í‚¹‚ç‚ê‚é‚à‚Ì‚ª‚È‚¢
                ans += rem;
                rem = 0;
            }else{
                map[mi] = 0;
                map[mz] = 0;
                rem -= 2;
                ans += 1;
            }
        }
        ans += rem;

        printf("Case #%d: ",round+1);
        printf("%d",ans);
        printf("\n");
    }

}
