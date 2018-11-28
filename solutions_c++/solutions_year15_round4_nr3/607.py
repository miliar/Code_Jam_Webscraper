#include<bits/stdc++.h>
using namespace std;


void solve(){
    int n;
    cin >> n;
    vector<vector<int> > v;
    string tmp;
    getline(cin,tmp);
    map<string,int> mpp;
    int cnt=1;
    for(int i = 0 ; i < n ; ++ i ){
        string str;
        getline(cin,str);
        stringstream ss;
        ss << str;
        vector<int> vs;
        while(ss>>str){
            if(str.size()>0){
                if(!mpp.count(str))mpp[str]=cnt++;

                vs.push_back(mpp[str]);
            }


            str="";
        }
        v.push_back(vs);
    }
/*
    for(auto vs:v){
        for(auto s:vs){
            cout << s << " " ;
        }
        cout << endl;
    }
*/
    int ans=10000;
    //set<int> eng ;
    vector<bool> eng(cnt+10,false);
    for(auto x : v[0] ) eng[x]=true;
    //set<int> frn;
    vector<bool> fng(cnt+10,false);
    for(auto x : v[1] ) fng[x]=true;
    int mans = 0 ;

    for(int i = 0 ; i < ( 1<< (n-2) ) ; i++ ){
        vector<bool> engg=eng;
        vector<bool> fngg=fng;
        int mask=i*4;
        for(int j = 2 ; j < n ; ++ j ){
            if( mask&(1<<j)){
                for(auto x : v[j]){
                    engg[x]=true;
                }
            }
            else{
                for( auto x : v[j]){
                    fngg[x]=true;
                    /*
                    if(alr.find(x)==alr.end()&&frn.find(x)==frn.end()){
                        alr.insert(x);
                        if(word.find(x)!=word.end()||eng.find(x)!=eng.end())cnt++;
                    }*/
                }
            }
        }
        int mans=0;
        for(int q = 0 ; q < cnt ; ++ q ){
            if(engg[q]&fngg[q])mans++;
        }
        /*
        int mask= i<<2;
        set<int> word;
        for(int j = 2 ; j < n ; ++ j ){
            if( mask&(1<<j)){
                for(auto x:v[j])word.insert(x);
            }
        }
        int cnt = 0 ;
        set<int> alr;
        for(int j = 2 ; j < n ; ++ j ){
            if( mask&(1<<j)){}
            else{
                for( auto x : v[j]){
                    if(alr.find(x)==alr.end()&&frn.find(x)==frn.end()){
                        alr.insert(x);
                        if(word.find(x)!=word.end()||eng.find(x)!=eng.end())cnt++;
                    }
                }
            }
        }
        for(int j = 2 ; j < n ; ++ j ){
            if( mask&(1<<j)){
                for(auto x:v[j]){
                    if(alr.find(x)==alr.end()&&frn.find(x)!=frn.end()&&eng.find(x)==eng.end()){
                        alr.insert(x);
                        cnt++;
                    }
                }
            }
        }*/
        //cout << i << " " << cnt+mans << endl;
        ans=min(ans,mans);
    }
    cout << ans << endl;
}

int main(){
    //freopen("Csample.txt","r",stdin);
    freopen("C-small-attempt3"".in","r",stdin);
    freopen("C-small-attempt3"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
