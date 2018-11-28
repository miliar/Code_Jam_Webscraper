#include<iostream>
#include<cstdio>

using namespace std;


bool chkPln(long long  n){

    long long m = n ;
    long long res = 0;
    while(m){
        res = res*10 + m%10;
        m = m/10;
    }
    if(res == n)
        return true;
    return false;
}

int main()
{
    long long arr[50];
    int cntt =0;
    for(long long i = 1 ; i <= 10000000 ; i++){
        if(chkPln(i)){
            long long j = i*i;
            if(chkPln(j)){
                //cout<< i <<" "<< j << endl;
                arr[cntt++] = j;
            }
        }
    }
    //cout << cntt <<endl;

    int t,i,j,cnt=0;
    long long a,b;
    //File *in ,*out;

    //freopen("input.txt","r",stdin);
    //in = fopen("input.txt","w")
    scanf("%d",&t);
    for(j = 1 ; j <= t ; j++){
        scanf("%lld %lld",&a,&b);
        cnt = 0;
        for(i = 0 ; i < 39; i++){
            if(arr[i] >= a && arr[i] <=b)
                cnt++;
        }
        printf("Case #%d: %d\n",j,cnt);
    }
    return 0;

}
