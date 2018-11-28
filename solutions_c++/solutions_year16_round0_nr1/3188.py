#include <iostream>
using namespace std;
int main()
{
    long long count,roll=0;
    cin>>count;
    while(count--){
        long long num=0;
        cin>>num;
        if(num==0){
            cout<<"Case #"<<++roll<<": INSOMNIA"<<endl;
        }else{
            int a[10]={0};
            int flag=0;
            int mul=1;
            do{
                long long tmp=num*mul;
                while(tmp!=0){
                    a[tmp%10]=1;
                    tmp/=10;
                }
                flag=1;
                for(int i=0;i<10;i++){
                    if(a[i]!=1){
                        flag=0;
                        break;
                    }
                }
                mul++;
            }while(flag==0);
            cout<<"Case #"<<++roll<<": "<<num*(mul-1)<<endl;
        }

    }
}
