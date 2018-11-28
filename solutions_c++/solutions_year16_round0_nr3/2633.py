#include <cstdio>
#include <string>
#include <cmath>
using namespace std;

int prime[10000]={2};

void Test(){
    string binary;
    long long b10num,printarr[9]={0},temp,notprime,idx,i,j,N,J,cnt = 0,isValid;
    scanf("%lld%lld",&N,&J);
    for(i=0;i<N;i++) binary.push_back('0');
    *(binary.end()-1) = *(binary.begin()) = '1';
    while(cnt < J){
        idx = isValid = 0;
        for(i=2;i<=10;i++){
            temp = 0;
            notprime = 1;
            for(j=0;j<N;j++){
                temp += (binary[N-j-1]-'0')*pow(i,j);
            }
            for(j=0;j<10000;j++){
                if(temp%prime[j] == 0) notprime = 0;
            }
            if(!notprime){
                for(j=2;j<temp;j++){
                    if(temp%j == 0){
                        temp = j;
                        break;
                    }
                }
                printarr[idx++] = temp;
                isValid++;
            }
        }
        if(isValid == 9){
            for(i=0;i<N;i++) printf("%c",binary[i]);
            for(i=0;i<9;i++) printf(" %lld",printarr[i]);
            printf("\n");
            cnt++;
        }
        binary[N-2]++;
        for(i=N-2;0 < i;i--){
            if('1' < binary[i]){
                binary[i] = '0';
                binary[i-1]++;
            }
        }
    }
}

int main(){
    int i,j,T,idx=0;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    prime[idx++] = 2;
    for(i=3;idx<10000;i++){
        for(j=0;j<idx;j++){
            if(i%prime[j] == 0){
                break;
            }
        }
        if(j==idx){
            prime[idx++] = i;
        }
    }
    scanf("%d",&T);
    for(i=1;i<=T;i++) {
        printf("Case #%d:\n",i);
        Test();
    }
}