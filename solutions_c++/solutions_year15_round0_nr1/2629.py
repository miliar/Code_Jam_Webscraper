#include <iostream>
#include <string>
using namespace std;

void printResult(int caseNum, int result){
    cout<<"Case #"<<caseNum<<": "<<result<<endl;
}

int main(int argc, const char * argv[])
{
    int T;
    cin>>T;
    for (int kk = 1; kk <= T; ++ kk) {
        int smax;
        string s;
        cin>>smax;
        cin>>s;
        int sum = 0;
        int rest = 0;
       
        sum += s[0] - '0';
        for (int i = 1; i <= smax; ++ i) {
            int t = s[i] - '0';
            if (sum < i) {
                rest += i - sum;
                sum += i - sum;
            }
            sum += t;
        }
        printResult(kk, rest);
    }
}

