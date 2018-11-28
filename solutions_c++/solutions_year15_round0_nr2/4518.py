#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int sol;

int main(){
    int t,tc=0,n,tt;cin>>t;
    while(t--){
        
        cin>>n;
        vector<int> v(n);
        int sol = 0,div=0;
        for(int i=0;i<n;i++){cin>>v[i];}
        sort(v.begin(),v.end());
        sol = v[v.size()-1];
        queue<pair< vector<int>,int> > Q;
        Q.push({v,div});
        while(!Q.empty()){
            vector<int> tmp = Q.front().first;
            
            int cur = Q.front().second;
            //cout<<"cur: "<<cur<<" tmp: ";
            //for(int j=0;j<tmp.size();j++)cout<<tmp[j]<<" ";cout<<endl;
            
            sol = min(sol,cur+tmp[tmp.size()-1]);
            Q.pop();
            if(cur>=sol)continue;
            
            for(int i=1;i<tmp[tmp.size()-1];i++){
                vector<int> tt = tmp;
                tt[tt.size()-1] -= i;
                tt.push_back(i);
                sort(tt.begin(),tt.end());
                //for(int j=0;j<tt.size();j++)cout<<tt[j]<<" ";cout<<endl;
                
                if(tt[tt.size()-1] > 1){
                    if(cur+1 < sol)
                        Q.push({tt,cur+1});
                }
                    
                
            }
        }

        
        cout<<"Case #"<<++tc<<": "<<sol<<endl;
    }
}
