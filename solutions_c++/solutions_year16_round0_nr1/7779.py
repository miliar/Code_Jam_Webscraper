#include <iostream>
#include <set>
#include <stdlib.h>
#include <cstdlib>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output_file_name1.out","w",stdout);
    long long T,n,tmp,k;
    bool f=false;
    cin>>T;
    k=1;
    while(T--){
        cin>>n;
        set<int> s;
        tmp=n;
        f=false;
        for(int i=1; i<100000; i++){
            tmp*=i;
            while(tmp){
                s.insert(tmp%10);
                tmp/=10;
            }
            if(s.size()==10){
                cout<<"Case #"<<k<<": "<<i*n<<endl;
                f=true;
                break;
            }
            tmp=n;
        }
        if(!f){
            cout<<"Case #"<<k<<": INSOMNIA"<<endl;
        }
        k++;

    }
    return 0;
}
