#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>

using namespace std;

const double pow2[41] = {1.0 , 2.0 , 4.0 , 8.0 , 16.0 , 32.0 , 64.0 , 128.0 , 256.0 , 512.0 , 1024.0 ,
2048.0 , 4096.0 , 8192.0 , 16384.0 , 32768.0 , 65536.0 , 131072.0 , 262144.0 , 524288.0 , 1048576.0 ,
2097152.0 , 4194304.0 , 8388608.0 , 16777216.0 , 33554432.0 , 67108864.0 , 134217728.0 , 268435456.0 ,
536870912.0 , 1073741824.0 , 2147483648.0 , 4294967296.0 , 8589934592.0 , 17179869184.0 , 34359738368.0 ,
68719476736.0 , 137438953472.0 , 274877906944.0 , 549755813888.0 , 1099511627776.0 };

int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

void SolveTestcase(int testcase){
    std::string line;
    std::cin >> line;
    int pos = line.find('/');
    std::string sP = line.substr(0, pos);
    std::string sQ = line.substr(pos+1, line.length() - pos);

    std::istringstream ssP(sP);
    std::istringstream ssQ(sQ);

    unsigned int P,Q;
    ssP >> P;
    ssQ >> Q;

    int G = gcd(P,Q);
    P = P / G;
    Q = Q / G;

    double res = (double) Q/P;
    if (res == 1.0){
        std::cout << "Case #" << testcase << ": 0" << std::endl;
        return ;
    }

    bool CanBe = false;
    for (int i=1; i<=20; i++){
        CanBe = (CanBe || (Q == pow2[i]));
    }
    if (!CanBe){
        std::cout << "Case #" << testcase << ": impossible" << std::endl;
        return ;
    }

    int ans = 0;
    for (ans = 1; ans <= 40; ans++){
        if ((res <= pow2[ans]) && (res > pow2[ans-1])){
            std::cout << "Case #" << testcase << ": " << ans << std::endl;
            return ;
            break;
        }
    }
    std::cout << "Case #" << testcase << ": impossible" << std::endl;
}


int main(){
    int T;
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++)
        SolveTestcase(testcase);
    fclose(stdin);
    fclose(stdout);
    return 0;
}
