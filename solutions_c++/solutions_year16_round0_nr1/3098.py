#include <cstdio>
#include <string>
using namespace std;

int Test(){
    string n;
    char arr[100]={0},check[10]={0};
    int N,i,j,ret;
    long long num;
    scanf("%s",arr);
    n = arr;
    N = stoi(n);
    for(i=1;i<=99;i++){
        num = N*i;
        n = to_string(num);
        for(j=0;j<n.length();j++){
            check[n[j]-'0'] = 1;
        }
        ret = 0;
        for(j=0;j<10;j++){
            if(check[j]) ret++;
        }
        if(ret == 10){
            printf("%lld\n",num);
            return 1;
        }
    }
    printf("INSOMNIA\n");
    return 0;
}

int main(){
    int i,T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++) {
        printf("Case #%d: ",i);
        Test();
    }
}