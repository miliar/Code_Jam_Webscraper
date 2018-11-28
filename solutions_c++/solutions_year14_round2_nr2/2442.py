#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
#include <fstream>
using namespace std;

int main()
{
    long long T, A, B, K;
    fstream f, out;
    f.open ("testB.txt", std::fstream::in | std::fstream::out | std::fstream::app);
    out.open("resultB.txt", std::fstream::in | std::fstream::out | std::fstream::app);

    f >> T;
    for(int i = 1; i <= T; i++){
        f >> A;
        f >> B;
        f >> K;
        long long count = 0;
        for(int j = 0; j < K; j++){
            for(int a = 0; a < A; a++){
                for(int b = 0; b < B; b++){
                    long long num = a & b;
                    if(num == j){
                        count++;
                    }
                }
            }
        }

        out << "Case #" << i << ": " << count << endl;
    }

    return 0;
}

