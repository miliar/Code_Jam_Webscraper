#include <QCoreApplication>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
using namespace std;


void prework() {

}


int z[200][200];

int x[200][200];

void work(int order) {
    int R,C;
    cin>>R>>C;

    memset(z,0,sizeof(z));

    memset(x,0,sizeof(z));

    for (int i=1;i<=R; i++) {
        for (int j=1; j<=C; j++) {
            char c;
            cin>>c;
            switch (c) {
            case '.':
                z[i][j] = 5;
                break;
            case '<':
                z[i][j] = 1;
                break;
            case 'v':
                z[i][j] = 2;
                break;
            case '>':
                z[i][j] = 3;
                break;
            case '^':
                z[i][j] = 4;
                break;
            }
        }
    }

    int result = 0;

    for (int i=1;i<=R; i++) {
        int count= 0;
        int first,last;
        first = -1;
        for (int j=1; j<=C; j++) {
            if (z[i][j] !=5) {
                if (first<0) first = j;
                last = j;
                count++;
            }
        }
        if (count==1) {
            if (z [i][first]  == 1 || z [i][first]  ==3) result++;
            x[i][first]  ++;

            continue;
        }

        if (count==0) continue;
        if (z[i][first] ==1) result++;

        if (z[i][last] ==3) result++;

    }


    for (int j=1; j<=C; j++) {
        int count= 0;
        int first,last;
        first = -1;

        for (int i=1;i<=R; i++) {
            if (z[i][j] !=5) {
                if (first<0) first = i;
                last = i;
                count++;
            }
        }
        if (count==1) {
            if (z [first][j] == 2 || z [first][j] ==4) result++;
            x[first][j] ++;

            continue;
        }

        if (count==0) continue;
        if (z [first][j] ==4) result++;

        if (z [last][j] ==2) result++;

    }

    for (int i=1;i<=R; i++) {
        for (int j=1; j<=C; j++) {
            if (x[i][j]>=2) {
                cout<<"IMPOSSIBLE";
                return;
            }
        }
    }


    cout<<result;
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

return 0;
    return a.exec();
}
