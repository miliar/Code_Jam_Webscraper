#include<bits/stdc++.h>
using namespace std;
long long int isprime[10000001];
vector<long long int>primes;
long long int sizeofprimes;
long long int fast_power(long long int num,long long int pow){
    long long int ans = 1;
    while(pow > 0){
        if(pow % 2 == 1){
            ans = (ans * num);
        }
        num = num * num;
        pow = pow / 2;
    }
    return ans;
}
void Calcprime(){
    isprime[0] = 1;
    isprime[1] = 1;
    long long int i,j;
    for(i = 2; i * i <= 10000000; i++){
        if(isprime[i]==1)
            continue;
        for(j = i * 2; j <= 10000000; j += i){
            isprime[j]=1;
        }
    }
    for(i = 2; i <= 10000000; i++){
        if(isprime[i] == 0){
            primes.push_back(i);
        }
    }
    sort(primes.begin(),primes.end());
    sizeofprimes = primes.size();
}
int main(){
    FILE *myFile;
    myFile = fopen("C:\\Users\\Dell\\Desktop\\input1.in", "r");
    FILE *fptr;
    fptr = fopen("C:\\Users\\Dell\\Desktop\\output.txt","w");
    Calcprime();
    long long int n,j,t;
    fscanf(myFile, "%lld", &t);
    fscanf(myFile, "%lld%lld", &n, &j);
    fprintf(fptr,"Case #1:\n");
    //cin>>t>>n>>j;
    long long int arr[11];
    long long int i;
    for(i = 2; i < 11; i++){
        arr[i] = fast_power(i,n-1) + 1;
    }
    long long int m = n-2;
    long long int val[11];
    long long int count = 0;
    for(i = 0; i <= fast_power(m,2); i++){
        for(int ii = 0; ii < 11; ii++){
            val[ii] = 0;
        }
        int c = 1;
        int p = i;
        int k;
        while(p > 0){
            if(p & 1){
                for(k = 2; k < 11; k++){
                    val[k] = val[k] + fast_power(k,c);
                }
            }
            p = p >> 1;
            c++;
        }
        for(k = 2; k < 11; k++){
            val[k] = val[k] + arr[k];
        }
        int temp = 0;
        for(k = 2; k < 11; k++){
            if(val[k] < 10000001){
                if(isprime[val[k]] == 0){
                    temp = 1;
                    break;
                }
            }
            else{
                long long int l;
                long long int x = val[k];
                int check = 1;
                for(l = 0; l < sizeofprimes; l++){
                    if(primes[l] <= sqrt(x)){
                        if(x % primes[l] == 0){
                            check = 0;
                            break;
                        }
                    }
                }
                if(check == 1){
                    temp = 1;
                    break;
                }
            }
        }
        if(temp == 0){
            vector<long long int>binarynum;
            p = i;
            //cout<<p<<"\n";
            while(p > 0){
                if(p & 1){
                    binarynum.push_back(1);
                }
                else{
                    binarynum.push_back(0);
                }
                p = p >> 1;
            }
            //cout<<1;
            fprintf(fptr,"1");
            int h = binarynum.size();
            long long int l;
            if(h < m){
                for(l = 0; l < m-h; l++){
                    //cout<<"0";
                    fprintf(fptr,"0");
                }
            }
            int q = binarynum.size();
            for(l = q - 1; l >= 0; l--){
                //cout<<binarynum[l];
                fprintf(fptr,"%lld",binarynum[l]);
            }
            fprintf(fptr,"1 ");
            //cout<<1;
            //cout<<" ";
            for(k = 2; k < 11; k++){
                for(l = 2; l <= sqrt(val[k]); l++){
                    if(val[k] % l == 0){
                        fprintf(fptr,"%lld ",l);
                        //cout<<l<<" ";
                        break;
                    }
                }
            }
            fprintf(fptr,"\n");
            //cout<<"\n";
            count++;
            if(count == j){
                break;
            }
        }
    }
    return 0;
}
