#include<bits/stdc++.h>
typedef long long LL;
using namespace std;
int main()
{
    int t;
    //freopen("D-small-attempt0.in","rt",stdin);
    //freopen("output.cpp","wt",stdout);
    cin>>t;
    for(int testCase=1;testCase<=t;testCase++){
        LL k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<testCase<<": ";
        if(c==1){
            LL last_index=pow(k,c);
            for(LL i=1;i<=k;i++){
                cout<<i<<" ";
            }
            cout<<endl;
            continue;
        }
        LL lastIndex=pow(k,c);
        LL oneLevelLessNodes=pow(k,c-1);
        if(c==2){
            LL twoLevelLessNodes=0;
            LL addOne=0,addTwo=0;
            for(LL i=1;i<=k;i++){
                cout<<i+addOne+addTwo<<" ";
                addOne+=oneLevelLessNodes;
                addTwo+=twoLevelLessNodes;
            }
        }
        else{
            LL twoLevelLessNodes=pow(k,c-2);
            LL addOne=0,addTwo=0;
            for(LL i=1;i<=k;i++){
                cout<<i+addOne+addTwo<<" ";
                addOne+=oneLevelLessNodes;
                addTwo+=twoLevelLessNodes;
            }
        }
        cout<<endl;
    }
    return 0;
}
