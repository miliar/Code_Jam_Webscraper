#include <iostream>
#include <queue>
#include <cstdio>
#define F first
#define S second

using namespace std;

int bused;

int r,c;

int ma;

int getbc(int x,int y){
    return (1<<(y*c+x));
}

int breveal (int x,int y){
    if (bused&getbc(x,y)) return 0;
    bused|=getbc(x,y);
    for (int i=-1;i<=1;i++){
        for (int ii=-1;ii<=1;ii++){
            if (i!=0||ii!=0){
                if ((x+i>=0&&x+i<c)&&(y+ii>=0&&y+ii<r)){
                    if (ma&getbc(x+i,y+ii)){
                        return 1;
                    }
                }
            }
        }
    }
    int ret=1;
    for (int i=-1;i<=1;i++){
        for (int ii=-1;ii<=1;ii++){
            if (i!=0||ii!=0){
                if ((x+i>=0&&x+i<c)&&(y+ii>=0&&y+ii<r)){
                    ret+=breveal(x+i,y+ii);
                }
            }
        }
    }
    return ret;
}

int main(){
    freopen ("csmall.out","w",stdout);
    int t;
    cin>>t;
    for (int tc=1;tc<=t;tc++){
        int m;
        cin>>r>>c>>m;
        int bok=0;
        int sx,sy;
        for (ma=0;ma<(1<<r*c);ma++){
            int bs=0;
            for (int i=0;i<r*c;i++){
                if ((1<<i)&ma){
                    bs++;
                }
            }
            if (bs==m){
                for (sx=0;sx<c;sx++){
                    for (sy=0;sy<r;sy++){
                        if (!(ma&getbc(sx,sy))){
                            bused=0;
                            if (breveal(sx,sy)==r*c-m){
                                bok=1;
                                break;
                            }
                        }
                    }
                    if (bok) break;
                }
            }
            if (bok) break;
        }
        cout <<"Case #"<<tc<<":"<<endl;
        if (bok){
            for (int i=0;i<r;i++){
                for (int ii=0;ii<c;ii++){
                    if (i==sy&&ii==sx){
                        cout <<"c";
                        continue;
                    }
                    if (ma&getbc(ii,i)){
                        cout <<"*";
                    }
                    else{
                        cout <<".";
                    }
                }
                cout <<endl;
            }
        }
        else{
            cout <<"Impossible"<<endl;
        }
    }
}
