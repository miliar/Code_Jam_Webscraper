#include<bits/stdc++.h>
using namespace std;
long long int check(long long int a[]){
    long long int i;
    for(i = 0; i < 10; i++){
        if(a[i] == 0){
            return 0;
        }
    }
    return 1;
}
int main(){
    FILE *myFile;
    myFile = fopen("C:\\Users\\Dell\\Desktop\\input2.in", "r");
    FILE *fptr;
    fptr = fopen("C:\\Users\\Dell\\Desktop\\output.txt","w");
    long long int t;
    //cin>>t;
    fscanf(myFile, "%lld", &t);
    long long int cc = 1;
    while(t--){
        long long int n,i;
        fscanf(myFile, "%lld", &n);
        //cin>>n;
        if(n == 0){
            //cout<<"Case #"<<cc++<<" "<<"INSOMNIA\n";
            fprintf(fptr,"Case #%lld: INSOMNIA\n",cc++);
            continue;
        }
        long long int a[10];
        for(i = 0; i < 10; i++){
            a[i] = 0;
        }
        long long int ans = n;
        long long int c = 2;
        while(1){
            long long int x = ans;
            while(x > 0){
                a[x % 10] = 1;
                x = x / 10;
            }
            if(check(a) == 1){
                break;
            }
            else{
                ans = c * n;
                c++;
            }
        }
        //cout<<"Case #"<<cc++<<" "<<ans<<"\n";
        fprintf(fptr,"Case #%lld: %lld\n",cc++,ans);
    }
    fclose(myFile);
    fclose(fptr);
    return 0;
}
