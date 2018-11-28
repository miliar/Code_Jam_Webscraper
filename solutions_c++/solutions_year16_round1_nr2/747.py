
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef long long LL;

#define INF 100000000

bool check(vector< vector<int> >& mp,vector< vector<int> >& lst,vector<bool>& vst){
    int N = mp.size();
    vst.resize(N*2);
    for(int i=0;i<2*N;i++) vst[i]=false;
    for(int i=0;i<lst.size();i++){
        bool ok = false;
        for(int r=0;r<N;r++){
            if(vst[r]) continue;
            if(ok) break;
            bool rowOk = true;
            for(int c=0;c<N;c++) if(mp[r][c]!=lst[i][c]) {rowOk=false;break;}
            if(rowOk){
                ok = true;
                vst[r] = true;
            }
        }
        for(int c=0;c<N;c++){
            if(vst[c+N]) continue;
            if(ok) break;
            bool colOk = true;
            for(int r=0;r<N;r++) if(mp[r][c]!=lst[i][r]) {colOk=false;break;}
            if(colOk){
                ok = true;
                vst[c+N] = true;
            }
        }
        if(!ok) return false;
    }
    return true;
}

bool check(vector< vector<int> >& mp,vector< vector<int> >& lst){
    int N = mp.size();
    vector<bool> vst(N*2);
    return check(mp,lst,vst);
}

void solve(vector< vector<int> >& lst,int N,vector< vector<int> >& mp){
    ///cout<<"here "<<N<<endl;
    if(N==1){
        mp.resize(1);
        mp[0].resize(1);
        mp[0][0] = lst[0][0];
        return;
    }
    mp.resize(N);
    for(int i=0;i<N;i++) mp[i].resize(N);
    int mn=INF,mx=-1;
    for(int i=0;i<2*N-1;i++) {
        mn=min(mn,lst[i][0]);
        mx=max(mx,lst[i][N-1]);
    }
    vector<int> mnId,mxId;
    for(int i=0;i<2*N-1;i++){
        if(mn==lst[i][0]) mnId.push_back(i);
        if(mx==lst[i][N-1])mxId.push_back(i);
    }
    cout<<"H:"<<N<<" "<<mnId.size()<<" "<<mxId.size()<<endl;
    if(mnId.size()>=2){
        for(int i=0;i<N;i++){
            mp[0][i] = lst[mnId[0]][i];
            mp[i][0] = lst[mnId[1]][i];
        }
///for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<" -!"<<endl;}
        vector< vector<int> > small;
        vector< vector<int> > newList(N*2-3);
        int pos = 0;
        for(int i=0;i<2*N-1;i++){
            if(i != mnId[0] && i!=mnId[1]){
                for(int ii=1;ii<N;ii++) newList[pos].push_back(lst[i][ii]);
                pos++;
            }
        }
        solve(newList,N-1,small);
        ///cout<<"here- "<<N<<endl;
        for(int i=1;i<N;i++) for(int j=1;j<N;j++){
            mp[i][j] = small[i-1][j-1];
        }
        ///for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<" !!"<<endl;}
        ///cout<<"herexxx "<<N<<endl;
        if(check(mp,lst)) return;
        ///cout<<"hereddd "<<N<<endl;
        for(int i=1;i<N;i++) for(int j=1;j<N;j++){
            mp[i][j] = small[j-1][i-1];
        }
        if(check(mp,lst)) return;
        cout<<N<<" -!!!!!!!"<<endl;
        return;
    }
    else{
        for(int i=0;i<N;i++){
            mp[N-1][i] = lst[mxId[0]][i];
            mp[i][N-1] = lst[mxId[1]][i];
        }
///for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<" -!"<<endl;}
        vector< vector<int> > small;
        vector< vector<int> > newList(N*2-3);
        int pos = 0;
        for(int i=0;i<2*N-1;i++){
            if(i != mxId[0] && i!=mxId[1]){
                for(int ii=0;ii<N-1;ii++) newList[pos].push_back(lst[i][ii]);
                pos++;
            }
        }
        solve(newList,N-1,small);
        ///cout<<"here- "<<N<<endl;
        for(int i=0;i<N-1;i++) for(int j=0;j<N-1;j++){
            mp[i][j] = small[i][j];
        }
        ///for(int i=0;i<N;i++) {for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<" !!"<<endl;}
        ///cout<<"herexxx "<<N<<endl;
        if(check(mp,lst)) return;
        if(N==7) for(int i=0;i<N;i++) { for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<endl;}cout<<endl;
        ///cout<<"hereddd "<<N<<endl;
        for(int i=0;i<N-1;i++) for(int j=0;j<N-1;j++){
            mp[i][j] = small[j][i];
        }
        if(check(mp,lst)) return;
        for(int i=0;i<N;i++) { for(int j=0;j<N;j++) cout<<mp[i][j]<<" ";cout<<endl;}
        cout<<N<<" !!!!!!!"<<endl;
        return;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    ///freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        int N;
        cin>>N;
        vector< vector<int> > mp(2*N-1);
        int x;
        for(int i=0;i<N*2-1;i++){
            for(int ii=0;ii<N;ii++){
                cin>>x;
                mp[i].push_back(x);
            }
        }


        ///for(int i=0;i<N*2-1;i++) {for(int p:mp[i]) cout<<p<<" ";cout<<endl;}

        vector< vector<int> > out;
        solve(mp,N,out);
        ///for(int i=0;i<N;i++) { for(int j=0;j<N;j++) cout<<out[i][j]<<" ";cout<<endl;}
        vector<bool> vst(N*2);
        check(out,mp,vst);
        vector<int> ans;
        for(int i=0;i<2*N;i++){
            cout<<i<<" : "<<vst[i]<<endl;
            if(vst[i]==false){
                if(i<N) for(int j=0;j<N;j++) ans.push_back(out[i][j]);
                else for(int j=0;j<N;j++) ans.push_back(out[j][i-N]);
            }
        }
        printf("Case #%d:",cas);
        for(int xx:ans) printf(" %d",xx);
        cout<<endl;
    }
    return 0;
}
