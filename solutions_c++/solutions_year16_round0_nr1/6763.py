#include<iostream>
#include<unordered_set>
using namespace std;

class Solution {
public :
    bool isEnough(unordered_set<int>& appeared, long long int num){
        while (num > 0) {
            appeared.insert(num-num/10*10);
            if (appeared.size() == 10) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
    long long int getCounter(long long int num){
        unordered_set<int> appeared;
        long long int sum = num;
        while (1) {
            if(isEnough(appeared, sum)){
                return sum;
            }else{
                sum += num;
            }
        }
    }
    
};
int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        long long int N;
        cin >> N;
        Solution solution;
        if (N == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }else{
            cout << "Case #" << i << ": " << solution.getCounter(N) << endl;
        }
    }
    return 0;
}
