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
    long T,N,digits[10],sum=0,multiple=1,temp,dig,j=0,product;
    cin>>T;
    while(T--){
        j++;
        cin>>N;
        if(N==0)
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else{
            // init
            sum=10;
            int digits[10]={0};
            multiple=1;
            // end init
            while(sum!=0){
                product=N*multiple;
                temp=product;
                //extract digits
                while(temp){
                    dig=temp%10;
                    temp=temp/10;
                    if(digits[dig]==0){
                        sum--;
                        digits[dig]++;
                    }
                }
                multiple++;
            }
            cout<<"Case #"<<j<<": "<<product<<endl;
        }
    }
    return 0;
}