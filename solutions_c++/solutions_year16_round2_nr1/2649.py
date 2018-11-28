#include<stdio.h>
// WFOXOURIST
// 0=>zero
//    one
//    two
//    three
//    four
//    five
//    six
//    seven
//    eight
//    nine
//
// e->9
// f->
// g->
// h->
// i->9
// n->9(2)
// o->
// r->
// s->
// t->
// u->
// v->
// w->
// x->
// z->
int main()
{
    int count[26], digits[10];
    int i, j, k;
    int cases, pp = 0;
    char s[2001];

    scanf("%d", &cases);
    while (cases--) {
        scanf("%s", s);
        for (i = 0; i < 26; i++) count[i] = 0;
        for (i = 0; i < 10; i++) digits[i] = 0;
        i = j = 0;

        while (s[i] != '\0') {
            count[s[i] - 'A']++;
            j++;i++;
        }

        while (j > 0) {
            k = count['G' - 'A'];
            if (k) {
                digits[8] += k;
                count['E' - 'A'] -= k;
                count['I' - 'A'] -= k;
                count['G' - 'A'] -= k;
                count['H' - 'A'] -= k;
                count['T' - 'A'] -= k;
                j -= k * 5;
            }

            k = count['H' - 'A'];
            if (k) {
                digits[3] += k;
                count['T' - 'A'] -= k;
                count['H' - 'A'] -= k;
                count['R' - 'A'] -= k;
                count['E' - 'A'] -= k;
                count['E' - 'A'] -= k;
                j -= k * 5;
            }

            k = count['T' - 'A'];
            if (k) {
                digits[2] += k;
                count['T' - 'A'] -= k;
                count['W' - 'A'] -= k;
                count['O' - 'A'] -= k;
                j -= k * 3;
            }

            k = count['U' - 'A'];
            if (k) {
                digits[4] += k;
                count['F' - 'A'] -= k;
                count['O' - 'A'] -= k;
                count['U' - 'A'] -= k;
                count['R' - 'A'] -= k;
                j -= k * 4;
            }

            k = count['F' - 'A'];
            if (k) {
                digits[5] += k;
                count['F' - 'A'] -= k;
                count['I' - 'A'] -= k;
                count['V' - 'A'] -= k;
                count['E' - 'A'] -= k;
                j -= k * 4;
            }

            k = count['R' - 'A'];
            if (k) {
                digits[0] += k;
                count['Z' - 'A'] -= k;
                count['E' - 'A'] -= k;
                count['R' - 'A'] -= k;
                count['O' - 'A'] -= k;
                j -= k * 4;
            }

            k = count['O' - 'A'];
            if (k) {
                digits[1] += k;
                count['O' - 'A'] -= k;
                count['N' - 'A'] -= k;
                count['E' - 'A'] -= k;
                j -= k * 3;
            }

            k = count['V' - 'A'];
            if (k) {
                digits[7] += k;
                count['S' - 'A'] -= k;
                count['E' - 'A'] -= k;
                count['V' - 'A'] -= k;
                count['E' - 'A'] -= k;
                count['N' - 'A'] -= k;
                j -= k * 5;
            }

            k = count['S' - 'A'];
            if (k) {
                digits[6] += k;
                count['S' - 'A'] -= k;
                count['I' - 'A'] -= k;
                count['X' - 'A'] -= k;
                j -= k * 3;
            }


            k = count['E' - 'A'];
            if (k) {
                digits[9] += k;
                count['N' - 'A'] -= k;
                count['I' - 'A'] -= k;
                count['N' - 'A'] -= k;
                count['E' - 'A'] -= k;
                j -= k * 4;
            }
        }

        printf("Case #%d: ", ++pp);
        for (i = 0; i < 10; i++) {
            while (digits[i]) {
                printf("%d", i);
                digits[i]--;
            }
        }
        puts("");
    }
    return 0;
}
