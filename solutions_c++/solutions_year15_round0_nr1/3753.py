#include <iostream>
using namespace std;

const int maxn=1005;

int shy[maxn];

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    for (int ttt=1; ttt<=T; ttt++)
    {
        int N;
        cin>>N;
        string S;
        cin>>S;
        for (int i=0; i<S.size(); i++) shy[i]=(S[i]-'0');
        int out=0, standing=shy[0];
        for (int i=1; i<=N; i++)
        {
            if (standing<i) {out+=i-standing; standing=i;}
            standing+=shy[i];
        }
        cout<<"Case #"<<ttt<<": "<<out<<"\n";

    }
}
