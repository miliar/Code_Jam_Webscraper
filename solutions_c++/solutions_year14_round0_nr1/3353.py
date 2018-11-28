#include <iostream>
#include <cstdio>

using namespace std;

#define N 4

bool ori[17];

int main()
{
//    freopen("D:\\A-small-attempt0.in","r",stdin);
//    freopen("D:\\gcj_a.txt","w",stdout);
    int fc,sc,T,tmp;
    cin >> T;
    for (int cas=0;cas<T;cas++){
        int ct = 0;
        int record;
        fill(ori,ori+17,false);
        cin >> fc;
        for (int i=1;i<=N;i++){
            for (int j=0;j<N;j++){
                cin >> tmp;
                if (i==fc){
                    ori[tmp] =true;
                }
            }
        }
        cin >> sc;
        for (int i=1;i<=N;i++){
            for (int j=0;j<N;j++){
                cin >> tmp;
                if (i==sc){
                    if (ori[tmp]){
                        ct++;
                        record = tmp;
                    }
                }
            }
        }
        cout << "Case #"<<cas+1<<": ";
        if (ct==0){
            cout << "Volunteer cheated!" << endl;
        } else {
            if (ct==1){
                cout << record << endl;
            } else {
                cout << "Bad magician!"<< endl;
            }
        }
    }
    return 0;
}
