#include <iostream>
#include <cstdio>
using namespace std;

bool check(int digits[10])
{
    if((digits[0] && digits[1] && digits[2] && digits[3] && digits[4] && digits[5] && digits[6] && digits[7] && digits[8] && digits[9]) == 1)
        return true;
    else
        return false;
}
int mynumb(int num)
{
    int digits[10] ={0};
    int numc = num;
    int finalnum = num;
    int i;
    for(int j = 1; !check(digits) ; j++)
    {
        numc = num*j;
        finalnum = numc;
        while(numc){
            i = numc%10;
            digits[i] = 1;
            numc /= 10;
         }
    }
    return finalnum;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    short t;
    cin>>t;
    int num, i;
    for(i=1;i<=t;i++){
        cin>>num;
        if(!num)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<mynumb(num)<<endl;
    }
    return 0;
}


