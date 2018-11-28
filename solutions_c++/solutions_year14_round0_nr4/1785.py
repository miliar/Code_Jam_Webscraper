#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    int T;
    double  x[1100],y[1100];
    cin>>T;
    for(int i=1;i<=T;++i){
        int N=0;

        cin>>N;
        for(int j=0;j<N;++j){
            cin>>x[j];
        }
        for(int j=0;j<N;++j){
            cin>>y[j];
        }
        sort(x,x+N,greater<double>());
        sort(y,y+N,greater<double>());
//        for(int j=0;j<N;++j)
//            cout<<x[j]<<" ";
//        cout<<endl;
//        for(int j=0;j<N;++j)
//            cout<<y[j]<<" ";
//        cout<<endl;
        int score1=0,score2=0,px=0,py=0;
        while(px<N&&py<N){
            if(x[px]>y[py]){
                ++score1;
                ++px,++py;
            }else {
                ++py;
            }
        }

        px=py=0;
        while(px<N&&py<N){
            if(x[px]<y[py]){
                ++px,++py;
            }else {
                ++px;
                ++score2;
            }
        }

        printf("Case #%d: %d %d\n",i,score1,score2);
    }
    return 0;
}
