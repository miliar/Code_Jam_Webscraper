#include <iostream>
#include <algorithm>
#include <queue>

int reverse(int input) {
    int k = 0;
    while (input) {
        k *= 10;
        k+= input % 10;
        input /= 10;
    }
    return k;
}
int main(int argc, char const* argv[])
{
    int count[1000001]={};
    count[1] = 1;
    std::queue<int> q;
    q.push(1);
    while (!q.empty()) {
        int tmp = q.front();
        q.pop();
        if (tmp > 1000001)
            continue;
        int now = count[tmp] +1;
        if (count[tmp+1]) {
            if (count[tmp+1] > now ) {
                count[tmp+1] = now;
                q.push(tmp+1);
            }
        } else {
            count[tmp+1] = now;
            q.push(tmp+1);
        }
        int r = reverse(tmp);
        if (count[r]) {
            if (count[r] > now) {
                count[r] = now;
                q.push(r);
            }
        } else {
            count[r] = now;
            q.push(r);
        }

    }
    /*
    for (int i = 0; i < 30; i++) {
        printf("(%d, %d)\n", i, count[i]);
    }
    */
    int run;
    std::cin >> run;
    for(int times=1; times <= run; ++times) {
        int z;
        std::cin >> z;
        std::cout << "Case #" << times << ": " << count[z] << std::endl;
    }
    return 0;
}
