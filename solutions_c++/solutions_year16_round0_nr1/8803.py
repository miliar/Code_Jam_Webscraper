#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string to_string(long long n){
    stringstream ss;
    ss << n;
    return ss.str();
}

int main()
{
    int T;
    cin >> T;
    freopen("A.txt","w",stdout);

    for(int i = 1; i <= T; i++){
        long long N;
        cin >> N;

        if(N == 0){
            cout << "Case #"<< i <<": INSOMNIA" << endl;
            continue;
        }

        int num = 0;

        string temp = to_string(N);

        for(int j = 0; j < temp.size(); j++){
            num |= (int)pow(2,temp[j]-'0');
        }

        int k = 2;
        while(num != 1023){
            temp = to_string(N*k);
            for(int j = 0; j < temp.size(); j++){
                num |= (int)pow(2,temp[j]-'0');
            }
            k++;
        }
        cout << "Case #"<< i <<": " << temp << endl;
    }

    return 0;
}
