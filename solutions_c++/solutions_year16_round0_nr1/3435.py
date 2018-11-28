#include<iostream>
#include<set>
using namespace std;


set<int> getDigit(int input) {
    set<int> ans;
    while(input != 0) {
        ans.insert(input % 10);
        input /= 10;
    }
    return ans;
}

string calc(int input){
    if(input == 0)
        return "INSOMNIA";
    int i = 1;
    set<int> state;
    while(state.size() != 10) {
        for (int digit : getDigit(input * i)) {
            state.insert(digit);
        }
        if(state.size() == 10)
            break;
        i++;
    }
    return to_string(input * i);
}
int main() {
    int numCase = 1000000;
    cin >> numCase; 
    for (int i = 0; i < numCase; i++) {
        int val = i;
        cin >> val;
        cout <<"Case #"<<(i+1)<<": "<<calc(val)<<endl;
    }
}
