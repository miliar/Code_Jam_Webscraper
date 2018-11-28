#include<iostream>
#include<map>
#include<vector>
using namespace std;

typedef long long LL;
typedef pair<int,int> PLL;



int T;
int E,R,N,V;
long long res = 0;



int main(){
    int i,j,k;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>E>>R>>N;
        if(R>=E){
            res = 0;
            for(i=0;i<N;++i){
                cin>>V;
                res+=V;
            }
            res*=E;
        }
        else{
            cin>>V;
            vector<PLL> v;
            v.push_back(make_pair(V,E));
            for(i=1;i<N;++i){
                cin>>V;
                int rem = E-R;
                int cur = R;
                while(v.back().first<V){
                    if(v.back().second<=rem){
                        cur+=v.back().second;
                        rem -=v.back().second;
                        v.pop_back();
                    }
                    else{
                        v.back().second-=rem;
                        cur+=rem;
                        break;
                    }
                    
                    
                }
                v.push_back(make_pair(V,cur));
            }
            res = 0;
            for(i=0;i<v.size();++i){
                long long t1 = v[i].first;
                t1*=v[i].second;
                res+=t1;
            }
        }
        cout<<"Case #"<<cs<<": "<<res<<endl;
        cerr<<"Case #"<<cs<<": "<<res<<endl;
    }
    return 0;
}

