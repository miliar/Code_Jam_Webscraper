#include <cstdio>
#include <cstring>

bool palindrome[2000];
bool square_palindrome[2000];

int A, B;

int main()
{
    int nprob;

    for (int i = 1; i <= 1000; i++) {
        char n[100]; sprintf(n, "%d", i);
        int len = strlen(n);
        palindrome[i] = true;
        for (int k = 0; k < len; k++)
            if (n[k] != n[len-k-1]) palindrome[i] = false;
    }
    for (int i = 1; i*i <= 1000; i++)
        if (palindrome[i]) square_palindrome[i*i] = true;

    scanf("%d", &nprob);
    for (int prob = 0; prob < nprob; prob++) {
        scanf("%d%d", &A, &B);

        int answer = 0;
        for (int i = A; i <= B; i++)
            if (palindrome[i] && square_palindrome[i]) answer++;
        printf("Case #%d: %d\n", prob+1, answer);
    }

    return 0;
}
