#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <math.h>

using namespace std;

bool palindroma (int m){
    int n = log10(m);
    int a = 1;
    int b = 10;
    for (int i = 0;i < n;++i)
        a*=10;
    //cout<<n<<endl;
    for (int i = 0; i < n/2 + 1; ++i){
            //cout<<m%b<<" "<<m/a<<endl;
        if (m%b != m/a)
            return false;
        m/=10;b/=10;
        if (log10(m%10) == 0)
            break;
    }


    return true;
}

int main(){


    int a,b,n,o=0;
    cin>>n;
    while(n--){
        cin>>a>>b;
    int c=0;
        for (int i = a;i <= b; ++i){
            if (palindroma(i)){
                    int n1 = sqrt(i);
                    if (n1*n1 == i){
                        if (palindroma(n1))
                        c++;
                    }
            }
        }
        cout<<"Case #"<<++o<<": "<<c<<endl;

    }

    return 0;
}
