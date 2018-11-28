#include <iostream>
using namespace std;
void InitArray(int dig[]){
    for(int i=0;i<11;i++)
        dig[i]=0;

}
long long int ExtractDigits(long long int n,int dig[]){
    long long int num=n;
    int digit;
    while(num>0){
        digit=num%10;
        if(dig[digit]==0){
            dig[digit]=1;
            dig[10]++;
        }
        if(dig[10]==10)return n;
        else
            num=num/10;

    }
    return 0;

}
main(){
    int T, dig[11];
    long long int num;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>num;
        if(num==0)cout<<"Case #"<<i<<": "<<"Insomnia\n";
        else {
            InitArray(dig);
            for(int j=1;;j++){
                long long int k=ExtractDigits(j*num,dig);
                if(k!=0){
                    cout<<"Case #"<<i<<": "<<k<<endl;
                    break;
                }

            }


        }

    }
}
