#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iomanip>

const int MAXN = 1010;

using namespace std;

int N;
double A1[MAXN], A2[MAXN], B1[MAXN], B2[MAXN];

int main(){
    int T; cin>>T;
    
    for(int t=1;t<=T;t++){
            cin>>N;
            for(int i=0;i<N;i++)
                    cin>>A1[i];
            for(int i=0;i<N;i++)
                    cin>>B1[i];
            
            sort( A1, A1 + N );
            sort( B1, B1 + N );
            for(int i=0;i<N;i++){
                    A2[i] = A1[i];
                    B2[i] = B1[i];
                    }
            
            //cout<<N<<'\n';
            //for(int i=0;i<N;i++)
            //        cout<<fixed<<setprecision(3)<<A1[i]<<' ';cout<<'\n';
            //for(int i=0;i<N;i++)
            //        cout<<fixed<<setprecision(3)<<B1[i]<<' ';cout<<'\n';
            
            int y = 0;
            for(int i=0;i<N;i++){
                    int pos = -1;
                    for(int j=0;j<N;j++)
                            if( B1[j] < A1[i] ){
                                pos = j;
                                y++;
                                break;
                                }
                    if( pos == -1 )
                        for(int j=N-1;j>=0;j--)
                                if( B1[j] < 1 ){
                                    pos = j;
                                    break;
                                    }
                    B1[pos] = 1;
                    }
            
            int z = 0;
            for(int i=0;i<N;i++){
                    int pos = -1;
                    for(int j=0;j<N;j++)
                            if( B2[j] > A2[i] ){
                                pos = j;
                                z++;
                                break;
                                }
                    if( pos == -1 )
                        for(int j=0;j<N;j++)
                                if( B2[j] != -1 ){
                                    pos = j;
                                    break;
                                    }
                    
                    B2[pos] = -1;
                    }
            z = N - z;
            
            cout<<"Case #"<<t<<": "<<y<<' '<<z<<'\n';
            }
    
    return 0;
}
