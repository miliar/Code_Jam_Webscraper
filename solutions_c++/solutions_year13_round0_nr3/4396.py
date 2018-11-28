#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <math.h>
using namespace std;

bool judge(int r){
    int s = 0,x = r;
    while(x){
        s = s * 10 + x % 10;
        x /= 10;
    }
    return s == r;
}
int main()
{
    //freopen("Input.txt","r",stdin);
   // freopen("Output.txt","w",stdout);
    int T,k = 1;
    cin>>T;
    while(T--){
        int A,B;
        cin>>A>>B;
        cout<<"Case #"<<k++<<": ";
        int cnt = 0,r = (int)sqrt(A*1.0),i;
        if(r * r == A) i = r;
        else i = r + 1;
        for(;i*i <= B;++i){
            if(judge(i) && judge(i*i)) cnt++;
        }
        cout<<cnt<<endl;
    }
    return 0;
}
