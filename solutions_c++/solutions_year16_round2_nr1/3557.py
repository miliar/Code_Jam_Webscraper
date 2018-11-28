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

    QFile reading("/Users/davidsanchezplaza/Downloads/A-small-attempt0 (1).in");
//    QFile reading("/Users/davidsanchezplaza/Downloads/solution.in");
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


//        QStringList bffString = in.readLine().split("", QString::SkipEmptyParts);
//        qDebug() << "bffString" << bffString;

        QList<int> timesOfNumber;

        for(int i = 0; i < 10; ++i){
            timesOfNumber.append(0);
        }

//        qDebug() << "timesOfNumber" << timesOfNumber;


//        qSort(bffString);
//        qDebug() << "bffString" << bffString;

//        qDebug() << "bffString" << bffString.count("Z");
//        timesOfNumber.at(0) =  bffString.count("Z");
//        //For eliminating Zero
//        for(int i = 0; i < timesOfNumber.at(0); ++i){
//            bffString.removeOne("");

//        }


        QString enunciado = in.readLine();

        QHash<QString, int> hash;

        for(int i = 0; i < enunciado.size(); ++i){
            hash[enunciado.at(i)] += 1;
        }

//        qDebug() << "timesOfNumber" << timesOfNumber;
//        qDebug() << "hash" << hash;


        QString sequence = "ZWGHUFXVIO";
        QStringList numbers;

        numbers << "ZERO" << "ONE" << "TWO" << "THREE" << "FOUR" << "FIVE" << "SIX" << "SEVEN" << "EIGHT" << "NINE";
        QString sequence_num = "0283456791";


        for(int i = 0; i < sequence.size(); ++i){

//            qDebug() << "sequence.at(i)" << sequence.at(i);
//            qDebug() << "hash[sequence.at(i)]" << hash[sequence.at(i)];

            int number = QString(sequence_num[i]).toInt();
//            qDebug() << "number" << number;

            timesOfNumber[number] = hash[sequence.at(i)];

            if(timesOfNumber[number] > 0){

                //Delete the characters from the list
                for(int j = 0; j < numbers.at(number).size(); ++j){
//                    qDebug() << "numbers.at(number)" << numbers.at(number);
//                    qDebug() << "numbers.at(number).at(j)" << numbers.at(number).at(j);

                    hash[numbers.at(number).at(j)] -= timesOfNumber[number];
                }
            }


//            qDebug() << "hash" << hash;

        }

        qDebug() << "timesOfNumber" << timesOfNumber;


        QString partialSol = "";

        for(int i = 0; i < timesOfNumber.size(); ++i){
            if(timesOfNumber.at(i) == 0){
                continue;
            }
            for(int j = 0; j < timesOfNumber.at(i); ++j){
                partialSol.append(QString::number(i));
            }
        }

        qDebug() << "========== partialSol" << partialSol;


//        foreach(int i, totalNumbers){
//            partialSol.append(QString::number(i));
//            partialSol.append(" ");
//        }





//        qDebug() << "totalNumbers" << totalNumbers;
//        qSort(totalNumbers);
//        qDebug() << "totalNumbers" << totalNumbers;


//        removeOneOfEachPair(totalNumbers);

//        //Generate string solution;
//        QString partialSol = "";
//        foreach(int i, totalNumbers){
//            partialSol.append(QString::number(i));
//            partialSol.append(" ");
//        }

//        partialSol.chop(1);

//        qDebug() << "partialSol" << partialSol;



////        QList<int> row = in.readLine().split("", QString::SkipEmptyParts);






//        //        QString solution ("Case #" + QString::number((z+1)) + ": " + QString::number(currentNumber));

        QString solution ("Case #" + QString::number((z+1)) + ": " + partialSol);
        qDebug() << solution;
        out << solution << endl;

    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
