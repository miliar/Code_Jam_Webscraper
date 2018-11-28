#include <bits/stdc++.h>

using namespace std;

long long func(long long a){
    if(a==0){
        return -1;
    }
    long long j=1, a_copy = a;
    bool ar[10]{false, false, false, false, false, false, false, false, false, false};
    while(ar[0]==false || ar[1]==false || ar[2]==false || ar[3]==false || ar[4]==false || ar[5]==false || ar[6]==false || ar[7]==false || ar[8]==false || ar[9]==false){
        long long n=a*j;
        while(n>0){
            if(ar[n%10]==false) ar[n%10]=true;
            n/=10;
        }
        j++;
    }
    a*=j;
    return (a-a_copy);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T=0;
    cin>>T;
    vector<long long> vec;
    for(int in=0;in<T;in++){
        long long F;
        cin>>F;
        vec.push_back(F);
    }
    for(int i=0;i<T;i++){
        long long s = func(vec[i]);
        if(s==-1) cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i+1<<": "<<s<<endl;
    }
    return 0;
}
