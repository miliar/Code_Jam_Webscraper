#include <iostream>
#include <fstream>

using namespace std;

int N, a, b, c;

int main() {
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> a >> b >> c;
        int ans = ((b + c - 1) / c) * a + (c - 1);
        cout << "Case #" << (i+1) << ": " << ans << endl;
    }
    
    return 0;
}