#include <iostream>
#include <stdio.h>
#include <math.h>
#include <map>
using namespace std;
 
int main()
{
    int t,i,d,tmp;
    long long int n,n_mul;
    std::ios::sync_with_stdio(false);
    cin >> t;
    for (i = 1; i <= t; ++i) 
    {
        cin >> n;
        if(n==0) {cout << "Case #" << i << ": " << "INSOMNIA" <<endl; continue;}
        map<int,int> m;
        n_mul=n;
        while(m.size()!=10)
        {
            //cout << n_mul << endl;
            tmp=n_mul;
            do {
                d = tmp%10;
                m[d]=1;
                tmp /= 10;
            } while (tmp > 0);
            n_mul+=n;
        }
        cout << "Case #" << i << ": " << n_mul-n << endl;
    }
    return 0;
}