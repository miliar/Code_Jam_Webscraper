#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <stdio.h>
using namespace std;

class Quaternion {
    public:
        char type;
        int  sign;
        Quaternion(char type, int sign);
        Quaternion(int sign);
};

Quaternion::Quaternion(int s) {
    sign = s;
}

Quaternion::Quaternion(char t, int s) {
    type = t;
    sign = s;
}

void printError(char c) {
    printf ("Something went wrong: got %c\n", c);
}

Quaternion multiply (Quaternion q_left, Quaternion q_right) {
    Quaternion q_product(1);

    switch (q_left.type) {
        case '1':
            q_product.type = q_right.type;
            break;
        case 'i':
            switch (q_right.type) {
                case '1':
                    q_product.type = 'i';
                    break;
                case 'i':
                    q_product.type = '1';
                    q_product.sign = -1;
                    break;
                case 'j':
                    q_product.type = 'k';
                    break;
                case 'k':
                    q_product.type = 'j';
                    q_product.sign = -1;
                    break;
                default: printError(q_right.type);
            }
            break;

        case 'j':
            switch (q_right.type) {
                case '1':
                    q_product.type = 'j';
                    break;
                case 'i':
                    q_product.type = 'k';
                    q_product.sign = -1;
                    break;
                case 'j':
                    q_product.type = '1';
                    q_product.sign = -1;
                    break;
                case 'k':
                    q_product.type = 'i';
                    break;
                default: printError(q_right.type);
            }
            break;


        case 'k':
            switch (q_right.type) {
                case '1':
                    q_product.type = 'k';
                    break;
                case 'i':
                    q_product.type = 'j';
                    break;
                case 'j':
                    q_product.type = 'i';
                    q_product.sign = -1;
                    break;
                case 'k':
                    q_product.type = '1';
                    q_product.sign = -1;
                    break;
                default: printError(q_right.type);
            }
            break;

        default: printError(q_left.type);
    }
    
    q_product.sign = q_product.sign * q_left.sign * q_right.sign;
    return q_product;
}

Quaternion get_inverse(Quaternion q) {
    switch (q.type) {
        case '1':
            return Quaternion(q.type, q.sign);
            break;
        default:
            return Quaternion(q.type, q.sign * (-1));
    }
}


void test() {
    string Qs = "1ijk";

    for (int i = 0; i < 4; i++) {
        Quaternion q_left(Qs[i], 1);
        
        for (int j = 0; j < 4; j++) {
            Quaternion q_right(Qs[j], 1);
            Quaternion q_product = multiply(q_left, q_right);

            if (q_left.sign == -1) {
                printf("-");
            }
            else {
                printf(" ");
            }
            printf("%c * %c = ", q_left.type, q_right.type);

            if (q_product.sign == -1) {
                printf("-");
            }
            else {
                printf(" ");
            }
            printf("%c\n", q_product.type);
        }
        printf("\n");
    }

    for (int i = 0; i < 4; i++) {
        Quaternion q_left(Qs[i], -1);
        
        for (int j = 0; j < 4; j++) {
            Quaternion q_right(Qs[j], 1);
            Quaternion q_product = multiply(q_left, q_right);

            if (q_left.sign == -1) {
                printf("-");
            }
            else {
                printf(" ");
            }
            printf("%c * %c = ", q_left.type, q_right.type);

            if (q_product.sign == -1) {
                printf("-");
            }
            else {
                printf(" ");
            }
            printf("%c\n", q_product.type);
        }
        printf("\n");
    }

    for (int i = 0; i < 4; i++) {
        Quaternion q_left(Qs[i], -1);
        
        for (int j = 0; j < 4; j++) {
            Quaternion q_right(Qs[j], -1);
            Quaternion q_product = multiply(q_left, q_right);

            printf("-%c * -%c = ", q_left.type, q_right.type);

            if (q_product.sign == -1) {
                printf("-");
            }
            else {
                printf(" ");
            }
            printf("%c\n", q_product.type);
        }
        printf("\n");
    }

    for (int i = 0; i < 4; i++) {
        Quaternion q(Qs[i], 1); 
        Quaternion inv = get_inverse(q);
        printf("inverse(%c) = ", q.type);
        if (inv.sign == -1) {
            printf("-");
        }
        printf("%c\n", inv.type);
    }
    for (int i = 0; i < 4; i++) {
        Quaternion q(Qs[i], -1); 
        Quaternion inv = get_inverse(q);
        printf("inverse(-%c) = ", q.type);
        if (inv.sign == -1) {
            printf("-");
        }
        printf("%c\n", inv.type);
    }
}

/*
string answer(int L, int X, string str) {

    Quaternion q_i;
    q_i.type = '1';
    q_i.sign = 1;
    for (int i = 0; i < L*X; i++) {
        // look for i
        q_i = multiply (q_i, str[i]);
        if (q_i.type != 'i') {
            continue;
        }

        // look for j
        Quaternion q_j;
        q_j.type = '1';
        q_j.sign = 1;
        for (int j = i + 1; j < L*X; j++) {
            printf ("i = %d, j = %d \n", i, j);
            q_j = multiply(q_j, str[j]);
            if (q_j.type != 'j') {
                continue;
            }

            // Check if the remaining characters in the third section multiply to get 'k'
            Quaternion q_k;
            q_k.type = '1';
            q_k.sign = 1;
            for (int k = j + 1; k < L*X; k--) {
                q_k = multiply(q_k, str[k]);
            }
            if (q_k.type == 'k') {
                return "YES";
            }
        }
    }

    return "NO";
}
*/

string answer(int L, int X, string str) {
    bool i_found = false;
    bool k_found = false;
    int i_pos_end;
    int k_pos_start;

    Quaternion q_i('1', 1);
    Quaternion q_j('1', 1);
    Quaternion q_k('1', 1);

    // find the leftmost 'i'
    for (int i = 0; i < L*X; i++) {
        Quaternion q_right(str[i], 1);
        q_i = multiply(q_i, q_right);
        if (q_i.type == 'i' && q_i.sign == 1) {
            i_found = true;
            i_pos_end = i;
            break;
        }
    }

    // find the rightmost 'k'
    for (int k = L*X -1; k > i_pos_end; k--) {
        Quaternion q_left(str[k], 1);
        q_k = multiply(q_left, q_k);
        if (q_k.type == 'k' && q_k.sign == 1) {
            k_found = true;
            k_pos_start = k;
            break;
        }
    }

    if (i_found == false || k_found == false) {
        return "NO";
    }

    // Get the product of the middle section.
    for (int j = i_pos_end + 1; j < k_pos_start; j++) {
        Quaternion q_right(str[j], 1);
        q_j = multiply(q_j, q_right);
    }
    if (q_j.type == 'j' && q_j.sign == 1) {
        return "YES";
    }

    for (int k = k_pos_start - 1; k > i_pos_end; k--) {
        Quaternion q_left(str[k], 1);
        Quaternion inv = get_inverse(q_left);
        q_k = multiply(q_left, q_k);
        q_j = multiply(q_j, inv);
    //return"HERE";

        if (q_k.type != 'k' || q_k.sign != 1) {
            continue;
        }

        Quaternion q_i_copy(q_i.type, q_i.sign);
        Quaternion q_j_copy(q_j.type, q_j.sign);
        for (int i = i_pos_end + 1; i < k; i++) {
            Quaternion q_right(str[i], 1);
            Quaternion inv = get_inverse(q_right);
            q_i_copy = multiply(q_i_copy, q_right);
            q_j_copy = multiply(inv, q_j_copy);
            
            if (q_i_copy.type == 'i' && q_i_copy.type == 1) {
                if (q_j_copy.type == 'j' && q_j_copy.type == 1) {
                    return "YES";
                }
            }
        }
    }
     
    return "NO";
}


int main() {

    //test();
    //return 0;

    int T;
    int L;
    int X;
    string s;
    string str;
    cin >> T;

    for (int t = 0; t < T; t++) {
        cin >> L;
        cin >> X;
        cin >> s;

        string str = "";
        for (int i = 0; i < X; i++) {
            str += s;
        }

        string ans = answer(L, X, str);
        printf("Case #%d: %s\n", t+1, ans.c_str());
    }
    
    return 0;
}
