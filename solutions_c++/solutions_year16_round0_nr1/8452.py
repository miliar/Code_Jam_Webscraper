#include<bits/stdc++.h>
#define read(tag) freopen(tag,"r",stdin)
#define rite(tag) freopen(tag,"w",stdout)
using namespace std;

set<int>dig;
void chk(int Q)
{
    int temp=Q;
    while(temp)
    {
        int el=temp%10;
        dig.insert(el);
        temp/=10;
    }
}
int main()
{
    //read("read.in");
    //rite("Ans.out");
    int N,K,cnt=1,T; cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>N; cnt=1; K=0;
        if(N==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        dig.clear(); chk(N);
        while(dig.size()!=10)
        {
            cnt++;
            K=N*cnt;
            chk(K);
        }
        cout<<"Case #"<<i<<": "<<N*cnt<<endl;
    }
    return 0;
}
