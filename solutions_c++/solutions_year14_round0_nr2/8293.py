#include<stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<fstream>
#include<iostream>
#include <iomanip>
using namespace std;

double c,f,x,rate,time1;

int main(){
    int i,j;
    int t,t1;
    ifstream cin("2.in");
    ofstream cout("2.out");
    cin >> t;
    for(t1=1;t1<=t;t1++)
    {
        cin >> c >> f >> x;
        rate = 2;
        time1 = 0;
        for(;;)
        {
            if(x/rate <= c/rate + x/(rate+f)){
                time1 += x/rate;
                break;
            }else{
                time1 += c/rate;
                rate += f;
            }
        }
        cout << "Case #" << t1 << ": " << fixed << setprecision(7) << time1 << endl;
    }
    scanf(" ");
}
