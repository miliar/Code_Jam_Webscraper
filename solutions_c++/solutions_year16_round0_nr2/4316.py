#include <bits/stdc++.h>
#define LLI long long int
#define LLUI long long unsigned int
#define LD long double
#define MOD 1000000007LL
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
using namespace std;

int main() {
    int T,N,len,i,j,k,ans=0;
    string str;
//  string mstr;
    cin>>T;
    for(i=1;i<=T;i++){
        cin>>str;
        k = 0;
            
        len = str.length();
        char mstr[len];//modified string
        mstr[k++]=str[0];
        for(j=1;j<len;j++){
            if(str[j] != str[j-1]){
                mstr[k++] = str[j];
            } 
        }
        mstr[k]='\0';
        len = k;
        ans = 9999;
        for(j=k-1;j>=0;j--){
            if(mstr[j]=='-'){
                ans = j;
                break;
            }
        }
        if (ans!=9999){
            ++ans;
            cout<<"Case #"<<T<<": "<<ans<<endl;
        } else {
            // ans =0
            cout<<"Case #"<<T<<": 0"<<endl;
        }
    }
    return 0;
}
