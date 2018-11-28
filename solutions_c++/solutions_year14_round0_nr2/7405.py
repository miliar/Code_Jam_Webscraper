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
using namespace std;
int main()
{
    int i, j, test;
    cin >> test;



    double C, X, F;
    double sum, rate;
    int inf=1;

    for (i = 0; i < test; i++) {
        cin >> C >> F >> X;
        rate = 2.0;
        sum = 0;
        while (inf==1) {

            if (X/rate > ((C/rate)+(X/(rate+F)))) {
                //sumrate
                sum += C/rate;

                rate += F;
            }
            else {
                //suum
                sum+= X/rate;

                break;
            }
        }
        printf("Case #%d: %0.7lf\n", i+1,sum);
    }


    return 0;
}
