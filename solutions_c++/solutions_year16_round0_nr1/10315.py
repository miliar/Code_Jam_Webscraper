#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int k=1;k<=t;k++){
        int n;
        cin >> n;
        int initial_value = n;
        int num[10] = {0};
        for(int i=0;i<100;i++){
            int tmp = n;
            while(tmp>=1){
                int r=0;
                r=tmp%10;
                //cout << tmp << " ";
                num[r] = 1;
                tmp/=10;
            }
            //getchar();
            int flag = 1;
            for(int j = 0;j<10;j++){
                //printf("j = %d num[j] = %d\n",j,num[j]);
                if(num[j]==0){
                    flag = 0;
                    break;
                }
            }
            if(flag==0){
                n=initial_value*(i+2);
            }
            else{
                cout << "Case #" << k << ": " << n << endl;
                break;
            }
        }
        for(int i=0;i<10;i++){
            if(num[i]==0){
                cout << "Case #" << k << ": INSOMNIA" << endl;
                break;
            }
        }
    }
    return 0;
}