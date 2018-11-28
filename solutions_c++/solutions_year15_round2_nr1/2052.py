# include<bits/stdc++.h>
using namespace std;

int mat[1000100];

//O(log10(a))
long long rev(long long a){
    long long ans = 0;
    while(a>=10){
        ans += (a%10);
        ans*=10;
        a/=10;
    }
    ans+=a;
    return ans;
}

bool glo=false;

int c;

int solve(long long n){
    c++;
    if(mat[n]) return mat[n];

    if(n<21) return n;
    long long a = rev(n);
    if(a<n && n%10!=0){
        int d = solve(a)+1;
        int k = solve(n-1)+1;
        if(d<k){
            mat[n] = d;
        }else{
            mat[n] = k;
        }
        return mat[n];
    }
    mat[n] = solve(n-1)+1;
    return mat[n];
}

int main(){
    //freopen("A4.in","r",stdin);
    //freopen("A.out","w",stdout);
    int t;
    long long x;
    cin>>t;
    memset(mat,0,sizeof(mat));

    for(int i=0 ; i<t ; i++){
        cin>>x;
        cout<<"Case #"<<i+1<<": "<<solve(x)<<endl;
    }
}










