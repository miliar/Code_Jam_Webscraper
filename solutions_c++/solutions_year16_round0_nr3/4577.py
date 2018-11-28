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


QList<long long> primes;

long long calculateFirstDivisor(long long target)
{
    qDebug() << "calculateFirstDivisor start() target" << target;

    //We check if module = 0
    for(int i = 0; i < primes.size(); i++){

        //        qDebug() << "YES IS DIVISIBLE";

        if(target < primes.at(i)){
            qDebug() << "Stop searching in number biggers";
            return 0;
        }

//        qDebug() << "target" << target;
//        qDebug() << "primes.at(i)" << primes.at(i);


        if(target % primes.at(i) == 0){
//            qDebug() << "YES IS DIVISIBLE";
            return primes.at(i);
        }
    }

    return 0;
}

int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem 1";

    QFile reading("/Users/davidsanchezplaza/Downloads/C-small-attempt0 (1).in");
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
        QStringList enunciado = in.readLine().split(" ");
        qDebug() << "========================";
        qDebug() << "enunciado" << enunciado;

        int N = enunciado.at(0).toInt();
        int J = enunciado.at(1).toInt();

        qDebug() << "N" << N;
        qDebug() << "J" << J;




        //First we generate the array with a lot of prime numbers, since we only need to check if is divisible by that number.
        //The biggest number we will have is 1111111111111111, so its max prime will be smaller than sqroot(1111111111111111) = 34e6
//        QList<int> primes;

        primes.append(2);
        for (int i = 3; i < 34e1; i += 2){ //We directly dont put the even numbers
            primes.append(i);
        }


        for(int i = 0; i < primes.size(); i++){

            //We eliminate the multiples of each number
            long long number = primes.at(i);
            while(number < primes.at(primes.size()-1)){
                number += primes.at(i);
                primes.removeOne(number);
            }
        }

        qDebug() << primes;




        QStringList totalSolution;

//        long long bigNumber = QString("1000000000000001").toLongLong(0,10);


        int mamadas = 0;


        //Generate all the numbers
        for(long long i = 32769; i < 65536; i+= 2){
//            for(long long i = 32769; i < 39969; i+= 2){

//        QStringList example;
//        example << "100011" << "111111" << "111001";

//        for(long long i = 0; i < 1; i++){
//            QString stringNumber = example.at(i);


            bool success = true;
            QString stringNumber = QString::number(i,2);
            qDebug() << "============";
            qDebug() << "stringNumber:" << stringNumber;

            QString possibleSolution = stringNumber;


            long long number = stringNumber.toLongLong(0,10);
            qDebug() << "Number:" << number;

            for(int j = 2; j <= 10; j++){
                long long numberBase = stringNumber.toLongLong(0,j);
                qDebug() << "numberBase " << numberBase << "    Base: " << j;

                long long resultPartialBase = calculateFirstDivisor(numberBase);

                if(resultPartialBase == 0){
                    qDebug() << "PROBLEMS IS A PRIME, so we ignore";
                    success = false;
                    break;
                }else{
                    possibleSolution.append(QString(" "));
                    possibleSolution.append(QString::number(resultPartialBase));
                }
            }

            if(success)
                totalSolution.append(possibleSolution);

            mamadas ++;

            if(totalSolution.size() >= 50) {
                break;
            }
        }

        qDebug() << "mamadas" << mamadas;
        qDebug() << "totalSolution" << totalSolution.size();
        qDebug() << "totalSolution" << totalSolution;













//        qDebug() << "Done";



////        qDebug() << bigNumber;

////        while(totalSolution.size() < J) {

////            qDebug() << bigNumber;


////            bigNumber +=2;

////        }




////        QString a = "1000000000000001";
//        QString a = "1111111111111111";
////        QString a = "1001";

//        for(int i = 2; i <= 10; i++){
//            qDebug() << a.toLongLong(0,i);

//        }


//        qDebug() << QString::number();






        QString solution ("Case #" + QString::number((z+1)) + ": ");
        qDebug() << "solution" << solution;

        out << solution << endl;

        for(int i = 0; i < totalSolution.size(); i++){
            out << totalSolution.at(i) << endl;

        }
    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}
