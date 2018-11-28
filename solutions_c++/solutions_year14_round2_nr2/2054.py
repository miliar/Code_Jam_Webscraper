#include<iostream>
#include<cstring>

using namespace std;


void do_a_case()
{
    long A,B,K;
    int cnt=0;
    cin>>A>>B>>K;
    for(long i=0;i<A;++i)
    for(long j=0;j<B;++j)
    if((i&j)<K)cnt++;
    cout<<cnt<<endl;

}

int main()
{
    int T;
    cin>>T;
    for(int i=0; i<T; ++i)
        {
            cout<<"Case #"<<i+1<<": ";
            //cout<<endl;
            do_a_case();}
    return 0;
}
