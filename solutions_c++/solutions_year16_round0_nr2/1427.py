//2-large??
#include "stdio.h"
#include "iostream"
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("solution.txt","w",stdout);
    int t;
    string d;
    cin>>t;
    for(int l=1;l<=t;l++){
        int countx=0;
        char now;
        cin>>d;
        for(int i=0;i<d.length()-1;i++){
            if(d[i]!=d[i+1]){
                countx++;
                now=d[i+1];
            }
        }
        if(countx==0) now=d[d.length()-1];
        if(now=='-') countx++;
        printf("Case #%d: %d\n",l,countx);
    }
    return 0;
}
