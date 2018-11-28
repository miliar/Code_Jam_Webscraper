#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    int a[6][6], b,c,n,m,x[6], ans,ansbool;

    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    m = 1;
    cin>>n;
    while (m != n+1){
        ansbool =0 ;
        ans = 0;
        b = 0;
        c = 0;
        cin>> b;
        for( int i = 1 ; i <= 4; i++ ){
            for ( int j = 1 ; j <= 4; j ++){
                cin>> a[i][j];
            }
        }
        for ( int i= 1; i<= 4 ; i ++ ){
            x [i]= a[b][i];
        }

        cin>> c;
        for( int i = 1 ; i <= 4; i++ ){
            for ( int j = 1 ; j <= 4; j ++){
                cin>> a[i][j];
            }
        }
        cout<< "Case #"<<m<<": ";
        for ( int i = 1 ; i <= 4; i ++ ) {
            for ( int j = 1; j <= 4 ; j ++){
                if ( x[i] == a[c][j] && ansbool==1){
                    cout<<"Bad magician!"<<endl;
                    ansbool++;
                    break;
                }
                if ( x[i] == a[c][j] ){
                    ansbool = 1;
                    ans = x[i];
                }

            }
            if ( ansbool>1)break;
        }
        if( ansbool == 1)cout<<ans<<endl;
        if( ansbool == 0)cout<<"Volunteer cheated!"<<endl;

//        for ( int i= 1; i<= 4 ; i ++ ){
//            cout<< x[i]<<" ";
//        }
//        cout<< endl;
//        for ( int i= 1; i<= 4 ; i ++ ){
//            cout<< a[c][i]<<" ";
//        }
        m++;
    }

return 0;
}
