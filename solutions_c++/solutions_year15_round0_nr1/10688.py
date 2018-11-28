#include <iostream>
using namespace std;
int main()
{
    int T,Sm,i,j,fri,tot_ova;
    char a[1001];
    std::cin>>T;
    for(i=0;i<T;i++) {
        std::cin>>Sm;
        std::cin>>a;
        fri=0;
        tot_ova=0;
        for(j=0;j<=Sm;j++) {
            if(tot_ova<j&&a[j]-'0'!=0) { fri+=j-tot_ova; tot_ova+=j-tot_ova; }
             tot_ova+=(a[j]-'0');
        }
        std::cout<<"\tCase #"<<i+1<<": "<<fri<<std::endl;
    }
    return 0;
}
