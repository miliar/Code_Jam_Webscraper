#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;


int main(){
    ifstream in("/Users/tech8/Desktop/Ainput.txt");
    ofstream out("/Users/tech8/Desktop/Aoutput.txt");
    long long t;
    in >> t;
    for(int s = 0; s < t; s++)
    {
        long long n;
        in >> n;
        long long a[10];
        memset(a, 0, sizeof(a));
        if(n == 0){
            out << "Case #"<< s + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }else
        {
            long long cnt = 0;
            long long i = 0;
            long long m = n;
            while(true) {
                bool flag = false;
                i++;
                n = m * i;
                do {
                    long long x = n % 10;
                    if(a[x] == 0){
                        a[x] = 1;
                        cnt++;
                    }
                    if (cnt == 10) {
                        flag = true;
                        break;
                    }
                    n = n/10;
                    if(n == 0)break;
                } while (n != 0);
                if (flag == true)break;
            }
            out << "Case #"<< s + 1 << ": " << m * i << endl;
        }

    }
}




