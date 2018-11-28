#include<iostream>
#include<string>
#include<vector>
#include<cmath>
int main()
{
    int T;
    std::cin>>T;
    int n=T;
    while(T--)
    {
        long A,B,K;
        std::cin>>A>>B>>K;
        long sum=0;
        for(int i=0;i<A;++i)
            for(int j=0;j<B;++j)
                if((i&j)<K)
                    sum++;
//         std::cout<<sum;
//         for(int i=0;i<std::min(A,B);++i)
//             if(i<K)
//                 sum--;
        std::cout<<"Case #"<<n-T<<": "<<sum<<std::endl;
        
    }
}