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

        int T;

        QString Res;


        in >> T;

//T=1;

        int max;max=0;
        for(int i=1;i<=T;i++)
        {
            qDebug()<<i;
           int N,M;

           in >> N;
           in >> M;


           int a[N][M];
           bool b[N][M];



           for(int j=0;j<N;j++)
           {

               for(int k=0;k<M;k++)
               {
                   b[j][k]=false;
               }

           }



           for(int j=0;j<N;j++)
           {

               for(int k=0;k<M;k++)
               {
                   in>>a[j][k];
               }

           }

//           for(int j=1;j<=3;j++)
//           {

//               for(int k=1;k<=M;k++)
//               {
//                   qDebug() << a[j][k] << " ";
//               }
//               qDebug() <<"\r\n";
//           }


           max=0;

           for(int j=0;j<N;j++)
           {
               //find maximums in the line
               for(int k=0;k<M;k++)
               {

                   if (a[j][k]>max)max=a[j][k];

               }

               //check maximums
               for(int k=0;k<M;k++)
               {

                   if (a[j][k] == max) b[j][k] = true;

               }

               max=0;

           }


           max=0;

           for(int k=0;k<M;k++)
           {
               //find maximums in the line
               for(int j=0;j<N;j++)
               {

                   if (a[j][k]>max)max=a[j][k];

               }

               //check maximums
               for(int j=0;j<N;j++)
               {

                   if (a[j][k] == max) b[j][k] = true;

               }

               max=0;

           }

           Res = "YES";
           for(int j=0;j<N;j++)
           {
               //find maximums in the line
               for(int k=0;k<M;k++)
               {

                   if (b[j][k]==false)Res = "NO";

               }


           }





            out << "Case #" << i << ": " << Res << "\r\n";

        }


        file1.close();
        file2.close();
        //           goto end_loop;
        //           end_loop: ;



    return a.exec();
}
