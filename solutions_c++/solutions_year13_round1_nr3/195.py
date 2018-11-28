#include<iostream>
#include<set>
#include<vector>
#include<map>
using namespace std;

int T;
int R = 100;
int N = 3;
int M = 5;
int K = 7;

bool ok(vector<int> v1,vector<int> v2){
    set<int> s(v1.begin(),v1.end());
    for(int i=0;i<v2.size();++i){
        if(s.count(v2[i])==0) return false;
    }
    return true;
    
}

int main(){
    int i,j,k,l,m;
    map<vector<int>,int> mm;
    for(i=2;i<=M;++i){
        for(j=i;j<=M;++j){
            for(k=j;k<=M;++k){
                set<int> s;
                for(l=0;l<8;++l){
                    int mul = 1;
                    if(l&1) mul*=i;
                    if(l&2) mul*=j;
                    if(l&4) mul*=k;
                    s.insert(mul);
                }
                vector<int> v(s.begin(),s.end());
                mm[v] = i*100+j*10+k;
            }
        }
    }
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=1;++cs){
        cin>>T>>T>>T>>T;
        cout<<"Case #"<<cs<<":\n";
        for(i=0;i<R;++i){
            set<int> ss;
            for(j=0;j<K;++j){
                cin>>T;
                ss.insert(T);
            }
            vector<int> vv(ss.begin(),ss.end());
            bool flag = true;
            for(map<vector<int>,int>::iterator it = mm.begin();it!=mm.end();++it){
                if(ok(it->first,vv)){
                    cout<<it->second<<endl;
                    cerr<<it->second<<endl;
                    flag = false;
                    break;
                }
            }
            if(flag) cerr<<"error\n";
            
        }
        
        
    }
    return 0;
}

