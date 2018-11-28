#include <iostream>

using namespace std;

char qmul(char a, char b);

int main()
{
    char s[10000];
    int t;
    cin >> t;
    for (int c = 0; c < t; ++c) {
        int l, x;
        cin >> l >> x;
        int len = l * x;
        for (int i = 0; i < l; ++i) {
            cin >> s[i];
        }
        // search for leftmost i
        int left = 0;
        int res = '1';
        while (left < len-1) {
            res = qmul(res, s[left%l]);
            if (res == 'i')
                break;
            ++left;
        }
        // search for rightmost k
        int right = len-1;
        res = '1';
        while (right > 0) {
            res = qmul(s[right%l], res);
            if (res == 'k')
                break;
            --right;
        }
        //check for middle part
        res = '1';
        if ((right-left-1) <= l) {
            for (int i = left+1; i < right; ++i) {
                res = qmul(res, s[i%l]);
            }
        } else {
            char lres = '1';
            int i, j;
            for (i = left+1; i%l != 0; ++i) {
                lres = qmul(lres, s[i%l]);
            }
            char rres = '1';
            for (j = right-1; j%l != (l-1); --j) {
                rres = qmul(s[j%l], rres);
            }
            char pres = '1';
            for (int k = 0; k < l; ++k) {
                pres = qmul(pres, s[k]);
            }
            int z = (j-i+1) / l;
            char mres = '1';
            for (int k = 0; k < (z%4); ++k) {
                mres = qmul(mres, pres);
            }
            res = qmul(lres, mres);
            res = qmul(res, rres);
        }
        // result check
        if ((res == 'j') && (left < len-2) && (right > 1)) {
            cout << "Case #" << c+1 << ": YES" << endl;
        } else {
            cout << "Case #" << c+1 << ": NO" << endl;
        }
    }

    return 0;
}

char qmul(char a, char b)
{
    switch (a) {
        case '1':
            switch (b) {
                case '1':
                    return '1';
                case 'i':
                    return 'i';
                case 'j':
                    return 'j';
                case 'k':
                    return 'k';
                case 'r':
                    return 'r';
                case 'I':
                    return 'I';
                case 'J':
                    return 'J';
                case 'K':
                    return 'K';
            }
        case 'i':
            switch (b) {
                case '1':
                    return 'i';
                case 'i':
                    return 'r';
                case 'j':
                    return 'k';
                case 'k':
                    return 'J';
                case 'r':
                    return 'I';
                case 'I':
                    return '1';
                case 'J':
                    return 'K';
                case 'K':
                    return 'j';
            }
        case 'j':
            switch (b) {
                case '1':
                    return 'j';
                case 'i':
                    return 'K';
                case 'j':
                    return 'r';
                case 'k':
                    return 'i';
                case 'r':
                    return 'J';
                case 'I':
                    return 'k';
                case 'J':
                    return '1';
                case 'K':
                    return 'I';
            }
        case 'k':
            switch (b) {
                case '1':
                    return 'k';
                case 'i':
                    return 'j';
                case 'j':
                    return 'I';
                case 'k':
                    return 'r';
                case 'r':
                    return 'K';
                case 'I':
                    return 'J';
                case 'J':
                    return 'i';
                case 'K':
                    return '1';
            }
        case 'r':
            switch (b) {
                case '1':
                    return 'r';
                case 'i':
                    return 'I';
                case 'j':
                    return 'J';
                case 'k':
                    return 'K';
                case 'r':
                    return '1';
                case 'I':
                    return 'i';
                case 'J':
                    return 'j';
                case 'K':
                    return 'k';
            }
        case 'I':
            switch (b) {
                case '1':
                    return 'I';
                case 'i':
                    return '1';
                case 'j':
                    return 'K';
                case 'k':
                    return 'j';
                case 'r':
                    return 'i';
                case 'I':
                    return 'r';
                case 'J':
                    return 'k';
                case 'K':
                    return 'J';
            }
        case 'J':
            switch (b) {
                case '1':
                    return 'J';
                case 'i':
                    return 'k';
                case 'j':
                    return '1';
                case 'k':
                    return 'I';
                case 'r':
                    return 'j';
                case 'I':
                    return 'K';
                case 'J':
                    return 'r';
                case 'K':
                    return 'i';
            }
        case 'K':
            switch (b) {
                case '1':
                    return 'K';
                case 'i':
                    return 'J';
                case 'j':
                    return 'i';
                case 'k':
                    return '1';
                case 'r':
                    return 'k';
                case 'I':
                    return 'j';
                case 'J':
                    return 'I';
                case 'K':
                    return 'r';
            }
    }
}
