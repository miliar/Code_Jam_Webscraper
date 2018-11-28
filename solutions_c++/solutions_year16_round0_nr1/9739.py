#include<iostream>
#include<fstream>
using namespace std;

bool has[10];
bool check(int n){
    while( n != 0 ) {
        has[n%10]=true;
        n/=10;
    }
    bool valid = true;
    for( int i = 0 ; i < 10 ; i ++ ){
        if( !has[i] )
            valid = false;
    }
    return valid;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        int n;
        scanf("%d",&n);
        if( n == 0 ) puts("INSOMNIA");
        else {
            for( int j = 0 ; j < 10 ; j ++ ){
                has[j] = false;
            }
            int answer = -1;
            for(int j = 1 ; j < 100 ; j ++ ){
                if( check(j*n) ){
                    answer = j;
                    break;
                }
            }
            if( answer != -1 ) printf("%d\n",answer*n);
            else puts("INSOMNIA");
        }

    }

    return 0;
}
