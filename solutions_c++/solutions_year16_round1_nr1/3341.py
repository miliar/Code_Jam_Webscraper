#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef struct node {
    char c;
    struct node *next;
} NODE;

int main(void) {
    char S[1001];
    NODE *n=NULL;
    NODE *p, *first, *last;
    int T;
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf("%s", S);
        n = (NODE*) malloc(sizeof(NODE));
        n->c = S[0];
        n->next = NULL;
        first = last = n;
        for (int j=1; S[j] != '\0'; j++) {
            p = (NODE*) malloc(sizeof(NODE));
            p->c = S[j];
            if (p->c >= first->c) {
                p->next = first;
                first = p;
            }
            else {
                last->next = p;
                p->next = NULL;
                last = p;
            }
        }
        printf ("Case #%d: ", i);
        for (p=first; p!=NULL;) {
            putchar(p->c);
            n = p;
            p = p->next;
            free(n);
        }
        putchar('\n');
    }
    return 0;
}
