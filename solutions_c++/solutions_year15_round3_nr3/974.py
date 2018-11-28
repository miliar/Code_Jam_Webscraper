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


void generateCombinations(QList<int> totalCoins, QList<int> &target_value){
    qDebug()<< "Hola";
    QList<int> aux;
    for(int i = totalCoins.size()-1; i >= 0; i --){
        qDebug()<< "totalCoins.at(i) " << totalCoins.at(i);
        target_value.removeAll(totalCoins.at(i));
        aux = totalCoins;
        aux.removeAt(i);
        generateCombinations(aux, target_value);
    }
}


int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem 1";

    QFile reading("/Users/davidsanchezplaza/Downloads/C-small-attempt0.in");

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
    QStringList values_list, coins_list;

    int C, D, V;

    QList<int> totalCoins;
    QList<int> aux_target_value;
    QList<int> target_value;

    for(int i = 0; i < 100 ; i ++){
        aux_target_value.append(i+1);
    }


//    qDebug() << aux_target_value;

    for(int z = 0; z < T; z++){
        //Each case line:

        qDebug() << "START +++++++++++++++++++++" << z + 1;

        totalCoins.clear();

        values_list = in.readLine().split(" ");

        C = values_list.at(0).toInt();
        D = values_list.at(1).toInt();
        V = values_list.at(2).toInt();

        coins_list = in.readLine().split(" ");

//        qDebug() << "values list " << values_list;
//        qDebug() << "coins_list " << coins_list;

        target_value = aux_target_value.mid(0,V);
        qDebug() << target_value;

        foreach(QString s, coins_list){

            for(int i = 0; i< C; i++){
                totalCoins.append(s.toInt());
            }
        }

//        coins_list.append(0);

        int added_num = 0;

        while(target_value.size() > 0){
            QStringList lista;

            for(int i = 0 ; i < pow(2,totalCoins.size()); i ++){
                int number = i;
                QString s = QString::number(number, 2);
                while(s.size() < totalCoins.size()){
                    s.prepend("0");
                }
                lista.append(s);
            }

            foreach(QString s, lista){
                int currentNum= 0;
                for(int i= 0; i< s.size(); i++){
                    if(s.at(i) == '1'){
                        currentNum += totalCoins.at(i);
                    }
                }
                target_value.removeAll(currentNum);
            }


            if(!target_value.isEmpty()){
                for(int a =0; a < C ; a ++){
                    totalCoins.append(target_value.first());
                }
                added_num ++;
            }
        }



        QString solution ("Case #" + QString::number((z+1)) + ": " + QString::number(added_num));
        qDebug() << solution;
        out << solution << endl;
    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
