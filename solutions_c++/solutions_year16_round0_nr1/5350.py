#include <bits/stdc++.h>

#define MAX 1000000
#define COUNT 1000

using namespace std;



int perform(int n){
    if(n==0) return 0;
    set<int> digits;
    int quo, rem;
    int it, temp;
    it = 0;
    for(int i=1; i<=COUNT; i++){

        it += n;
        temp = it;
        for(int j=1; j<=9; j++){
           // cout<<temp<<endl;
            rem = temp%10;
            digits.insert(rem);
            if(digits.size()>=10) return it;
            temp/=10;
            if(temp==0) break;
        }
    }
    return 0;


}
int main()
{
    freopen("A-large.in", "rb", stdin);
    freopen("Output_file.out", "wb", stdout);

    int n, t;
    int result;
    cin>>t;
    for(int i=1; i<=t; i++){

        cin>>n;
        result = perform(n);
        if(result == 0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i<<": "<<result<<endl;
    }


    return 0;
}
