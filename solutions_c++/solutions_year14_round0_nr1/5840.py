#include<iostream>
#include<vector>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        bool ans[20];
        for(int i=0;i<20;i++)ans[i]=false;
        int vans;
        cin>>vans;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                int tmp;
                cin>>tmp;
                if(vans==i+1)ans[tmp-1]=true;
            }
        }
        cin>>vans;
        vector<int>poss;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                int tmp;
                cin>>tmp;
                if(vans==i+1){
                    if(ans[tmp-1]){
                        poss.push_back(tmp);
                    }
                }
            }
        }
        cout<<"Case #"<<++cas<<": ";
        if(poss.size()==0)cout<<"Volunteer cheated!"<<endl;
        else if(poss.size()>1)cout<<"Bad magician!"<<endl;
        else cout<<poss[0]<<endl;
        poss.clear();
    }
}
