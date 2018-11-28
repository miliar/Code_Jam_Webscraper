#include <iostream>
#include <stdio.h>
#include <string>
#include <sstream>

using namespace std;

int main() {
    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
    int T;
	scanf("%d",&T);
    int in [T];
    int digit [10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    int size = 0;

    for (int i=0; i<T; i++) {
        scanf("%d",&in[i]);
    }

    bool stop = false;
    bool found = false;

    for (int x=0; x<T; x++) {
        int no = in[x];
        int iterator = 1;
        int res;

        if (no == 0) {
            stop = true;
            cout << "Case #" << x+1 << ": INSOMNIA" << endl;
        }

        while (stop != true) {
            res = no*iterator;
            stringstream ss;
            ss << res;
            string str = ss.str();
            for (int y=0; y<str.length(); y++) {
                char c = str.at(y);
                int dig = c - '0';
                if (digit[dig] == -1) {
                    digit[dig] = dig;
                    size++;
                }
            }

            // printf("%d %d %d %d %d %d %d %d %d %d\n",digit[0],digit[1],digit[2],digit[3],digit[4],digit[5],digit[6],digit[7],digit[8],digit[9]);

            if (size==10) {
                stop = true;
                printf("Case #%d: %d\n", x+1, res);
                size=0;
            }
            iterator++;
        }

        // clear digit array
        for (int y=0; y<10; y++) {
            digit[y] = -1;
        }

        stop = false;
        iterator =1;
        res = 0;
    }
    return 0;
}
