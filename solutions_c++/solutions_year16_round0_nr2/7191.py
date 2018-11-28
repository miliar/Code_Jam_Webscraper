#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main(){
    long long int t,i;
    cin >> t;
    for(long long int a0 = 0; a0 < t; a0++){
        long long int n,count;
        string str;
       cin >> str;
        n=str.length();
        for(i=0;i<n;++i){
            if(str[i]!='-')
                break;
        }
        if(i!=0)
            count=1;
        else
            count=0;
        for(;i<n;++i){
            if(str[i]=='-'){
                while((str[i]=='-')&&(i<n))
                    ++i;
                count+=2;
            }
        }
           
    cout<<"Case #"<<a0+1<<": "<<count<<endl;        
        }
    return 0;
}
