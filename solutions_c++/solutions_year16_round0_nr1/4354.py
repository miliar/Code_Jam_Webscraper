#include <iostream>
using namespace std;

int d[10];
int main(int argc, const char * argv[]) {
    int t, n, cnt;
    long long ans, tmp;
    cin >> t;
    for (int x=1; x <= t; x++){
        cin >> n;
        for (int i=0; i<10;i++) d[i]=0;
        cnt=0;
        int ii=1;
        ans=0;
        while(cnt < 10){

            if(ans==ii*n) {ans=-1; break;}
            ans=ii*n;
            tmp=ans;
            while( tmp > 0 && cnt < 10){
                if(d[tmp%10]==0) {d[tmp%10]=1;cnt++;}
                tmp= tmp/10;
                }
            ii++;
        }
        cout << "Case #"<<x<<": ";
        if(ans < 0) cout << "INSOMNIA" <<endl;
        else cout << ans <<endl;
        
    }
    
    return 0;
}
