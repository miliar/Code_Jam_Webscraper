#include <cstdio>
#include <iostream>
using namespace std;
size_t TEST_CASES;
int main()
{
    cin>>TEST_CASES;
    for(size_t CASE=0;CASE<TEST_CASES;++CASE)
    {
        long long num;
        long long current_num=0;
        int count[10]={0};
        int has=0;
        cin>>num;
        printf("Case #%ld: ",CASE+1);
        if(num==0){
            cout<<"INSOMNIA"<<endl;
        }else{
            for(int i=0;i<1000;++i){
                current_num+=num;
                long long ntmp=current_num;
                while(ntmp>0){
                    int m=ntmp%10;
                    if(count[m]==0){
                        count[m]=1;
                        has++;
                        if(has==10){
                            goto end;
                        }
                    }
                    ntmp/=10;
                }
            }
end:;
    //if(has<10) cout<<"What"<<endl;
    //else cout<<endl;
    cout<<current_num<<endl;
        }
    }
    return 0;
}
