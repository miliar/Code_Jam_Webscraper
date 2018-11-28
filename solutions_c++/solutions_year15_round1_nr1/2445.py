#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large-practice.in","r",stdin);
    freopen("A-large-practice.out","w",stdout);

    int count = 0;
    int T;
    cin>>T;
    int N;
    while(T--){
        cin>>N;
        vector<int> m(N,0);
        for(int i=0;i<N;++i){
            cin>>m[i];
        }

        long long res1 = 0,res2 = 0;
        for(int i=1;i<N;++i){
            if(m[i-1]>m[i])
                res1 += m[i-1]-m[i];
        }
       
        int rate = 0;
        for(int i=1;i<N;++i){ 
            if(m[i-1]-m[i] > rate)
                rate = m[i-1] - m[i];
        }
        for(int i=0;i<N-1;++i){
            if(m[i]<= rate)
                res2 += m[i];
            else
                res2 += rate;
        }

        cout<<"Case #"<<++count<<": ";
        cout<<res1<<" "<<res2<<endl;
    }

    return 0;
}
