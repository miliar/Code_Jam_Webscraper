#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int N,R,P,S;
bool found;
vector<char> res;

bool correct(vector<char> row){

    if( row.size() == 1 )
        return true;

    vector<char> neo;
    for(int i=0;i<row.size();i+=2){
        if( row[i]=='R' && row[i+1]=='R' )
            return false;
        else if( row[i]=='R' && row[i+1]=='P' )
            neo.push_back('P');
        else if( row[i]=='R' && row[i+1]=='S' )
            neo.push_back('R');
        else if( row[i]=='P' && row[i+1]=='R' )
            neo.push_back('P');
        else if( row[i]=='P' && row[i+1]=='P' )
            return false;
        else if( row[i]=='P' && row[i+1]=='S' )
            neo.push_back('S');
        else if( row[i]=='S' && row[i+1]=='R' )
            neo.push_back('R');
        else if( row[i]=='S' && row[i+1]=='P' )
            neo.push_back('S');
        else if( row[i]=='S' && row[i+1]=='S' )
            return false;
    }
    return correct(neo);
}

void calc(char cur,int r,int p,int s,vector<char> row){

    if( found )
        return;

    row.push_back( cur );
    if( r==0 && p==0 && s==0 ){
        if( correct(row) ){
            res = row;
            found = true;
        }
    }

    if( !found && p > 0 )
        calc( 'P', r, p-1, s, row );
    if( !found && r > 0 )
        calc( 'R', r-1, p, s, row );
    if( !found && s > 0 )
        calc( 'S', r, p, s-1, row );

}

bool solve(){

    found = false;
    res.clear();
    if( !found && P > 0 )
        calc( 'P', R, P-1, S, vector<char>() );
    if( !found && R > 0 )
        calc( 'R', R-1, P, S, vector<char>() );
    if( !found && S > 0 )
        calc( 'S', R, P, S-1, vector<char>() );

    if( res.size() == 0 )
        return false;
    return true;
}

int main(void){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int T; cin>>T;
    for(int t=1;t<=T;t++){
        cin>>N>>R>>P>>S;
        cout<<"Case #"<<t<<": ";
        int ok = solve();
        if( !ok )
            cout<<"IMPOSSIBLE\n";
        else{
            for(int i=0;i<res.size();i++)
                cout<<res[i];
            cout<<'\n';
        }
    }

}
