#include<bits/stdc++.h>
#define SIZE 105
using namespace std;
int main()
{
    int t;
    //freopen("B-large.in","rt",stdin);
    //freopen("output.cpp","wt",stdout);
    scanf("%d",&t);
    for(int testCase=1;testCase<=t;testCase++){
        string s;
        cin>>s;
        cout<<"Case #"<<testCase<<": ";
        int n=s.length();
        vector<pair<int,int> >states(n+2);
        states[0].first=states[0].second=0;
        if(s[0]=='+'){
            states[0].first=0;
            states[0].second=1;
        }
        else{
            states[0].first=1;
            states[0].second=0;
        }
        for(int i=1;i<n;i++){
            if(s[i]=='+'){
                states[i].first=states[i-1].first;
                states[i].second=states[i-1].first+1;
            }
            else{
                states[i].first=states[i-1].second+1;
                states[i].second=states[i-1].second;
            }
        }
        cout<<min(states[n-1].first,states[n-1].second+1)<<endl;
    }
    return 0;
}
