#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int T;
    double C,F,X,time1,time2,cookie,buying_cur,buying_old,time_old,time_cur;
    bool flag;
    cin >> T;
    for(int index = 1; index <= T ; ++index){
        cin >> C >> F >> X;
        cookie = 2.0;
        flag = true;

        time1 = X/cookie;

        ///**********************************
        buying_cur = C/cookie;///เวลาในการผลิต cookie เพื่อขยายโรงงาน
        cookie += F;///ขยายโรงงานแล้ว
        time2 = (X/cookie) + buying_cur;///เวลาในการผลิต cookie ให้ได้ตามยอด + เวลาที่เสียไปในการขยายโรงงาน
        ///************************************
        //cout << time1 << " : " << time2 << endl;
        if(time1 < time2){
            cout << fixed << setprecision(7);
            cout << "Case #" << index << ": " << time1 << endl;
        }else{
            time_old = time2;///เก็บเวลาเก่าไว้
            buying_old = buying_cur;
            //cout << "time_old = " << time_old << endl;
            //cout << "buying_old = " << buying_old << endl;
            while(flag){
                buying_cur = C/cookie;///เวลาในการผลิต cookie เพื่อขยายโรงงาน
                //cout << "buying_cur = " << buying_cur << endl;
                cookie += F;///ขยายโรงงานแล้ว
                time_cur = (X/cookie) + buying_cur;///เวลาในการผลิต cookie ให้ได้ตามยอด + เวลาที่เสียไปในการขยายโรงงาน
                //cout << "time_cur = " << time_cur << endl;
                time_cur += buying_old;
                //cout << "time_cur2 = " << time_cur << endl;
                if(time_old < time_cur){
                    cout << fixed << setprecision(7);
                    cout << "Case #" << index << ": " << time_old << endl;
                    flag = false;
                }else{
                    time_old = time_cur;///เก็บเวลาเก่าไว้
                    buying_old += buying_cur;
                }
            }
        }
    }
    return 0;
}
