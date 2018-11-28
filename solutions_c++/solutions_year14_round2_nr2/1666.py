#include<iostream>
#include<vector>
#include <time.h> 
using namespace std;

int main()
{
     freopen("B_out.txt","w",stdout);
     freopen("B-small-attempt0(1).in","r",stdin);
    int TT;
    cin>>TT; 
    for (int T = 1; T<=TT; T++)
    {
        int A,B,K;
        cin>>A>>B>>K;
        int cnt = 0;
 //      cout<<(0&2)<<endl;
        for(int a=0;a<A;a++)
        {
                for(int b=0;b<B;b++)
                { 
                        if ((a&b) < K)
                        {
                            
                                cnt++;
                        }//cout<<a<<" "<<b<<" "<<(a&b)<<endl;
                }
        }
        
        cout<<"Case #"<<T<<": "<<cnt<<endl;
    } 
    return 0;
    
}
