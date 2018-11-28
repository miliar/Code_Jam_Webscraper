#include <iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    int Tcnt = 1;
    for(; T; T--,Tcnt++) {
        int N;
        string line;
        cin>>N>>line;
        int standup = 0;
        int ans = 0;
        for(int i=0; i<(int)line.length(); i++) {
            if(standup < i) {
                ans += i-standup;
                standup = i;
            }
            standup += line[i]-'0';
        }
        cout<<"Case #"<<Tcnt<<": "<<ans<<endl;
    }
    return 0;
}

