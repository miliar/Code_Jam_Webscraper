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
    LLUI N,ans,i,temp_N,N_n,j,digit,k,count=0;
    int T;
    int flag1=0;
    int dp[10];
    for(i=0;i<10;i++){
        dp[i]=0;
    }
    cin>>T;
    j=0;
    for(i=1;i<=T;i++){
        j=0;
        cin>>N;
        N_n=N;
        count = 0;
        for(k=0;k<10;k++)   {
            dp[k]=0;
        }
        while(true){
            temp_N=N_n;
            flag1=0;
            j = j+1;
            if (N_n==0){
                cout<<"Case #"<<i<<": INSOMNIA"<<endl;
                break;
            }
            else {
                do{
                    digit = temp_N%10;
                    dp[digit]=1;
                    temp_N=temp_N/10;
                }while(temp_N>0);
                for(k=0;k<10;k++){
                    if(dp[k]==0){
                        flag1=1;
                        break;
                    }
                }
            }
            if(flag1 == 0){ // all digits found bingo
                cout<<"Case #"<<i<<": "<<N_n<<endl;
                break;
            } else {
                N_n=N*j;
                count ++;
            }
        }
    }
    return 0;
}
