#include<iostream>
#include<vector>
#include<algorithm>
typedef struct S{
    char c;
    int num;
}st;
using namespace std;

inline int midnum(vector<int>& q){
    return q[(q.size()/2)];
}

bool mysort(int a, int b){
    return (a<b);
}

int moves(vector<int>& q){
    sort(q.begin(), q.end(), mysort);
    int w=midnum(q);
    int re=0;
    for(int i=0 ; i<q.size() ; i++){
        re+=abs(q[i]-w);
    }
    return re;
}

int main(){
    vector<vector<st> > strings;
    vector<st> q;
    string tmp;
    int T,t=0,N,now,ans;
    cin>>T;
    while(++t <= T){
        strings.clear();
        cin>>N;ans=0;
        for(int i=0 ; i<N ; i++){

            q.clear();
            cin>>tmp;
            //now=0;

            st temp;
            temp.c=tmp[0];
            temp.num=1;
            q.push_back(temp);
            for(int j=1 ; j<tmp.size() ; j++){
                //cout<<"j="<<j<<", "<<tmp[j]<<endl;
                if(tmp[j] == q.back().c){
                    //cout<<tmp[j]<<"+1"<<endl;
                    q.back().num++;
                    //cout<<q.back().num<<endl;
                }
                else{
                    //cout<<" "<<q.back().num<<"\nQQQQ"<<tmp[j]<<endl;
                    temp.c=tmp[j];
                    temp.num=1;
                    q.push_back(temp);
                }
            }
            //cout<<q.size()<<endl;
            strings.push_back(q);
            //cout<<"s.size="<<strings.size()<<endl;
        }

        int tmpi=strings[0].size();;
        bool P=true;
        //cout<<"QQ"<<tmpi<<endl;
        for(int i=1 ; P and i<N ; i++){
            //cout<<"i="<<i<<", "<<strings[i].size()<<endl;
            if(strings[i].size() != tmpi){
                //cout<<"GG\n";
                P=false;
            }
        }
        for(int i=0 ; P and i<strings[0].size() ; i++){
            for(int j=1 ; j<N ; j++){
                if(strings[j][i].c != strings[0][i].c){
                    //cout<<"F\n";
                    P=false;
                }
            }
        }
        if(P){
            vector<int> tmpv;
            for(int i=0 ; i<strings[0].size() ; i++){
                tmpv.clear();
                for(int j=0 ; j<N ; j++){
                    tmpv.push_back( strings[j][i].num );
                }
                //cout<<strings[0][i].c<<" "<<moves(tmpv)<<endl;
                ans+=moves(tmpv);
            }
        }
        if(P) cout<<"Case #"<<t<<": "<<ans<<endl;
        else cout<<"Case #"<<t<<": Fegla Won"<<endl;

    }
}

