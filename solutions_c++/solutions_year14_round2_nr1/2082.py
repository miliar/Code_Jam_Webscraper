/*
	Author: Shivang Gupta
	language : C++
	CSE- THE LNMIIT

*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <functional>
#include <bits/stdc++.h>
#include <vector>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#include <bits/stdc++.h>
#include <cassert>
#define PI 3.141
#define ULL unsigned long long
#define mod 1000000007
#define V(x) vector<x>
#define VI vector <int>
#define VII vector < vector <int> >
#define EPS 0.000001
#define ll long long 
using namespace std;

int main()
{
    int t,n;
    int i,j,k;
    scanf("%d", &t);
    for (j = 1 ; j <= t ; j++) {
        scanf("%d", &n);
        char str[150][150];

        for (i = 0 ; i < n ; i++) {
            scanf("%s", &str[i]);
        }

        char str2[150][150];

        for (i = 0 ; i < n ; i++) {
            int z = strlen(str[i]);
            int p = 0;
            for (k = 0 ; k < z ; k++) {
                str2[i][p] = str[i][k];
                while(str[i][k] == str[i][k+1]) {
                    k++;
                }
                p++;
            }
            str2[i][p] = '\0';
        }

        /*for (i = 0 ; i < n ; i++) {
            printf("%s\n", str2[i]);
        }*/


        int flag = 0;
        for (i = 0 ; i < n-1 ; i++) {
            if (strcmp(str2[i],str2[i+1]) != 0) {
                flag = 1;
                break;
            }
        }

        if (flag == 1) {
            printf("Case #%d: Fegla Won\n",j);
            continue;
        }


        int cost_min = 0;
        int len = strlen(str2[0]);
        for (i = 0 ; i < n ; i++) {
            int temp = strlen(str[i]) - len;
            cost_min = cost_min + abs(temp);
        }


        int arr[1000];
        int arr1[1000];
        k = 0;
        for (i = 0; i < strlen(str[0]); i++) {
            arr[k] = 1;
            while (str[0][i] == str[0][i+1]) {
                i++;
                arr[k]++;
            }
            k++;
        }
        k = 0;
        for (i = 0; i < strlen(str[1]); i++) {
            arr1[k] = 1;
            while (str[1][i] == str[1][i+1]) {
                i++;
                arr1[k]++;
            }
            k++;
        }

        int cost = 0;

        for (int m = 0 ; m < k ;m++) {
            //printf("%d ",arr[m]);
            int z = arr[m]-arr1[m];
            cost = cost + abs(z);
        }
        /*printf("\n");
        for (int m = 0 ; m < k ;m++) {
            printf("%d ",arr1[m]);
        }*/

        int mini = cost_min < cost ? cost_min : cost;

        printf("Case #%d: %d\n",j,mini);

    }
    return 0;
}
