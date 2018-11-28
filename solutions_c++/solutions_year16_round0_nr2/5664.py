/**
  First of all, I LOVE GOOGLE JAM, thanks you make us learn a lot.
  This main.cpp is for executing using Qt FrameWork.

  Round 1C.

  Problem A.

  */

#include <QFile>
#include <QFileInfo>
#include <QDebug>
#include <QApplication>
#include <QApplication>
#include <QTextStream>


void flipAndTurnPankakes(QStringList &enunciado, int index)
{

    Q_ASSERT(index < enunciado.size());

//    qDebug() << "1st enunciado" << enunciado;
//    qDebug() << "index" << index;

    QStringList aux;
    for(int i= index; i >= 0; i--){
        aux.append(enunciado.takeAt(i) == "+"? "-" : "+");
//        qDebug() << "enunciado" << enunciado;
//        qDebug() << "aux" << aux;
    }

//    qDebug() << "aux" << aux;
//    qDebug() << "enunciado" << enunciado;

    aux.append(enunciado);
    enunciado = aux;
//    qDebug() << "enunciado" << enunciado;
}

int turnPankakes(QStringList enunciado, int turn)
{


    //For the groups
    bool isPlus = enunciado.at(0) == "+";
    bool isFirstPlus = isPlus;
    int count = 0;
    QList<int> groups;
    for(int i = 0; i < enunciado.size(); i++){
        if(isPlus) {
            if(enunciado.at(i) != "+"){
                isPlus = false;
                groups.append(count);
                count = 1;
            }else{
                count++;
            }
        }else{
            if(enunciado.at(i) != "-"){
                isPlus = true;
                groups.append(count);
                count = 1;
            }else{
                count++;
            }
        }
    }
    groups.append(count);

    if(groups.size() == 1 && isFirstPlus){
//        qDebug() << "We have finished!!!!!";
        return turn;
    }



    //We search the biggest two possible groups when switching
    int maximum = 0;
    int groupIndex = 1;

    for(int i= 1; i < groups.size(); i +=2){
        if(groups.at(i) > maximum){
            maximum = groups.at(i);
            groupIndex = i;
        }
    }

//    qDebug() << "groupIndex" << groupIndex;
//    qDebug() << "maximum" << maximum;


    int index = -1; //We dont count the last one.
    //Calculate the flip index. We need to pass till the index group.
    for(int i= 0; i < groupIndex; i ++){
        index += groups.at(i);
    }


//    qDebug() << "index" << index;

//    flipAndTurnPankakes(enunciado, enunciado.size()/2);

    flipAndTurnPankakes(enunciado, index);
//    qDebug() << "enunciado" << enunciado;


//    qDebug() << "groups" << groups;
//    qDebug() << "isPlus" << isPlus;
//    qDebug() << "isFirstPlus" << isFirstPlus;

    return turnPankakes(enunciado, ++turn);
}




int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem 1";

    QFile reading("/Users/davidsanchezplaza/Downloads/B-large.in");
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
        QStringList enunciado = in.readLine().split("", QString::SkipEmptyParts);
        qDebug() << "========================";
//        qDebug() << "enunciado" << enunciado;


        int result = turnPankakes(enunciado,0);
        QString solution ("Case #" + QString::number((z+1)) + ": " + QString::number(result));
        qDebug() << "solution" << solution;

        out << solution << endl;
    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
