#include <iostream>
#include <fstream>

using namespace std;

ifstream in("a.in");
ofstream out("a.out");

int main()
{
    int t;
    in>>t;
    for(int i=1;i<=t;++i){
        int n;
        in>>n;
        if(n==0)out<<"Case #"<<i<<": INSOMNIA"<<endl;
        else{
            bool d[10];
            for(int j=0;j<10;++j)d[j]=0;
            int m;
            for(m=n;;m+=n){
                int k=m;
                while(k){
                    d[k%10]=1;
                    k/=10;
                }
                bool c=1;
                for(int j=0;j<10;++j){
                    if(!d[j]){
                        c=0;
                        break;
                    }
                }
                if(c)break;
            }
            out<<"Case #"<<i<<": "<<m<<endl;
        }
    }
    return 0;
}
