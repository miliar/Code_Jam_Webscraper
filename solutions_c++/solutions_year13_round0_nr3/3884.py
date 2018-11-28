#include <QtCore/QCoreApplication>
#include <QtCore>
#include <QVector>

//#include <QTimer>
#include <iostream>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    float foot = 0;

        std::cout <<  "Plz enter ";
//        std::cin  >> foot;

//        std::cout << "foots = " << foot/ 7.481;


        QFile file1("Input.in");
        QFile file2("Output.txt");
        file2.remove();

        file1.open(QIODevice::ReadOnly);
        file2.open(QIODevice::WriteOnly);

        QTextStream in(&file1);
        QTextStream out(&file2);


        //Generation of base
//        QString line,line2;
//        line2.clear();
//        for(int i=1;i<=10000000;i++)
//        {

//            line = QString::number(i);
//            line2=line;

//            for(int k=0;k<line.length();k++)
//            {
//                line2[k]=line[line.length()-1-k];
//            }
//            if (line == line2)
//            {



//                line = QString::number(i*i);
//                line2=line;
//                for(int z=0;z<line.length();z++)
//                {
//                    line2[z]=line[line.length()-1-z];
//                }
//                if (line == line2)
//                {
//                    out << i*i << " ";
//                }



//            }

//        }



//1 4 9 121 484 10201 12321 14641 40804 44944 1002001 1234321 4008004 100020001 102030201 104060401 121242121 123454321 125686521 400080004 404090404


        int T;

        int Res;


        in >> T;

        const int SIZEF = 5;
        int fairs[SIZEF] = {1, 4, 9, 121, 484};


        for(int i=1;i<=T;i++)
        {
        Res=0;
        int A,B;
        in >> A;
        in >> B;


        for(int j=0;j<=SIZEF-1;j++)
        {
            if ((fairs[j] >= A) && (fairs[j] <= B))Res++;
        }


            out << "Case #" << i << ": " << Res << "\r\n";

        }





        file1.close();
        file2.close();
        //           goto end_loop;
        //           end_loop: ;



    return a.exec();
}
