#include<bits/stdc++.h>
using namespace std;

bool check(long long *arr){
    for(long long i=0 ; i<10 ; i++){
        if(*(arr+i)==0)
            return false;
    }
    return true;
}

int main(){
    freopen("in1s.in","r",stdin);
    freopen("op1s.txt","w",stdout);
    long long t,n,last,temp,a[10];
    cin >> t;
    for(long long tcase=1 ; tcase<=t ; tcase++){
        cin >> n;
        if(n==0)
            cout << "Case #" << tcase << ": INSOMNIA" << endl;
        else{
            last=0;
            for(long long i=0 ; i<10 ; i++)
                a[i]=0;
            while(!check(a)){
                last+=n;
                temp=last;
                while(temp){
                    a[temp%10]=1;
                    temp/=10;
                }
            }
            cout << "Case #" << tcase << ": " << last << endl;
        }
    }
    return 0;
}
