#include<iostream>
using namespace std;
int main()
{
    int N;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        int A,B,K;
        cin>>A>>B>>K;
        int cnt=0;
        for(int l=0;l<A;l++)
        {
            for(int h=0;h<B;h++)
            {
                int a=l&h;
               //cout<<l<<h<<a<<endl;

               if(a < K)
                cnt++;
            }
        }
        cout <<"Case #"<<i+1<<": "<<cnt<<endl;
    }
    return 0;

}
