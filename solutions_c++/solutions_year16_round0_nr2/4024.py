#include <iostream>
#include <cstdio>
using namespace std;
string a;
int main(){
    int n;
    int count=1;
    cin>>n;
    for(int i=1;i<=n;i++){
        count=0;
        a.clear();
        cin>>a;
        for(int j=0;j<a.length();j++){
            if(a[j]=='+'){
                for(int k=j+1;k<a.length();k++){
                    if(a[k]=='+'){
                        a.erase(a.begin()+k);
                        k--;
                    }
                    else{
                        break;
                    }
                }
            }
        }
        if(a.length()==1){
            if(a[0]=='+'){
                printf("Case #%d: 0\n",i);
                continue;
            }
            else{
                printf("Case #%d: 1\n",i);
                continue;
            }
        }
        for(int j=0;j<a.length();j++){
            if(a[j]=='+'){
                if(j==0){
                    count++;
                }
                else if(j==a.length()-1){
                    count++;
                }
                else{
                    count+=2;
                }
            }
            if(j==a.length()-1&&a[j]=='-'){
                count++;
            }
        }
        printf("Case #%d: %d\n",i,count);
    }
}