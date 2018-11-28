#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    string temp;
    getline (cin,temp);
    T = stoi(temp);
    int X = 1;
    while(X <= T){
        bool digits[10], flag = true;
        for(int i = 0; i < 10; i++){ digits[i] = 0; }
        int j = 1;
        string M,N;
        getline (cin,M);

        while(flag){
            if(stoi(M) == 0) { cout << "Case #" << X <<": INSOMNIA" << endl; break; }
            N = to_string(stoi(M)*j);
            for(int i = 0; i < N.size(); i++){ digits[N[i]-'0']= true; }
            int sum = 0;
            for(int i = 0; i < 10; i++){
                sum += digits[i];
                if(sum == 10) {
                    flag = false;
                    cout << "Case #" << X <<": " << N << endl;
                }
            }
            j++;
        }
        X++;
    }
    return 0;
}
