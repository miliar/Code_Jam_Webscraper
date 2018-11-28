#include <cstdio>
#include <iostream>
using namespace std;
size_t TEST_CASES;
int main()
{
    cin>>TEST_CASES;
    for(size_t CASE=0;CASE<TEST_CASES;++CASE)
    {
        int K,C,S;
        cin>>K>>C>>S;
        printf("Case #%ld:",CASE+1);
        for(int i=0;i<S;++i){
            cout<<" "<<i+1;
        }
        cout<<endl;
    }
    return 0;
}
