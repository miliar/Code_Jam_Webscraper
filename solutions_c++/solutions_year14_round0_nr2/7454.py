#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    int t,cnt=0;
    double c,f,x,tmp,sum_time,time_use;
    double produce,cur,prev;
    cin >> t;
   // cout.precision(7);
    //cout.setf( ios::fixed, ios::floatfield );
    while((t--)!=0){
        cin >> c >> f >> x;
        produce = 2;
        sum_time=0;
        prev = x/produce;
        while(1){
            sum_time+=(c/produce);
            produce+=f;
            time_use = x/produce;
            cur = sum_time + time_use;
           // cout << prev << " " << cur << endl;
            if(prev<cur)break;
            prev=cur;
        }
        cnt++;
        printf("Case #%d: %.7lf\n",cnt,prev);
        //cout << "Case #"<< cnt << ":" << prev << endl;
    }
    return 0;
}
