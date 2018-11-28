#include <iostream>
#include <string>

using namespace std;

int main(int arg, char** argv)
{
    int N, n;
    string a;
    cin >> N;
    size_t first;
    size_t last;
    for (int i = 1; i < N + 1; i++) {
        //cout << "#@#@#@# "<< i << " #@#@#@#"<< endl; 
        cin >> n;
        cin >> a;
        first = a.find_first_of('0');
        last = a.find_last_of('0');
        size_t num = a.find_first_not_of('0');
        //cout << "!!" << num << endl;
        //cout << "n: " << n << ", a: " << a << endl;
        if (first == string::npos){
            cout << "Case #" << i << ": 0" << endl; 
        } else if (first == last || first != 0 || !((first < num) &&  (num < last))) {
            //cout << "first: " << first << endl;
            //cout << "last: " << last << endl;
            int sum1 = 0;
            for (int j = 0; j < first; ++j){
                sum1 += a[j] - '0';
            }
            int sum2 = 0;
            for (int k = 0; k < last; ++k){
                sum2 += a[k] - '0';
            }
            int answer;
            answer = last + 1 - sum1 - ( sum2 - sum1);
            if (answer < 0){
                cout << "Case #" << i <<": 0" << endl;
            } else {
                cout << "Case #" << i << ": " << answer << endl;
            }
        } else {
            int sum1 = num;
            for (int j = 0; j < first; ++j){
                sum1 += a[j] - '0';
            }
            int sum2 = num;
            for (int k = 0; k < last; ++k){
                sum2 += a[k] - '0';
            }
            int answer;
            answer = last + 1 - sum1 - ( sum2 - sum1);
            if (answer < 0){
                cout << "Case #" << i <<": " << num << endl;
                //cout << "answer < 0 : " << answer <<", " << num << endl;
            } else if ( answer < num) {
                cout << "Case #" << i << ": " << num+answer << endl;
                //cout << "answer < num : "<< answer <<", " << num << endl;
            }else {
                cout << "Case #" << i << ": " << num+answer << endl;
                //cout << "answer randomly + 1" << answer <<", " << num<< endl;
            }
        }
    }

    return 0;
}
