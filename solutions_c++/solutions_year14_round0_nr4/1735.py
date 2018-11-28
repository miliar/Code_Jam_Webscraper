#include "war.h"

War::War()
{
    qDebug()<< "Constructor";
}

void War::start(){

    QFile inputFile("/home/spheris/Downloads/D-large.in");

    QString filename = "/home/spheris/Downloads/CodeJam/solution.txt";

    QFile file(filename);

    if(file.open(QIODevice::ReadWrite))
    {
        QTextStream stream(&file);

        if(inputFile.open(QIODevice::ReadOnly)){

            QTextStream in(&inputFile);

            int caseNumber = in.readLine().toInt();

            qDebug()<< "caseNumber :" << caseNumber;

            for(int z = 0 ; z< caseNumber ; z++){

                int N = in.readLine().toInt();

                QStringList naomiAuxList =  in.readLine().split(" ");
                QStringList kenAuxList =  in.readLine().split(" ");

                QList<double> naomiList;
                QList<double> kenList;

//                qDebug()<< "naomiAuxList :" << naomiAuxList;
//                qDebug()<< "kenAuxList :" << naomiAuxList;

                for(int x = 0; x < N ; x ++){
                    naomiList.append(naomiAuxList.at(x).toDouble());
//                    qDebug()<< "naomiList :" << naomiList.at(x);
                }
                for(int x = 0; x < N ; x ++){
                    kenList.append(kenAuxList.at(x).toDouble());
//                    qDebug()<< "kenList :" << kenList.at(x);
                }

                //qSort function Sorts the items in range in ascending order using the quicksort algorithm.
                qSort(naomiList.begin(), naomiList.end());
                qSort(kenList.begin(), kenList.end());

                QString solution ("Case #" + QString::number(z+1) + ": " +
                                  QString::number(deceitful(naomiList,kenList)) + " " +
                                  QString::number(war(naomiList,kenList)));

                stream << solution << endl;
            }

        }

    }

    file.close();
    inputFile.close();

}

int War::deceitful(QList<double> naomiList, QList<double> kenList ){

    int winsOfNaomi = 0;
    while(naomiList.size()!=0){
        //With the smallest of naomi we kill the biggest of ken
        if(naomiList.first()< kenList.first()){ //The smallest
            naomiList.removeFirst();
            kenList.removeLast();
            continue;
        }

        if(naomiList.first()>kenList.first()){ //We lie to him saying our brick is heavier than his heaviest brick.
            naomiList.removeFirst();
            kenList.removeFirst();
            winsOfNaomi++;
            continue;
        }
    }
    return winsOfNaomi;
}

int War::war(QList<double> naomiList, QList<double> kenList ){
    int winsOfNaomi = 0;

    double naomiChose = 0;
    while(naomiList.size()!=0){
        //Naomi doesnt know his bricks, so she just pray God to have higher than him. (BASED ON THE FACT THAT SHE DOESNT KNOW HIS BRICKS)
        naomiChose = naomiList.last();
        naomiList.removeLast();

        //What ken does, he always do the same. Tries to beat with his lowest.
        bool canHeBeat= false;
        for(int i = 0; i < kenList.size(); i++){
            if(naomiChose < kenList.at(i)){
                kenList.removeAt(i);
                canHeBeat = true;
                break;
            }
        }
        if(!canHeBeat){
            kenList.removeFirst(); //If he can not beat, removes his lowest brick.
            winsOfNaomi++;
        }
    }
    return winsOfNaomi;
}

double War::solve(int R, int C, int M ){

}

