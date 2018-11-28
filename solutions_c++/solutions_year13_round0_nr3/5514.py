#include <iostream>
#include <stdint.h>

using std::cin;
using std::cout;


int main()
{
    size_t n;
    uint32_t num[] = {1, 4, 9, 121, 484};

	freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    cin >> n;

    for(size_t i = 0; i < n; ++i) {
        uint32_t a;
        uint32_t b;
        int x = 0;
        int y = 0;
        int res = 0;

        cin >> a >> b;

		if(b < num[0] || a > num[4]) {
	        cout << "Case #" << i+1 << ": 0" << std::endl;
			continue;
		}

        for(size_t j = 0; j < 5; ++j) {
            if(a <= num[j]) {
                if(a == num[j]) {
                    ++res;
                    x = j;
                }
                else
                    x = j - 1;
                break;
            }
        }
        for(size_t j = 4; j > 0; --j) {
            if(b >= num[j]) {
                y = j;
                break;
            }
        }

        cout << "Case #" << i+1 << ": ";
        cout << y-x+res << std::endl;
    }

    return 0;
}
