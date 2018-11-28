#include <iostream>

using namespace std;

int main(){
    int T,N,mod,ans,tmp_n;
    cin >> T;
    //N=-1;
    for(int i=1; i <= T ; ++i){
        bool digit[10]={0},flag=1;
        cin >> N;
        //N++;
        int num = 1;
        ans = 0;
        while(flag && N != 0){
            tmp_n = N * num++;
            ans = tmp_n;
            while(tmp_n!=0){
                mod = tmp_n%10;
                digit[mod]=1;
                tmp_n = tmp_n/10;
            }
            for(int j = 0 ; j < 10 ; ++j){
                if(digit[j]==1){
                    flag=0;
                }else{
                    flag=1;
                    break;
                }
            }
            //for(int j = 0 ; j < 10 ; ++j){
                //cout << digit[j] << " ";
            //}
            //cout << endl;
        }
        if(N == 0){
            cout << "Case #" << i << ": INSOMNIA"<< endl;
        }else{
            cout << "Case #" << i << ": " << ans << endl;
        }
    }

    return 0;
}

