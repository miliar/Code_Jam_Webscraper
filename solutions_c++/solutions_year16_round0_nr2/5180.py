#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    int a;
    string pancakes;
    for(int i = 1; i <= T; i++){
        cin >> pancakes;
        a = 0;
        for(int y = 0; y < (pancakes.size() - 1); y++){
            if(pancakes[y] != pancakes[(y+1)])
                a++;
        }
        if(pancakes[(pancakes.size() - 1)] != '+')
            a++;
        cout << "Case #" << i << ": " << a << endl;
}
return 0;
}