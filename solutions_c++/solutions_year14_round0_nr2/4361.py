//
//  main.cpp
//  DemoTest
//
//  Created by mezheng on 10/14/13.
//
//

#include <iostream>
#include <algorithm>
#include <vector>
#include<iomanip>
using namespace std;

int main(int argc, const char * argv[])
{
    int n;
    double c, f, x;
    cin>>n;
    for (int i=1; i<=n; i++) {
        cin >> c >> f >> x;
        cout << "Case #" << i << ": ";
        double sum = 0.0;
        double speed = 2.0;
        if (x <= c) {
            sum = x / 2.0;
        } else {
            sum += c / speed;
            while (((x-c) / speed) > (x / (speed + f))) {
                speed += f;
                sum += c/speed;
            }
            sum += (x-c)/speed;
        }
        cout<<setiosflags(ios::fixed)<<setprecision(7)<<sum<<endl;
    }
    return 0;
}

