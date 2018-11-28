//#include <iostream>
//#include <cstring>
//#include <cstdio>
//#include <algorithm>
//#include <string>
//
//using namespace std;
//
//#define MAXN 100005
//char B[MAXN];
//char A[MAXN];
//int num[10];
//int lena, lenb;
//
//void Solve(int n){
//    if(n == 0){
//        printf("INSOMNIA\n");
//        return;
//    }
//    int cnt = 10;
//    memset(num, 0, sizeof(num));
//    sprintf(A, "%d", n);
//    lena = strlen(A);
//    reverse(A, A+lena);
//    memset(B, '0', sizeof(char)*lena);
//    lenb = lena;
//    while(cnt != 0){
//        int pre = 0;
//        for(int i=0; i<lena; i++){
//            int tmp = (A[i] + B[i] + pre - '0'*2);
//            B[i] = tmp%10 + '0';
//            pre = tmp/10;
//            if(num[B[i]-'0'] == 0){
//                num[B[i]-'0'] = 1;
//                cnt--;
//            }
//        }
//        int i = lena;
//        while(pre){
//            if(lenb <= i) B[lenb++] = '0';
//            int tmp = (B[i] + pre - '0');
//            B[i] = tmp%10 + '0';
//            pre = tmp/10;
//            if(num[B[i]-'0'] == 0){
//                num[B[i]-'0'] = 1;
//                cnt--;
//            }
//        }
//    }
//    reverse(B, B+lenb);
//    B[lenb] = ' ';
//    printf("%s\n", B);
//}
//
//int main()
//{
//    freopen("Ain.txt", "r", stdin);
//    freopen("Aout.txt", "w", stdout);
//    int t;
//    int cas = 1;
//    scanf("%d", &t);
//    while(t--){
//        int n;
//        scanf("%d", &n);
//        printf("Case #%d: ", cas++);
//        Solve(n);
//    }
//    return 0;
//}
//
///*
//5
//0
//1
//2
//11
//1692
//*/
#include <iostream>
#include <cstring>

using namespace std;

int ten[10];

void solve(int n){
    if(n == 0){
        printf("INSOMNIA\n");
        return;
    }
    int cnt = 10;
    int sum = 0;
    memset(ten, 0, sizeof(ten));
    while(cnt > 0){
        sum += n;
        int tmp = sum;
        while(tmp){
            if(ten[tmp%10] == 0){
                cnt--;
                ten[tmp%10]++;
            }
            tmp /= 10;
        }
    }
    printf("%d\n", sum);
}


int main()
{
    freopen("Ain1.txt", "r", stdin);
    freopen("Aout2.txt", "w", stdout);
    int t;
    int cas = 1;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", cas++);
        solve(n);
    }
    return 0;
}
