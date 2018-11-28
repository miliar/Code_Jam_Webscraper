#include<bits/stdc++.h>
using namespace std;

set<int> st;
int demo=0;

void doCalculation(int len, int n) {
    demo= n;
    for(int i=0; i<len; i++) {
        st.insert(n%10);
        n/=10;
    }
    return;
}


int main() {

//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//    freopen("al.txt", "w", stdout);

//    clock_t time= clock();
    int t;
    cin>>t;

    int n;

    for(int i=0; i<t; i++) {
        cin>>n;
        int cnt=1;

        if(!n)
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        else {
            int len;    //= log10(n) + 1;

            while(st.size()!=10) {
                len= log10(n*cnt) + 1;
                doCalculation(len,n*cnt);
                ++cnt;
            }
            cout<<"Case #"<<i+1<<": "<<demo<<endl;
            demo= 0;
            st.clear();
        }
    }

//    time= clock() - time;
//    printf("(%.4lf) seconds\n", ((float)time)/CLOCKS_PER_SEC);

    return 0;
}
