#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for(int i=0;i<t;++i){
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i+1 << ":";
        if(c==1){
            for(int j=0;j<s;j++){
                cout << ' ' << j+1;
            }
        }else{
            for(int j=0;j<s;j++){
                cout << ' ' << k/2+(j*k)+1;
            }
        }
        cout << endl;
    }
    return 0;
}
