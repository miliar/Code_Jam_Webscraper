#include <iostream>
using namespace std;
#define ll long long
int main()
{
    ll testcase,count=0;
    cin>>testcase;
    while(testcase--){count++;
        string olds;
        cin>>olds;
        string str22="";
        str22=olds[0]+str22;
    for(ll ctr=1;ctr<olds.size();ctr++){
        if(olds[ctr]>=str22[0])
        str22=olds[ctr]+str22;
        else 
        str22=str22+olds[ctr];
    }
    cout<<"Case #"<<count<<": "<<str22<<endl;
    }
    return 0;
}

