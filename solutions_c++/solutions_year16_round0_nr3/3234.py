#include <iostream>
#include <cmath>
using namespace std;
int findfactor(long long a)
{
    int limit = int(sqrt(double(a)));
    for (int i = 2; i <= limit; i++)
    {
        if (a % i == 0) return i;
    }
    return 1;
}
long long base(int b,int * number)
{
    long long ret = 0;
    for (int i = 15; i >= 0; i --)
    {
        ret *= b;
        ret += number[i];
    }
    return ret;
}
int main() {
    freopen("C-small.out","w",stdout);
    int times;

    printf("Case #1:\n");
    int J = 50;
    int current = (1 << (16-1))-1;
    int list[15];
    int number[16];
    while (J > 0)
    {
        bool flag = true;
        current += 2;
        int temp = current;
        for (int i = 0; i < 16; i++,temp /= 2)
            number[i] = temp % 2;
        for (int i = 2; i <= 10; i++){
            list[i] = findfactor(base(i,number));
            if (list[i] == 1){
                flag = false;
                break;
            }
        }
        if (!flag) continue;
        cout << base(10,number);
        for (int i = 2; i <= 10; i++){
            printf(" %d",list[i]);
        }
        printf("\n");
        J --;
    }

}