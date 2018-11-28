#include <iostream>

using namespace std;

int T;

int N;
string S;



void init(){

};

int solve(){
    int ans = 0;
    int sum = 0;
    for(int i=0; i<=N; i++){
        sum += S[i]-'0';
        if (sum <=i){
            ans += i-sum+1;
            sum += i-sum+1;
        }
    };

    return ans;
};

int main()
{
    cin >>T;
    int t = 0;
    while(T--){
        cin >>N >>S;
        init();
        t++;
        cout << "Case #"<<t<<": "<<solve()<<endl;
    }

    return 0;
}
