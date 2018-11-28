#include<bits/stdc++.h>
using namespace std;

bool isPlus(string str) {
    for(int i=0; i<str.size(); i++) {
        if(str[i]=='-')
            return false;
    }
    return true;
}

int main() {

//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);

//    clock_t timer= clock();
    int t;
    cin>>t;

    string str;
    for(int i=0; i<t; i++) {
        cin>>str;
        int cnt=0;

        if(isPlus(str)) {
            cout<<"Case #"<<i+1<<": "<<cnt<<endl;
        } else {
            char c= str[0];
            bool flag;

            for(int j=1; j<str.size(); j++) {
                if(str[j]!=c) {
                    c= str[j];
                    ++cnt;
                }
            }

            if(c=='-')
                ++cnt;
            cout<<"Case #"<<i+1<<": "<<cnt<<endl;
        }
        str.clear();
    }

//    timer= clock() - timer;

//    printf("(%lf) sec\n", ((float)timer)/CLOCKS_PER_SEC);

    return 0;
}
