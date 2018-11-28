#include <iostream>
#include <istream>
#include <fstream>
using namespace std;
int main()
{
    ifstream reader("input.txt");
	ofstream writer("output.txt");
    int t;
    double c, f, x,dbuy,buy_temp,cookies,time;
    int flag=1;
    reader >> t;
    for(int i = 0; i < t; i++) {
        reader >> c >> f >> x;
        time = 0;
        cookies = 2;
        flag = 1;
         do{
            dbuy = x/cookies + time;
            buy_temp = c/cookies + x/(cookies + f) + time;
            if(buy_temp < dbuy)
                {
                time += c/cookies;
                cookies += f;
                }
            else {
                time = dbuy;
                flag = 0;
            }
        }while(flag==1);
        writer.precision(7);
        writer.setf(ios::fixed, ios::floatfield);
        writer << "Case #" << i + 1 << ": " << time << endl;
    }
    return 0;
}
