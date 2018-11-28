#include <QCoreApplication>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
#include <cassert>
using namespace std;


int qz[10][10];
void prework() {

    qz[1][1] = 1;
    qz[2][1] = 2;
    qz[3][1] = 3;
    qz[4][1] = 4;

    qz[1][2] = 2;
    qz[2][2] = 5;
    qz[3][2] = 8;
    qz[4][2] = 3;

    qz[1][3] = 3;
    qz[2][3] = 4;
    qz[3][3] = 5;
    qz[4][3] = 6;

    qz[1][4] = 4;
    qz[2][4] = 7;
    qz[3][4] = 2;
    qz[4][4] = 5;

    for (int i=1; i<=4; i++) {
        for (int j=1; j<=4; j++) {
            int x = qz[i][j];
            int y;
            if (x>4) y = x-4;
            else y = x+4;

            qz[i+4][j] = y;
            qz[i][j+4] = y;
            qz[i+4][j+4] = x;

        }
    }

}

int pow(int q, int e) {
    int base = q;
    int re = 1;
    while (e>0) {
        if (e%2==1) {
            re = qz[re][base];
        }
        e/=2;
        base = qz[base][base];
    }




    return re;
}
int trans(char c) {
    switch(c) {
    case '1': return 1;
    case 'i': return 2;
    case 'j': return 3;
    case 'k': return 4;
    }
    assert(false);
    return 0;
}

void work(int order) {
    int L,X;
    cin>>L>>X;
    char s[11000];

    cin>>s;
   // qDebug()<<s;
    int leftmin[10];

    int rightmin[10];
    for (int i=0; i<10; i++) {
        leftmin[i] =  999999;
        rightmin[i] = 999999;
    }
    leftmin[1] = 0;
    rightmin[1] = 0;

    int l,r;
    l = 1;
    r = 1;
    for (int i=0; i<L;i++) {
        int x1 = trans(s[i]);
        int x2 = trans(s[L-i-1]);
        l = qz[l][x1];
        r = qz[x2][r];
        if (leftmin[l] > L) leftmin[l] = i+1;
        if (rightmin[r] > L) rightmin[r] = i+1;
    }

    qDebug()<<l <<' '<<r;
    assert(l==r);
    int all = pow(l,X);
    qDebug()<<all;
    if (all!=5) {
        cout<<"Case #"<<order<<": NO"<<endl;
        return;
    }

    int minall[10];
    for (int i=0; i<10; i++) {
        minall[i] = 99999;
    }
    minall[1] = 0;
    int now = 1;
    for (int i=0; i<X; i++) {
        now = qz[now][r];
        if (minall[now]>L) {
            minall[now] = i+1;
        }
        else break;
    }

    int r1,r2;
    int l1,l2;

    l1 = 99999;
    r1 = 99999;

    for (int i=1; i<9; i++) {
        for (int j=1; j<9; j++) {
            if (qz[i][j] == 2) {
                if (minall[i]<l1 && leftmin[j]<=L) {
                    l1 = minall[i];
                    l2 = leftmin[j];
                }

            }
            if (qz[i][j] == 4) {
                if (minall[j]<r1 && rightmin[i] <=L) {
                    r1 = minall[j];
                    r2 = rightmin[i];
                }
            }

        }
    }
    int x =  (l1+r1) * L +l2 + r2;

    if ( x<= X*L) {

        cout<<"Case #"<<order<<": YES"<<endl;
    }
    else {

        cout<<"Case #"<<order<<": NO"<<endl;
    }
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);


     if(freopen("D:\\output.txt", "w", stdout) == NULL)
         fprintf(stderr,"error redirecting stdout\n");
     if(freopen("D:\\input.txt", "r", stdin) == NULL)
         fprintf(stderr,"error redirecting stdin\n");
    int t;
    cin >>t;
    prework();
    for (int i=0; i<t;i++) {
        work(i+1);

    }

return 0;
    return a.exec();
}
