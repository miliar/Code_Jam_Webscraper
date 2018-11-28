#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    fstream f1("input.in");
  //  fstream o("output2.txt");
    int t;
    f1 >> t;
    for(int i = 0; i< t; i++){

        double c, f, t;
        double k = 2.00;
        f1 >> c >> f >> t;
        double m1, m2;
        m1 = t / k;
        m2 = (c / k) + t/(f+k) ;
        k = k + f;
        while(m2 <= m1){
            m1 = m2;
            m2 = (c/k) + (t/(f+k)) + m2 - t/k;
            k = k + f;
        }
        cout << "Case #"<<i+1<<": ";
        printf("%.7f\n", m1);
    }
    return 0;
}
