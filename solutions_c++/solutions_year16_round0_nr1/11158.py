#include <iostream>
#include <stack>
#include <map>
#include <string>
#include <list>

using namespace std;

int main(int argc, const char * argv[]) {
    int test;
    int  n;
    int input;
    int digit = 0;
    int num = 0;
    list<int> ls;
    for (int j = 0; j<10; j++)
        ls.push_back(j);
    
    cin >> test;
    
    for (int i =0; i < test ; i++) {
        cout << "Case #" << i+1 << ": ";
        cin >> input;
        num = input;
        //cout << "Input" << input << endl;
        n = 2;
        if (input > 0) {
            list<int> ls;
            for (int j = 0; j<10; j++)
                ls.push_back(j);
            while (!ls.empty()) {
                int count = 0;
                int temp = num;
                while (!ls.empty() && count < to_string(num).length()) {
                    //cout << "num" << num << endl;

                    digit = temp % 10;
                    //cout << "digit" << digit << endl;
                    ls.remove(digit);
                    
                    temp = temp / 10;
                    //cout << "temp" << temp << endl;
                    count ++;
                }
                if (ls.empty())
                    cout << num << endl;
                num = input * n;
                //cout << "num" << num << endl;

                n++;
            }
        }
        else cout <<"INSOMNIA" << endl;
    }
    return 0 ;
}
