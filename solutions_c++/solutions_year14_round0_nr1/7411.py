#include<iostream>
#include<queue>
#include<stack>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstring>
#define max 99;
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

struct node
{
    int data;
    struct node *left,*right;
};
int main()
{
    int i, j, k;
    int a, b;
    int count;
    int n, m, t;
    int num;
    int matrix1[10][10];
    int matrix2[10][10];
    int arr[25];
    cin >> t;


    FILE *fp = fopen("out.txt", "w");
    for (k = 1; k <= t; k++) {
        cin >> a;
        memset(arr, 0, sizeof(arr));
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                cin >> matrix1[i][j];
                if (i+1 == a) {
                    arr[matrix1[i][j]]++;
                }
            }
        }
        cin >> b;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++) {
                cin >> matrix2[i][j];
                if (i + 1 == b) {
                    arr[matrix2[i][j]]++;
                }
            }
        }
        count = 0;
        for (i = 1; i <= 16; i++) {
            if (arr[i] >= 2) {
                count++;
                num = i;
            }
        }
        if (count == 1) {
            fprintf(fp, "Case #%d: %d\n", k, num);
        }
        else if (count > 1) {
            fprintf(fp, "Case #%d: Bad magician!\n",k, num);
        }
        else {
            fprintf(fp, "Case #%d: Volunteer cheated!\n",k, num);

        }

    }
    fclose(fp);
    return 0;
}
