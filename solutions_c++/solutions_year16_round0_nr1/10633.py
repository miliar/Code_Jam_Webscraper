#include <iostream>
#include <string>
#include <stdio.h>
#include <set>
using namespace std;
int main(){
    int a,tc,j=0,n;
    long res;
    std::set<char> digits;
    string temp;
    scanf("%d",&tc);
    while(tc--!=0){
        j++;
        scanf("%d",&n);
        if(n==0){printf("Case #%d: INSOMNIA\n",j);continue;}
        digits.clear();int i=1;
        for(;i<10e16;i++){
            res=n*i;
            temp = std::to_string(res);
            digits.insert(temp.begin(),temp.end());
            if(digits.size()==10)break;
        }
        if(i>10e16){printf("Case #%d: INSOMNIA\n",j);continue;}
        printf("Case #%d: %d\n",j,res);
    }
    /*string name = std::to_string(a);
    std::set<char> nc(name.begin(),name.end());
    cout<<nc.size()<<endl;*/
    return 0;
}
