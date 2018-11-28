/**
  First of all, I LOVE GOOGLE JAM, thanks you make us learn a lot.
  This main.cpp is for executing using Qt FrameWork.

  Round 1C.

  Problem A.

  */

#include <QFile>
#include <QFileInfo>
#include <QDebug>
#include <math.h>
#include <QApplication>
#include <QApplication>
#include <QTextStream>



int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem 1";

    QFile reading("/Users/davidsanchezplaza/Downloads/A-large (1).in");
//    QFile file("/Users/davidsanchezplaza/Downloads/A-large-practice-1.in.text");

    QFile destiny("/Users/davidsanchezplaza/Downloads/solution.txt");

    //Making sure we can open the files!
    if (!reading.open(QIODevice::ReadOnly | QIODevice::Text)){
        qDebug() << "Can not open reading file";
    }
    if (!destiny.open(QIODevice::WriteOnly | QIODevice::Text)){
        qDebug() << "Can not open destiny file";
    }

    QTextStream in(&reading);
    QTextStream out(&destiny);

    QString line = in.readLine();

    //Read T cases
    int T = line.toInt();
    qDebug() << "We have T cases " << T;

    for(int z = 0; z < T; z++){
        //Each case line:

        qDebug() << "=============";

        long long startNumber = in.readLine().toLongLong();
        qDebug() << "startNumber" << startNumber;

        if(startNumber == 0){
            QString solution ("Case #" + QString::number((z+1)) + ": INSOMNIA");
            qDebug() << solution;
            out << solution << endl;
            continue;
        }


        QStringList missingDigits;

        for(int i =0; i < 10; i++){
            missingDigits.append(QString::number(i));
        }

        qDebug() << "missingDigits" << missingDigits;


        int safeGuard = 1e6;
        long long currentNumber = startNumber;

        while(safeGuard > 0){

            QString currentNumberString = QString::number(currentNumber);

            QStringList currentNumberDigits = currentNumberString.split("", QString::SkipEmptyParts);

            currentNumberDigits.removeDuplicates();

            for(int i=0; i < currentNumberDigits.size(); i++){
                missingDigits.removeAll(currentNumberDigits.at(i));
            }

            if(missingDigits.size() == 0){
                //We are done!!!!
                qDebug() << currentNumber;
                break;
            }
            safeGuard --;

            if(safeGuard <= 0){
                qDebug() << "BULSHIT";
            }

            currentNumber += startNumber;
        }

        QString solution ("Case #" + QString::number((z+1)) + ": " + QString::number(currentNumber));
        qDebug() << solution;
        out << solution << endl;

    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
