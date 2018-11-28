#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int check(long long k){

    int l = 0, s[200] ,t = k;
    while (k){
        s[l++] = k%10;
        k = k/10;
    }
    for (int i = 0; i < l/2; i++)
        if (s[i] != s[l-i-1]) return 0;
    //cout<<t<<endl;
    return 1;
}

int main()
{
    //freopen("Cinput.txt","r",stdin);
    //freopen("Coutput.txt","w",stdout);

    int T;
    cin>>T;
    for (int cas = 1; cas <=T; cas++){
        long long A, B, i, t,ans = 0;
        cin>>A>>B;
        i = (long long)sqrt(A);
        for (; i*i <= B; i++)
            if (check(i)){
            t = i*i;
            if (t >= A)
                if (check(t)) ans++;
            }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
