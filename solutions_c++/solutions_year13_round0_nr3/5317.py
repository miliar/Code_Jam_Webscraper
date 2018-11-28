#include <iostream>
#include<math.h>
bool is_pal(int num);
int main()
{
    int test_cases;
    std::cin >> test_cases;
    for (int i=0;i<test_cases;++i){
        int count = 0;
        int min; int max;
        std::cin >> min; std::cin>>max;
        std::cout<<"Case #"<<(i+1)<<": ";
        for (int j=min;j<=max;++j){
            if (is_pal(j)){
                double root = (sqrt(j));
                if (fmod(root,1)==0){
                    if (is_pal(root)){
                        ++count;
                    }
                }
            }
        }
        std::cout<<count<<std::endl;
    }
    return 0;
}
bool is_pal(int num){
    int sum =0;
    int tmp  = num;
    while(tmp>0){
        sum *=10;
        sum += (tmp%10);
        tmp = tmp/10;
    }
    return (sum == num);
}
