#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;
bool ispo(long long n){
     int in=0;
     int a[20];
     while (n>0){
           a[in]=n%10;
           n/=10;
           in++;
     }
     for (int i=0; i<in; i++){
         if (a[i]!=a[in-i-1]) return false;
     }
     return true;

}
bool isgood(long long n){
     bool ans=true;
     
     long long m;
     float x,y;
     x=1.0*n;
     
     y=sqrt(x);
     m=(long long)y;
     if (m*m!=n) return false;
     if (ispo(m) && ispo(n)) return true;
     else return false;
}

int amoxsna(long long a, long long b){
    int ans=0;
    for (long long i=a; i<=b; i++){
        if (isgood(i)) ans++;
    }
    return ans;   
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t;
    long long a,b;
    int s[10000];
    cin>>t;
    long long uu=121;
    //if (ispo(uu)) cout<<"RRRR";
    
    for (int i=0; i<t; i++){
      
      cin>>a>>b;    
          s[i]=amoxsna(a,b);  
    }
    for (int i=0 ; i<t; i++){
        cout<<"Case #"<<i+1<<": "<<s[i]<<endl;
    }
    //system("pause");
    return 0;
}
