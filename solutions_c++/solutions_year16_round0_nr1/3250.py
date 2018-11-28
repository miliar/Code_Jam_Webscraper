#include <iostream>
#include <set>

using namespace std;

#define ull unsigned long long

int main() {
    ull T,N,c,m,n,d,size;
    cin>>T;
    for(ull t=1;t<=T;t++)
    {
        cin>>N;
        ull A[10]={0};
        set<ull> s;
        c=10;
        m=0;
        while(c)
        {
            m+=N;
            n=m;
            size=s.size();
            s.insert(n);
            if(s.size()==size)
                break;
            while(n)
            {
                d=n%10;
                if(A[d]==0)
                {
                    A[d]=1;
                    c--;
                }
                n/=10;
            }
        }
        if(c==0)
            cout<<"Case #"<<t<<": "<<m<<endl;
        else
            cout<<"Case #"<<t<<": "<<"INSOMNIA\n";
    }
    return 0;
}