#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    FILE *fin = freopen("A-large.in", "r", stdin);
    FILE *fout = freopen("A-large.out", "w", stdout);
    int i,j=0,num,n,n1,t;
    cin>>t;
    while(t--){
        j++;
        cin>>num;
        n1=num;
        if(num==0)
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else{
            int digits[10]={0};
            i=1;
            while(1){
                n=num;
                while(n!=0){
                    digits[n%10]=1;
                    n/=10;
                }
                if((digits[0] && digits[1] && digits[2] && digits[3] && digits[4] && digits[5] && digits[6] && digits[7] && digits[8] && digits[9])==1){
                    cout<<"Case #"<<j<<": "<<num<<endl;
                    break;
                }
                else{
                    num=n1*(++i);
                }
            }
        }
    }
    return 0;
}