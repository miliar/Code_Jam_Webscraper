/*
  Author : Enjoy
  Method : ����ͼƥ��
         dfs(x, c)��xȾɫc������ͼȾɫ��
         find(x, fa)��x��ǰ��Ϊfa��������·��
         f[]Ⱦɫ���飬ne[]����·ǰ�����飬di[],bj[],di[]��ʾ�ߡ�
         n,bs��ʾ���������� 
*/
#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define maxn 500 + 10
#define maxm 2000000 + 10

int a[100000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int ts, ks, n, m, i, j;
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> n >> m;
        for (i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        j = 0;
        for (i = n - 1; i >= j; i--)
            if (a[i] + a[j] <= m) j++;
        printf("Case #%d: %d\n", ks + 1, n - 1 - i);
    }
    return 0;
}
