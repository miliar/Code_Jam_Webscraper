#include "iostream"

using namespace std;

int main() {
    int T=0,Smax;
    char str[8];
    cin >> T;
    for(int i=1;i <= T; i++) {
        cin >> Smax;
        cin >> str;
        int reqFriends = 0;
        int standing = 0;
        for (int j=0; str[j] != '\0'; j++) {
            if(str[j] == 48) continue;
                int Si=(str[j]-48);
                if(standing >= j) {
                    standing += Si;
                } else {
                    reqFriends += (j - standing);
                    standing += (str[j]-48)+reqFriends;
                }
        }
        cout << "Case #" << i << ": " << reqFriends << endl;
    }
}