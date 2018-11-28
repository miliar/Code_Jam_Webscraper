#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    //freopen("test", "r", stdin);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        long long int n;
        bool a[10] = {false};
        cin>>n;
        if (n == 0)
            cout<<"Case #"<<testcase+1<<": "<<"INSOMNIA"<<endl;
        else {
            long long int c = 0, i = 1, num;
            while (c!=10) {
                num = i*n;
                while(num!=0) {
                    int j = num%10;
                    if (!a[j]) {
                        a[j] = true;
                        c++;
                    }
                    num = num/10;
                }
                i+=1;
            }
            cout<<"Case #"<<testcase+1<<": "<<(i-1)*n<<endl;
        }
    }
    return 0;
}
