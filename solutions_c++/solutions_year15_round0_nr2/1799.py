#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        vector<int> pank;
        int d,p;
        int maxPank=-1;
        cin>>d;
        for(int i=0;i<d;i++){
            cin>>p;
            if(p>maxPank)maxPank=p;
            pank.push_back(p);
        }
        int ans=maxPank;
        for(int i=1;i<maxPank;i++){
            int tmp=0;
            for(int j=0;j<pank.size();j++){
                if(pank[j]>i){
                    tmp+=pank[j]/i;
                    tmp--;
                    if(pank[j]%i)tmp++;
                }
            }
            ans=min(ans,tmp+i);
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
}
