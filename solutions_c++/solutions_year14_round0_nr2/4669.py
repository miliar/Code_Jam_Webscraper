#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
using namespace std;

#define eps 1e-8
int cmp (double x){
    if (fabs(x)<eps) return 0;
    if (x>0) return 1;
    return -1;
}
int main() {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while (T--){
        double c,f,x;
        cin>>c>>f>>x;
        double time=0;
        double cur=0;
        double speed=2.0;
        while (cmp(cur-x)<0){
            double next=time+c/speed;
            //cout<<"kondo"<<next<<endl;
            double elseNext=time+x/speed;
            //cout<<"And"<<elseNext<<endl;
            if (cmp(next-elseNext)>=0){
                time=time+(x-cur)/speed;
                cur=x;
                //cout<<"go"<<1<<endl;
            }
            else {
                if (cmp((x-c)/speed-x/(speed+f))>=0){
                        cur=0;
                        time=next;
                        speed+=f;
                        //cout<<"go"<<2<<endl;
                }
                else {
                    time=time+x/speed;
                    cur=x;
                    //cout<<"go"<<3<<endl;
                }
            }
        }
        printf("Case #%d: %.9lf\n",cas++,time);
    }
    return 0;
}
