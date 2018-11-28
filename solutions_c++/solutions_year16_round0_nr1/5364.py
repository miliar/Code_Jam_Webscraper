#include<iostream>
#include<vector>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int itrS = 0; itrS < t; itrS++){
        long long int n;
        cin >> n;
        int cnt = 0;
        vector<bool> key(10, true);
        cout << "Case #" << itrS + 1 << ": ";
        if(n == 0){
            cout << "INSOMNIA\n";
            continue;
        }
        long long int N = n;
        while( cnt != 10){
            //cout << N << " # " << cnt << endl;
            long long int tmp = N;
            while(tmp > 0){
                int val = tmp % 10;
                if(key[val] == true){
                    cout<<"D: "<<val<<"->"<<N<<endl;
                    cnt++;
                    key[val] = false;
                }
                tmp /= 10;
            }
            if(cnt != 10)
                N += n;
        }
        if(cnt == 10)   cout << N;
        cout<<endl;
    }
    return 0;
}
