#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
int tc;
string s;
int n;
pair<int,int> dp1[20001],dp2[20001]; // start with C, start with J.  stores best points
const int DP_NO_EXIST = -1000000000;
pair<int,int>* curr;
pair<int,int>* prevdp;

int main(){
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>s;
        n=s.size();
        curr=dp1;
        curr[0]=make_pair(0,0);
        for(int i=1;i<=n;++i){
            curr[i]=make_pair(DP_NO_EXIST,DP_NO_EXIST);
        }
        for(int ist=0;ist<n;++ist){
            prevdp=curr;
            curr=((ist%2)?dp1:dp2);
            for(int i=0;i<=n;++i){
                curr[i]=make_pair(DP_NO_EXIST,DP_NO_EXIST);
            }
            char scurr=s[ist];
            if(scurr=='C'){
                for(int i=1;i<=n;++i){
                    curr[i-1].second=max(curr[i-1].second,prevdp[i].first+10);
                }
                for(int i=0;i<n;++i){
                    curr[i+1].first=max(curr[i+1].first,prevdp[i].second);
                }
                for(int i=1;i<=n;++i){
                    curr[i-1].first=max(curr[i-1].first,prevdp[i].second+5);
                }
            }
            else{
                for(int i=1;i<=n;++i){
                    curr[i-1].first=max(curr[i-1].first,prevdp[i].second+10);
                }
                for(int i=0;i<n;++i){
                    curr[i+1].second=max(curr[i+1].second,prevdp[i].first);
                }
                for(int i=1;i<=n;++i){
                    curr[i-1].second=max(curr[i-1].second,prevdp[i].first+5);
                }
            }
            int max0=max(curr[0].first,curr[0].second);
            curr[0]=make_pair(max0,max0);
        }
        int maxel=0;
        for(int i=0;i<=n;++i){
            maxel=max(maxel,curr[i].first);
            maxel=max(maxel,curr[i].second);
        }
        printf("Case #%d: %d\n",ct,maxel);
    }
}
