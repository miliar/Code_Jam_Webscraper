/// #sh

#include<bits/stdc++.h>

using namespace std;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        //freopen("A_large.out", "w", stdout);
    #endif // ONLINE_JUDGE

    int test;
    scanf("%d", &test);
    for(int t=1; t<=test; ++t){
        printf("Case #%d: ", t);

        string str;
        cin >> str;

        string temp = "";
        temp += str[0];
        char first = str[0];

        for(int i=1; i<str.size(); ++i){
            if(str[i] < first)
                temp += str[i];
            else{
                temp = str[i] + temp;
                first = str[i];
            }
        }
        cout << temp << "\n";
    }
}
