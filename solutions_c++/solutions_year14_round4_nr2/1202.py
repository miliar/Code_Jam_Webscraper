#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<vector>
using namespace std;
int n;

int work(int b[], int pos, int k){
    int ret = 0;
    if (pos > k){
        for (int i = pos; i > k; --i){
            swap(b[i], b[i - 1]);
            ret++;
        }
    }else{
        for (int i = pos; i < k; ++i){
            swap(b[i], b[i + 1]);
            ret++;
        }
    }
/*
    for (int i = 0; i < n; ++i)
        printf(" %d ", b[i]);
    printf("\n");*/
    for (int i = 0; i < k; ++i)
        for (int j = 0; j < k; ++j)
            if (b[j] > b[j + 1]){
                ret++;
                swap(b[j], b[j + 1]);
            }
    /*
    for (int i = 0; i < n; ++i)
        printf(" %d ", b[i]);
    printf("\n");*/
    for (int i = k; i < n; ++i)
        for (int j = k + 1; j < n - 1; ++j)
            if (b[j] < b[j + 1]){
                ret++;
                swap(b[j], b[j + 1]);
            }
    return ret;
}

int a[1011];
int  main()
{
    freopen("B-small-attempt0(1).in","r",stdin);
    freopen("out1.txt", "w", stdout);
    //freopen("B-small-attempt0(1).in","r",stdin);
    //freopen("in.in","r",stdin);
    //freopen("out.txt", "w", stdout);
    int _;
    cin >> _;
    for (int __ = 1; __ <= _; ++__){
        printf("Case #%d: ", __);
        cin >> n;
        for (int i = 0; i < n; ++i){
            scanf("%d", &a[i]);
        }
        int Ans = (1 << 30);
        int Maxx = -1;
        int p;
        for (int i = 0; i < n; ++i){
            if (a[i] > Maxx){
                Maxx = a[i];
                p = i;
            }
        }
        //cout << p << " " << Maxx << endl;
        int b[1011];
        memcpy(b, a, sizeof(a));
        for (int i = 0; i < n; ++i){
            memcpy(a, b, sizeof(a));
            Ans = min(Ans, work(a, p, i));
           // cout << i << " " << Ans << endl;
        }
        cout << Ans << endl;
    }
    return 0;
}
