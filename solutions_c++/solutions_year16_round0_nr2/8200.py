#include <iostream>
using namespace std;

int flip_cake(string cakes)
{
    int times = 0;
    int side = '+';
    int len = cakes.length();
    while (len > 0) {
        if (cakes[len - 1] != side) {
            side = (side == '+' ? '-' : '+');  // flip target side
            times++;
        }
        len--;
    }

    return times;
}

int main(void)
{
    int times;
    cin >> times;

    int seq = 1;

    string buffer;
    while (times-- > 0) {
        cin >> buffer;
        cout << "Case #" << seq << ": " << flip_cake(buffer) << endl;

        seq++;
    }
    return 0;
}
