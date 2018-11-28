#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define NC 16

void processCase(int n) 
{
    int A1, A2;
    int selected[NC];
    memset(selected, 0, sizeof(int) * NC);
    int pos1[NC], pos2[NC];
    cin >> A1;
    for (int i = 0; i < NC; i++)
        cin >> pos1[i];

    cin >> A2;
    for (int i = 0; i < NC; i++)
        cin >> pos2[i];

    int a1 = A1 - 1;
    int a2 = A2 - 1;
//    printf("First: ");
    for (int i = 0; i < 4;i++)
    {
        int c = pos1[a1 * 4 + i];
//        printf("%d ", c);
        selected[c - 1] = 1;
    }
//    printf("\n");

//    printf("Second: ");
    int C = 0;
    int N = 0;
    for (int i = 0; i < 4;i++)
    {
        int c = pos2[a2 * 4 + i];
        if (selected[c - 1])
        {
            C = c;
            N++;
        }
        if (N > 1)
            break;
        
//        printf("%d ", c);
    }
//    printf("\n");
    printf("Case #%d: ", n);
    if (N == 1)
        printf("%d", C);
    else if (N == 0)
        printf("Volunteer cheated!");
    else 
        printf("Bad magician!");
    printf("\n");
}

            


int main(int argc, char **argv)
{
 
    int N = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        processCase(i + 1);

    return 0;
}