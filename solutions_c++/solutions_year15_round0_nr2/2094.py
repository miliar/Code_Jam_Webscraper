#include <QCoreApplication>

#include <iostream>
#include <QDebug>
#include <cstdio>
using namespace std;

int d;
int z[2000];



void prework() {


}

bool trying(int days) {

    for (int eat = 1; eat <= days; eat++) {
        int count = 0;

        for (int i=0; i<d; i++) {
            int x = z[i];

            int y =  (x-1) / eat ;
            count+=y;
        }
        //qDebug()<<count<<' '<<eat;
        if (count+eat <= days) return true;

    }

    return false;
}

void work(int order) {

    cin >>d;
    for (int i=0; i<d; i++) {
        cin >>z[i];
    }

    int low,top;

    low = 0;
    top = 1000;

    while(low+1<top) {
        int mid = (low+top) /2;

        if (trying(mid)) {
            top = mid;
        }
        else {
            low = mid;
        }

    }

    cout<<"Case #"<<order<<": "<<top<<endl;
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

    for (int i=0; i<t;i++) {
        work(i+1);

    }

return 0;
    return a.exec();
}
