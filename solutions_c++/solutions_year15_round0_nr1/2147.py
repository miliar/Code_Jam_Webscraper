#include <QCoreApplication>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
using namespace std;



void prework() {


}



void work(int order) {

    int  smax;
    cin >>smax;
    string s;
    cin>>s;

    int count = 0;
    int maxreq = 0;
    for (int i=0; i<s.size(); i++) {

        int x = i-count;
        if (x>maxreq) maxreq = x;
        count+= s[i]-'0';

    }
    cout<<"Case #"<<order<<": "<<maxreq<<endl;
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
