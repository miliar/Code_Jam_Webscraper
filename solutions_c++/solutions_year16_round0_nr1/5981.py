#include <iostream>

using namespace std;

int main(){
    int T;
    cin>>T;
    unsigned int found=0;
    for(int t=0;t<T;t++){
        found=0;
        long long N;
        cin>>N;
        if(N==0){
            cout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
            continue;
        }
        int counter=0;
        while(found!=0x03FF){
            ++counter;
            long long temp=N*counter;
            while(temp>0){
                int digit=temp%10;
                found|=1<<digit;
                temp=temp/10;
            }

        }
        cout<<"Case #"<<t+1<<": "<<N*counter<<endl;
    }
}
