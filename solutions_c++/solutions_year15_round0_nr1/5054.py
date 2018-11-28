/**
  First of all, I LOVE GOOGLE JAM, thanks you make us learn a lot.
  This main.cpp is for executing using Qt FrameWork.

  Problem A. Standing Ovation

  */

#include <QFile>
#include <QFileInfo>
#include <QDebug>
#include <QApplication>
#include <QApplication>
#include <QTextStream>


int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem A. Standing Ovation";

    QFile reading("/Users/davidsanchezplaza/Downloads/A-large.in");
//    QFile file("/Users/davidsanchezplaza/Downloads/A-large-practice-1.in.text");

    QFile destiny("/Users/davidsanchezplaza/Downloads/out.txt");

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
    QStringList enunciado, numPeople;

    int maxShy, addedFriends, clappingPeople;

    for(int i = 0; i < T; i++){
        //Each case line:
        addedFriends = 0;
        clappingPeople = 0;

        line = in.readLine();
        enunciado = line.split(" ");
        maxShy = enunciado.at(0).toInt();
        numPeople = enunciado.at(1).split("",QString::SkipEmptyParts);

        for(int j = 0; j < maxShy; j++){
            clappingPeople += numPeople.at(j).toInt();

            if(clappingPeople < j + 1){
                qDebug() << "missingFriends, WE NEED MORE SUPPORT!, adding one more ";
                addedFriends ++;
                clappingPeople ++;
            }
        }

        QString solution ("Case #" + QString::number((i+1)) + ": " + QString::number(addedFriends));
        out << solution << endl;
    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
