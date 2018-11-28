/*
 * =====================================================================================
 *
 *       Filename:  2.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2014/04/13 00时58分10秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main() {
    int t;
    cin>>t;
    for (int ncase = 1; ncase <= t; ncase++) {
        double c,f,x;
        cin>>c>>f>>x;
        double result = 100000;
        for (int i = 0; ; i++) {
            double amount = 0;
            double rate = 2;
            double tmpresult = 0;
            bool invalid = false;
            for (int j = 1; j <= i; j++) {
                tmpresult += c / rate;
                rate += f;
                if (amount > x) {
                    invalid = true;
                }
            }
            if (invalid) {
                break;
            }
            tmpresult += (x - amount) / rate;
            if (tmpresult < result) {
                result = tmpresult;
            }
            else {
                break;
            }
        }
        printf("Case #%d: %.7lf\n", ncase, result);
    }
    return 0;
}
