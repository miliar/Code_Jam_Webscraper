#include<bits/stdc++.h>
using namespace std;
int main (){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int T , S;
    cin>>T;
    int *sol = new int[T];
    for (int i=0;i<T;i++){
        cin>>S;
        S++;
        string input;
        cin>>input;
        int cntr =0 ;
        int sum =0 , tmp;
        for (int j=0;j<S;j++){
            tmp = input[j]-48;
            if(sum<j&&tmp!=0){cntr+=j-sum;sum+=cntr;}
            sum+=tmp;
        }
        sol[i]=cntr;
    }
    for (int i=0;i<T;i++){
        cout<<"Case #"<<i+1<<": "<<sol[i]<<endl;
    }
    return 0;
}
