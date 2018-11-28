#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-practice.in","r",stdin);
    freopen("A-small-practice.out","w",stdout);

    int count = 0;
    int T;
    cin>>T;
    int Smax;
    string S;
    while(T--){
        cin>>Smax>>S;
        //cout<<Smax<<"  "<<S<<endl;
        int cnt = 0;
        int sum = S[0]-'0';
        for(int i=1;i<=Smax;++i){
            if(S[i]!='0'&&sum < i){
                cnt += i - sum;
                sum += cnt;
            }
            sum += S[i] - '0';
        }

        cout<<"Case #"<<++count<<": ";
        cout<<cnt<<endl;
    }

    return 0;
}
