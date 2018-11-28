#include <QCoreApplication>

#include <QString>
#include <QTextStream>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;


void prework() {

}

qint64 getNumber(){
    string a;
    cin>>a;
    QString s(a.c_str());

    s.remove('.');
    while(s[0] =='0') s = s.mid(1);

    QTextStream ts(&s);
    qint64 n;
    ts>>n;
   // qDebug()<<n;
    return n;
}

void work(int order) {
    int n;
    qint64 V,X, R[200], C[200];
    cin>>n;
    V = getNumber();
    X = getNumber();

    qint64 a,b,c,d,e;

    a = 0;
    b = 0;
    c = 0;
    d = 0;
    for (int i=0; i<n; i++) {
        R[i] = getNumber();
        C[i] = getNumber() - X;
        a += R[i]* C[i];

        if (C[i] ==0) {b+=R[i];}

        if (C[i] >0) {c+=R[i]*C[i];}

        if (C[i] <0) {d+=R[i]*C[i];}

    }
 //   qDebug()<<b;
 //       qDebug()<<c;
 //           qDebug()<<d;
    if (a<0) {
        swap(c,d);
        for (int i=0; i<n; i++) {
            C[i]  *= -1;
        }
    }
    if (b==0 ) {
        if (c==0 || d==0) {
            cout<<"IMPOSSIBLE";
            return;
        }

    }
    for (int i=0; i<n; i++) {
        for (int j=n-1 ; j>0; j--) {
            if (C[j-1]> C[j]) {
                swap(C[j-1], C[j]);
                swap(R[j-1], R[j]);

            }
        }
    }

    double bottomT, topT, mid;
    bottomT = 0;

    topT = 1e20;

    mid = 1;

        double nowV = 0;
        double bire = 0;
        for (int i=0; i<n; i++) {
            qDebug()<<R[i]<<' '<<C[i];
            if (C[i]<=0) {
                bire -= R[i] * C[i];
                nowV += R[i] * mid;
            }
            else {
                if (bire<=0)  break;
                double nb = R[i]* C[i];
                if (bire< nb) nb = bire;
                bire -= nb;
                double  h = nb/(R[i] * C[i]);
                qDebug()<<h;
                nowV += R[i] * h;
            }
        }
    qDebug()<<nowV;
    qDebug()<<V;
    cout<<setprecision(20)<< V / nowV;

}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

     if(freopen("D:\\temp\\output.txt", "w", stdout) == NULL)
         fprintf(stderr,"error redirecting stdout\n");
     if(freopen("D:\\temp\\input.txt", "r", stdin) == NULL)
         fprintf(stderr,"error redirecting stdin\n");
    int t;
    cin >>t;
    prework();
    for (int i=0; i<t;i++) {

        qDebug()<<"case "<<i+1;
        cout<<"Case #"<<i+1<<": ";

        work(i+1);
        cout<<endl;
    }
    qDebug()<<"end!";
return 0;
    return a.exec();
}
