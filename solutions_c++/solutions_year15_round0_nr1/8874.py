#include<iostream>

using namespace std;

char a[1000];

int inviteFriends(int Smax){
    int sum = (a[0]-'0'), friends = 0;
    for(int i = 1; i < Smax+1; ++i){
        if(sum < i){
            friends += (i - sum);
            sum += (i - sum);
        }
        sum += (a[i] - '0');
    }
    return friends;
}

int main(){
    int T;
    int Smax;

    cin >> T;

    for(int t = 0; t < T; ++t){
        cin >> Smax >> a;
        cout << "Case #"<< (t+1) <<": " << inviteFriends(Smax) << endl;
    }
}

