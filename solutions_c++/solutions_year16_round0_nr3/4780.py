#include <iostream>
#include <stdio.h>
#include <algorithm>
#define MAX 10000001
#define MAX2 700000
using namespace std;
long long changebase3(long long N,int B){
long long c = 1,x = 0;
for(int i = 0; i < 32;i++,c*=B)
    if((N&(1<<i))!= 0)
    x+=c;
    return x;
}
void print(int x,int n){
for(int i = n-1;i >= 0;i--)
    if((x&(1<<i))!= 0)
    cout<<1;
    else cout<<0;
}
    bool v[10000];
    long long primes[600];

int main(){
    for(long long i = 2;i*i < 1000;i++)
        if(!v[i])
            for(long long j = i*i;j < 1000;j+=i)
                v[j] = true;

int index = 0;
    for(int i = 2;i < 1000;i++){
        if(!v[i]){
                primes[index] = i;
            index++;
        }
    }

//freopen("A.in","r",stdin);
//freopen("o3.out","w",stdout);
  freopen("C-small-attempt3.in","r",stdin);
  freopen("out4.out","w",stdout);
int T = 1,cs = 1;
    cin >> T;
while(T--){
int n,J;
cin >> n >> J;
cout<<"Case #"<<cs++<<": \n";
int N = 0;//= (1<<(n-1))+1;
N = N|(1<<(n-1));
N = N|(1<<0);
//print(N); cout<<endl;
int c = 1;
while(c <= J&&N < (1<<n)){
vector<int>v;
if((N&(1<<0))== 0){
 N++;
 continue;
 }
if((N&(1<<(n-1)))== 0){
 N++;
 continue;
 }

    for(int i = 2;i <= 10;i++){
        long long x = changebase3(N,i);
        int mx = 0;
        for(int j = 0;j < index;j++)
            if(x%primes[j] == 0){
            v.push_back(primes[j]);
            break;
            }
    }
    if(v.size() == 9){
    //cout<<c<<" "<<N<<" ";
        print(N,n);
        for(int i = 0;i < v.size();i++)
            cout<<" "<<v[i];
        cout<<endl;
        c++;
    }
    N++;
}

}

    return 0;
}

/*
cout<<c<<" "<<N<<" --- ";
    for(int i = 9;i <= 10;i++){
        long long x = changebase3(N,i);
        cout<<x<<" ";
        }
        cout<<"\n*************\n";
cout<<c<<" "<<N<<" --- ";
    for(int i = 2;i <= 10;i++){
        int x = changebase3(N,i);
        cout<<x<<" ";
        }
        cout<<"\n*************\n";

/*


long long changebase(long long N,int B){
if(B == 10)
return N;
long long x = 0;
while(N){
x*=10;
x+=N%B;
N/=B;
}
return x;
}
long long changebase2(long long N,int B){
if(B == 10)
return N;
string s;
while(N){
s+=char('0'+N%10);
N/=10;
}

reverse(s.begin(),s.end());
long long x = 0,c = 1;
for(int i = 0;i < s.size();i++,c*=B)
    if(s[i] == '1')
        x+=c;
        return x;
}
long long change(string s){
int x = 0;
for(int i = s.size()-1;i>= 0 ;i--)
    if(s[i] == '1')
    x|=(1<<i);
    return x;
}

*/
