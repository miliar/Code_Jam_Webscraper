#include<cstdio>
#include<vector>
#include<iostream>
#include<map>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<stack>
#include<cmath>
using namespace std;

#define A

int main(){
    #ifdef ARC
        freopen("A-small-attempt0.in","r",stdin);
        //freopen("out.txt","r",stdout);
    #endif
    int T,r,ncas=0;
    double t;
    scanf("%d",&T);
    double PI = 3.141592654;
    //cout<<<<endl;
    while(T--){
        int con=0;
        scanf("%d",&r);
        cin>>t;
        double tmp1,tmp2;
        t *= PI;
        for(int i=r+1;true;i+=2){
            tmp1 = i*i*PI;
            tmp2 = (i-1)*(i-1)*PI;
            if(t -(tmp1-tmp2) >= 0.000000-0.0000001){
                con++;
                t -= (tmp1-tmp2);
            }else{

                //cout<<"T: "<<t<<" "<<(tmp1-tmp2)<<endl;
                break;
            }
        }
        printf("Case #%d: %d\n",++ncas,con);
        //cout<<con<<endl;

    }
}
