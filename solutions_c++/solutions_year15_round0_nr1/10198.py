#include<iostream>

using namespace std;

int main() {
    int T, S, cnt, tmp;
    char str[1000];
    cin >> T;
    for (int i=1; i<=T; i++) {
        cin >> S;
        cnt = 0;
        cin>>str;
        int arr[S+1];
        for (int j=0;j<=S;j++) {
            arr[j] = str[j] - '0';
        }
        tmp = arr[0];

        for(int j=1; j<=S; j++) {
            if (tmp >= j) {
                tmp += arr[j];
            }
            else {
                cnt = cnt + (j-tmp);
                tmp = j + arr[j];
            }
        }

        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }

    return 0;
}
