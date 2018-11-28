//this is for problem C
#include <iostream>
#include <cmath>
#include <stack>
using namespace std;
int main() {
    int T;
    cin>>T;
    while(T>0){
        int N;
        int J;
        int counter=0;
        cin>>N>>J;
        cout<<"Case #1:"<<endl;
        long sum;
        int ubound=(1<<14)-1;
        for(int i=0;i<=ubound;i++){
            int condition=1;
            int p[9]={0,0,0,0,0,0,0,0,0};
            short jamcoin[14];
            for(int qwerty=0;qwerty<14;qwerty++)
                jamcoin[qwerty]=0;
            
            for(int base=2;base<=10;base++){
                sum=pow(base,N-1)+1;
                int v=i;
                int temp;
                int expo=1;
                while(v>0){
                    temp=v%2;
                    v=(v>>1);
                    if(base==2){
                        jamcoin[14-expo]=temp;
                    }
                    sum+=temp*pow(base,expo);
                    expo++;
                }
                for(int index=2;index<=sqrt(sum);index++){
                    if(sum%index==0){
                        p[base-2]=index;
                        break;
                    }
                }
            }
            for(int as=0;as<9;as++)
                condition*=p[as];
            if(condition!=0){
                cout<<"1";
                for(int qwerty=0;qwerty<14;qwerty++)
                    cout<<jamcoin[qwerty];
                cout<<"1"<<" ";
                for(int qwerty=0;qwerty<8;qwerty++)
                    cout<<p[qwerty]<<" ";
                cout<<p[8]<<endl;
                counter++;
            }
            if(counter==J)
                break;
        }
        T--;
    }
    return 0;
}
