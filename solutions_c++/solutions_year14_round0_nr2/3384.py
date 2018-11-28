#include <iostream>
#include <istream>
#include <fstream>
using namespace std;
int main()
{
    ifstream reader("input.txt");
	ofstream writer("output.txt");
    int t;
    double c, f, x,dontbuy,buy,no_of_cookie,time_total;
    int flag=1;
    reader >> t;
    for(int i = 0; i < t; i++) {
        reader >> c >> f >> x;
        time_total = 0;
        no_of_cookie = 2;
        flag = 1;
        while(flag==1) {
            dontbuy = x/no_of_cookie + time_total;
            buy = c/no_of_cookie + x/(no_of_cookie + f) + time_total;
            if(buy < dontbuy)
                {
                time_total += c/no_of_cookie;
                no_of_cookie += f;
                }
            else {
                time_total = dontbuy;
                flag = 0;
            }
        }
        writer.precision(7);
        writer.setf(ios::fixed, ios::floatfield);
        writer << "Case #" << i + 1 << ": " << time_total << endl;
    }
    return 0;
}
