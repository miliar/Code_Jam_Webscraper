#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iomanip>

using namespace std;

int N,K;
double p[210];

double sum(vector<int>row){

    double athroisma = 0.0;
    for(int i=0;i<1<<K;i++){
        double tmp = 1.0;
        int counter = 0;
        for(int j=0;j<K;j++)
            if( i & 1<<j ){
                counter++;
                tmp *= p[row[j]];
            }else{
                tmp *= (1-p[row[j]]);
            }
        if( counter == K/2 ){
            athroisma += tmp;
        }
    }
    return athroisma;

}

double calc(int pos,vector<int> row){

    row.push_back( pos );
    if( row.size() == K ){
        return sum(row);
    }
    double best = 0.0;
    for(int i=pos+1;i<N;i++){
        double tmp = calc( i, row);
        if( tmp > best )
            best = tmp;
    }
    return best;
}

double solve(){

    double best = 0.0;
    for(int i=0;i<N;i++){
        double tmp = calc( i, vector<int>() );
        if( tmp > best )
            best = tmp;
    }
    return best;
}

int main(void){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int T; cin>>T;
    for(int t=1;t<=T;t++){
        cin>>N>>K;
        for(int i=0;i<N;i++)
            cin>>p[i];
        cout<<"Case #"<<t<<": "<<setprecision(6)<<fixed<<solve()<<'\n';
    }

}
