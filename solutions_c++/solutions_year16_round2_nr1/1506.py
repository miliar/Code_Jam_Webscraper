# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);
    char st[2009], numbers[10][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int cases, caseno=0, occur[26], digit[10];
    scanf("%d", &cases);
    while(cases--){
        scanf("%s", st);
        memset(occur, 0, sizeof(occur));
        memset(digit, 0, sizeof(digit));
        for (int i=0; st[i]; i++) occur[st[i]-'A']++;
        if (occur['Z'-'A']){
            digit[0] = occur['Z'-'A'];
            occur['E'-'A'] -= occur['Z'-'A'];
            occur['R'-'A'] -= occur['Z'-'A'];
            occur['O'-'A'] -= occur['Z'-'A'];
            occur['Z'-'A'] = 0;
        }
        if (occur['X'-'A']){
            digit[6] = occur['X'-'A'];
            occur['I'-'A'] -= occur['X'-'A'];
            occur['S'-'A'] -= occur['X'-'A'];
            occur['X'-'A'] = 0;
        }
        if (occur['W'-'A']){
            digit[2] = occur['W'-'A'];
            occur['T'-'A'] -= occur['W'-'A'];
            occur['O'-'A'] -= occur['W'-'A'];
            occur['W'-'A'] = 0;
        }
        if (occur['U'-'A']){
            digit[4] = occur['U'-'A'];
            occur['F'-'A'] -= occur['U'-'A'];
            occur['O'-'A'] -= occur['U'-'A'];
            occur['R'-'A'] -= occur['U'-'A'];
            occur['U'-'A'] = 0;
        }
        if (occur['G'-'A']){
            digit[8] = occur['G'-'A'];
            occur['E'-'A'] -= occur['G'-'A'];
            occur['I'-'A'] -= occur['G'-'A'];
            occur['T'-'A'] -= occur['G'-'A'];
            occur['H'-'A'] -= occur['G'-'A'];
            occur['G'-'A'] = 0;
        }
        if (occur['S'-'A']){
            digit[7] = occur['S'-'A'];
            occur['E'-'A'] -= occur['S'-'A'];
            occur['V'-'A'] -= occur['S'-'A'];
            occur['E'-'A'] -= occur['S'-'A'];
            occur['N'-'A'] -= occur['S'-'A'];
            occur['S'-'A'] = 0;
        }
        if (occur['F'-'A']){
            digit[5] = occur['F'-'A'];
            occur['I'-'A'] -= occur['F'-'A'];
            occur['V'-'A'] -= occur['F'-'A'];
            occur['E'-'A'] -= occur['F'-'A'];
            occur['F'-'A'] = 0;
        }
        if (occur['H'-'A']){
            digit[3] = occur['H'-'A'];
            occur['T'-'A'] -= occur['H'-'A'];
            occur['R'-'A'] -= occur['H'-'A'];
            occur['E'-'A'] -= occur['H'-'A'];
            occur['E'-'A'] -= occur['H'-'A'];
            occur['H'-'A'] = 0;
        }
        if (occur['O'-'A']){
            digit[1] = occur['O'-'A'];
            occur['N'-'A'] -= occur['O'-'A'];
            occur['E'-'A'] -= occur['O'-'A'];
            occur['O'-'A'] = 0;
        }
        if (occur['I'-'A']){
            digit[9] = occur['I'-'A'];
            occur['N'-'A'] -= 2*occur['I'-'A'];
            occur['E'-'A'] -= occur['I'-'A'];
            occur['I'-'A'] = 0;
        }
        for (int i=0; i<26; i++){
            if (occur[i]){
                printf("%c error\n", i+'A');
                break;
            }
        }
        printf("Case #%d: ", ++caseno);
        for (int i=0; i<10; i++){
            while(digit[i]--) printf("%d", i);
        }
        putchar('\n');
    }
    return 0;
}
