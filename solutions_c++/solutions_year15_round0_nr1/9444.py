#include <iostream>
#include <stdio.h>

using namespace std;

int len;
char str[1001];

int process()
{
    int i, persons = 0, extra = 0;
    if (len > 1000) return 0;

    for(i = 0; i <= len; i++) {
        if(persons > len) {
            break;
        }
        if (str[i] == '0') {
            continue;
        }
        if (persons < i) {
            extra += i - persons;
            persons += i - persons;
        }

        persons += str[i] - '0';
    }

    return extra;
}

void input()
{
    scanf("%d", &len);
    scanf("%s", &str);
}

int main()
{
    freopen("q1_ip_level.txt","r",stdin);
    freopen("q1_op_level.txt","w",stdout);

    int Test, Case = 1;
    scanf("%d", &Test);
    while(Test--) {
        input();
        printf("Case #%d: %d\n", Case++, process());
    }

    return 0;
}

