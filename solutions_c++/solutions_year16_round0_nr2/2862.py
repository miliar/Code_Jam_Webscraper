#include <cstdio>
#include <iostream>
using namespace std;
size_t TEST_CASES;
int main()
{
    cin>>TEST_CASES;
    for(size_t CASE=0;CASE<TEST_CASES;++CASE)
    {
        string pancakes;
        cin>>pancakes;
        char pre=' ';
        int ans=0;
        for(int i=0;i<(int)pancakes.size();++i){
            if(pancakes[i]!=pre){
                ans++;
                pre=pancakes[i];
            }
        }
        if(pancakes[pancakes.size()-1]=='+') ans--;
        printf("Case #%ld: %d\n",CASE+1,ans);
    }
    return 0;
}
