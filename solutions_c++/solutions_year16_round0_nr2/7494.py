#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream ansfile;
    ansfile.open("answer_2.txt");

    long long t, counter_t = 1;
    cin>>t;
    while(counter_t <= t) {

        unsigned long long i = 0,ans = 0;
        string st;
        cin>>st;

        while(i < st.size()) {

        while(st[i] == '+' && i < st.size()) {
                i++;
        }

        if( i >= st.size())
            break;

        if( i == 0 ) {
                while(st[i] == '-' && i < st.size())
                    i++;
                ans++;
            }
        else {
                while(st[i] == '-' && i < st.size())
                    i++;
                ans+=2;
            }
        }

        ansfile<<"Case #"<<counter_t<<": "<<ans<<endl;
        counter_t++;
    }
    ansfile.close();
return 0;
}
