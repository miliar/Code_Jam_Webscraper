#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stdio.h>
using namespace std;

int main(int argc, char* argv[]){
    char* filename = argv[1];
    //cout << filename << endl;
    fstream fp;
    int T;

    fp.open(filename, ios::in);
    if(!fp){
        cout <<"fail to open" << filename <<endl;
    }
    fp >> T ;
    double guess;
    double C,F,X;
    double init = 2.0;
    double time =0.0;
    for(int t=0; t<T; t++){
        fp >> C >> F >> X;
        vector<double> arr;

        int k=0;
        double ans;

        while(1){
            //arr[k] = k*C + X / (2+K*F);
            time = 0.0;
            double init2 = init;
            for(int i=0; i<k;i++){
                time += C / init2;
                init2 += F;
            }
            time += X / init2;
            arr.push_back(time);

            if(k>=1 && arr[k] > arr[k-1]){
                ans = arr[k-1];
                break;
            }
            k++;
        }
        //cout << "Case #" << (t+1) << ": "; << ans << endl;
        printf("Case #%d: %.7lf\n",t+1,ans);
    }


    return 0;
}
