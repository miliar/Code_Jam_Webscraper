/*
* @Author: ahteeGang
* @Date:   2016-04-09 12:26:17
* @Last Modified by:   ahteeGang
* @Last Modified time: 2016-04-09 12:26:17
*/

#include <iostream>
using namespace std;

unsigned long int findSheep(unsigned long int n)
{
    bool digit[10] = {false};
    bool succ;
    int i = 1;
    unsigned long int temp;
    do {
        temp = i * n;
        while (temp != 0) {
            if (!digit[temp % 10]) {
                digit[temp % 10] = true;
            }
            temp /= 10;
        }
        succ = true;
        for (int j = 0; j < 10; j++) {
            if (!digit[j]) {
                succ = false;
            }
        }
        i++;
    } while (!succ);
    return n * (i - 1);
}

int main()
{
    int loop;
    unsigned long int n;
    cin >> loop;
    for (int i = 0; i < loop; i++) {
        cin >> n;
        if (n)
            cout << "Case #" << i + 1 << ": " << findSheep(n) << endl;
        else
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
    }
    return 0;
}