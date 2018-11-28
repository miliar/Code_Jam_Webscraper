#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <deque>
using namespace std;
int A[51][51];
bool set[51][2]; //[0] is the row, [1] is the column
int P[102][51];
int n;
bool row(int i){
    int ans=0;
    int tr1=0;
    int tr2=0;
    for (int j=0;j<2*n-1;j++){
        bool good=true;
        for (int e=0;e<n;e++) if ((A[i][e]!=-1)&&(A[i][e]!=P[j][e])) good=false;
        if (good){
            ans++;
            if (tr1==0) tr1=j;
            else tr2=j;
        }
    }
    bool same=false;
    if (ans==2){
        same=true;
        for (int e=0;e<n;e++) if (P[tr1][e]!=P[tr2][e]) same=false;
    }
    if ((ans==1)||(same)){
        for (int e=0;e<n;e++) A[i][e]=P[tr1][e];
        memset(P[tr1],0,sizeof P[tr1]);
        set[i][0]=true;
        return true;
    }
    return false;
}
bool col(int i){
    int ans=0;
    int tr1=0;
    int tr2=0;
    for (int j=0;j<2*n-1;j++){
        bool good=true;
        for (int e=0;e<n;e++) if ((A[e][i]!=-1)&&(A[e][i]!=P[j][e])) good=false;
        if (good){
            ans++;
            if (tr1==0) tr1=j;
            else tr2=j;
        }
    }
    bool same=false;
    if (ans==2){
        same=true;
        for (int e=0;e<n;e++) if (P[tr1][e]!=P[tr2][e]) same=false;
    }
    if ((ans==1)||(same)){
        for (int e=0;e<n;e++) A[e][i]=P[tr1][e];
        memset(P[tr1],0,sizeof P[tr1]);
        set[i][1]=true;
        return true;
    }
    return false;
}

void print(){
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++) cout<<A[i][j]<<' ';
            cout<<endl;
        }
        cout<<endl;
}
int main(){
    freopen("readable.txt","w",stdout);
    int t;
    cin>>t;
    for (int ca=1;ca<=t;ca++){
        memset(A,-1,sizeof A);
        memset(set,false,sizeof set);
        cin>>n;
        int small,big;
        small=2505;
        big=0;
        for (int i=0;i<2*n-1;i++){
            for (int j=0;j<n;j++) {
                cin>>P[i][j];
                small=min(small,P[i][j]);
                big=max(big,P[i][j]);
            }
        }
        A[0][0]=small; A[n-1][n-1]=big;
        //first row
        for (int j=0;j<2*n-1;j++){
            bool good=true;
            for (int e=0;e<n;e++) if ((A[0][e]!=-1)&&(A[0][e]!=P[j][e])) good=false;
            if (good){
                for (int e=0;e<n;e++) A[0][e]=P[j][e];
                memset(P[j],0,sizeof P[j]);
                set[0][0]=true;
                break;
            }
        }
        deque<pair<int,bool>> dq;
        if (col(0)==0) dq.push_back({0,false});
        if (row(n-1)==0) dq.push_back({n-1,true});
        if (col(n-1)==0) dq.push_back({n-1,false});
        for (int i=1;i<n-1;i++){
            dq.push_back({i,false});
            dq.push_back({i,true});
        }

        while (dq.size()>1){
            pair<int,bool> here=dq.front();
            dq.pop_front();
            if (here.second){
                if (!row(here.first)) dq.push_back(here);
            }
            else{
                if (!col(here.first)) dq.push_back(here);
            }
            //print();
        }
        cout<<"Case #"<<ca<<": ";
        for (int i=0;i<n;i++){
            if (!set[i][0]){
                for (int j=0;j<n-1;j++) cout<<A[i][j]<<' ';
                cout<<A[i][n-1]<<endl;
            }
            if (!set[i][1]){
                for (int j=0;j<n-1;j++) cout<<A[j][i]<<' ';
                cout<<A[n-1][i]<<endl;
            }
        }
    }
}
