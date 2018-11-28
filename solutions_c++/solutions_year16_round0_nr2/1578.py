#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outB.txt", "w", stdout);
    int t;
    string S;
    scanf("%d", &t);
    for(int k=1; k<=t; k++)
    {
        ll ans=0;
        cin>>S;
        vector<int>A;
        for(int i=0; i<S.size(); i++){
            if(i==0){
                if(S[i]=='-')
                    A.push_back(0);
                else
                    A.push_back(1);
            }
            else{
                if(S[i]!=S[i-1]){
                    if(S[i]=='-')
                        A.push_back(0);
                    else
                        A.push_back(1);
                }
            }
        }
        for(int i=0; i<A.size(); i++){
            if(i==0){
                if(A[i]==0){
                    ans++;
                }
            }
            else if(A[i]==0){
                ans+=2;
            }
        }
        printf("Case #%d: %lld\n", k, ans);
    }
    return 0;
}
