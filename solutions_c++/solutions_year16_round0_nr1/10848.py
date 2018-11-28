#include <iostream>
#include <set>
using namespace std;

int main()
{
    long int t, x=0;
    unsigned long int n;
    cin >> t;

    for (int i = 0; i < t; ++i){
        cin >> n;
        set<int> s;
        long int k = 1;
        int tmp;
        unsigned long int m;
        bool flag = false;
        while(true){
            if(n==0){
                break;
            }
            m = k*n;
            while(m > 0){
                tmp = m%10;
                s.insert(tmp);
                if(s.size() >= 10){
                    flag = true;
                    break;
                }

                m /= 10;
            }

            if(flag)
                break;
            ++k;
        }
        ++x;
        if(n != 0)
            cout << "Case #" << x << ": " << k*n << endl;
        else
            cout << "Case #" << x << ": " << "INSOMNIA" << endl;
    }

    return 0;
}

