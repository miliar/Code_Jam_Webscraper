#include <stdio.h>
#include <string.h>
#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))
int data[10000];

int main(){
    freopen("test.in","r",stdin);
    freopen("small.out","w",stdout);
    int T;
    int tt = 1;
    scanf("%d",&T);
    while(T--){
        int m;
        scanf("%d ",&m);
        for(int i = 0;i < m;i++){
            scanf("%d",&data[i]);
        }
        int res = 0;
        while(1){
            int mi,mi2;
            mi = mi2 = 0;
            if(m >= 2){
                if(data[0] > data[1]){mi = 0;mi2 = 1;}
                else{mi = 1; mi2 = 0;}
            }
            for(int i = 2 ;i < m;i++){
                if(data[mi] < data[i]){mi2 = mi;mi = i;}
            }
            if(data[mi] <= 3){
                res += data[mi];
                break;
            }else{
                int rest = 0;
                int ns = 0x7fffffff;
                for(int s = 1; s < data[mi];s++){
                    int t_ns = 0;
                    for(int i = 0;i < m;i++){
                        if(data[i] > s){
                            t_ns += (data[i] - 1) / s;
                        }
                    }
                    if(t_ns + s < rest + ns){
                        rest = s;
                        ns = t_ns;
                    }
                }
                if(ns + rest < data[mi]){
                    int j = 0;
                    res += ns;
                    for(int i = 0;i < m;i++){
                        if(data[i] > rest){
                            int tt = data[i];
                            data[i] = rest;
                            tt -= rest;
                            while(tt > 0){
                                data[m+j++] = min(rest,tt);
                                tt -= rest;
                            }
                        }
                    }
                    m += ns;
                }else{
                    res += data[mi];
                    break;
                }
            }
        }
        printf("Case #%d: %d\n",tt++,res);
    }
}