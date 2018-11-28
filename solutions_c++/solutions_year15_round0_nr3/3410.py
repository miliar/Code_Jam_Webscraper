/**
  First of all, I LOVE GOOGLE JAM, thanks you make us learn a lot.
  This main.cpp is for executing using Qt FrameWork.

  Problem C. Dijkstra

  */

#include <QtCore/qmath.h>
#include <QFile>
#include <QFileInfo>
#include <QDebug>
#include <QApplication>
#include <QApplication>
#include <QTextStream>

QHash<QString, QString> hash;


QString reduceWord(QString word){
    QString aux,newW;
    while(word.size() > 1){
        if(word.size() == 2 && word.at(0) == QString("-")){
//            qDebug() << "We finished and the word is negative";
            return word;
            break;
        }
        aux = word.right(2);
        word.chop(2);
        newW = hash.value(aux);

        word.append(newW.right(1));
        if(newW.size() == 2){//Has a - sign
            if(word.at(0) == QString("-")){
                word = word.mid(1);
            }else{
                word.prepend("-");
            }
        }
    }
    return word;
}

bool calculateIsPossible(int X, QString word){
    QString phrase;

    //Generate the whole pharese
    while(X > 0){
        phrase.append(word);
        X--;
    }

    if(phrase.size()<3){
//        qDebug() << "We dont even have three items ";
        return false;
    }

    bool isNegative = false;
    QString aux,newW;

    //Better strategy: Calculate, and change the value of phrase.
    while(phrase.size()>1){
//        qDebug() << phrase;
        if(!isNegative && phrase.at(0) == QString("i")){
            qDebug() << "We found an i so please Stop!!!";
            break;
        }
        aux = phrase.left(2);
        phrase.remove(0,2);
        newW = hash.value(aux);

        phrase.prepend(newW.right(1));

        if(newW.size() == 2){ //Has a - sign
            isNegative != isNegative;
        }
    }

    isNegative = false;


    while(phrase.size()>1){
//        qDebug() << phrase;
        if(!isNegative && phrase.at(phrase.size()-1) == QString("k")){
            qDebug() << "We have an k so please Stop!!! AMAZING WE WON!!!";
//            break;
            return true;
        }

        aux = phrase.right(2);
        phrase.chop(2);
        newW = hash.value(aux);
        phrase.append(newW.right(1));

        if(newW.size() == 2){ //Has a - sign
            isNegative != isNegative;
        }
    }
    return false;
}


int main(int argc, char *argv[])
{

    qDebug() << "Starting Problem A. Standing Ovation";

    QFile reading("/Users/davidsanchezplaza/Downloads/C-small-attempt0.in-2.txt");
//    QFile reading("/Users/davidsanchezplaza/Downloads/Solve-A.txt");
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
    QStringList lista;

    hash.insert("11", "1");
    hash.insert("1i", "i");
    hash.insert("1j", "j");
    hash.insert("1k", "k");

    hash.insert("i1", "i");
    hash.insert("ii", "-1");
    hash.insert("ij", "k");
    hash.insert("ik", "-j");

    hash.insert("j1", "j");
    hash.insert("ji", "-k");
    hash.insert("jj", "-1");
    hash.insert("jk", "i");

    hash.insert("k1", "k");
    hash.insert("ki", "j");
    hash.insert("kj", "-i");
    hash.insert("kk", "-1");

    //Read T cases
    int T = line.toInt();
    qDebug() << "We have T cases " << T;

    int L, X;

    for(int i = 0; i < T; i++){

        lista = in.readLine().split(" ");

        L = lista.at(0).toInt();
        X = lista.at(1).toInt();
        line = in.readLine();
        QString word;

        qDebug() << "We have T cases L " << L;
        qDebug() << "We have T cases X " << X;
        qDebug() << "We have T cases line " << line;
        int X_aux = X;

        //We can notice that if we want to have the three i, j, k; we need at least to have two of them, since
        //the other one can be generated: eg.  ijjiii would be a valid secuence
        bool contains_i = line.contains("i");
        bool contains_j = line.contains("j");
        bool contains_k = line.contains("k");

        if(!(contains_i && contains_j || contains_i && contains_k || contains_j && contains_k)){
            qDebug() << "Special case where the word can not generate by itself the three requirements: i,j,k";
            QString solution = "Case #" + QString::number((i+1)) + ": NO";
        }

        //Reduce the word
        word = reduceWord(line);

        //We need to repeat multiply the word for himself X times
        X_aux = X;

        QString aux_multiplication = word;
        while(X_aux > 1){ // Bigger than 1 because finalWord already has the word itself :D.
            word.append(aux_multiplication);
            X_aux--;
        }


        if(word.count("-")%2 == 0){
            word.replace("-","");
        }else{
            word.replace("-","");
            word.prepend("-");
        }

        QString finalResultPhrase = reduceWord(word);
        QString solution;

        if(finalResultPhrase == "-1"){
            qDebug() << "The result of the whole string is  " << finalResultPhrase << " and can be possible to form, so start analysing here";

            if(calculateIsPossible(X, line)){
                solution = "Case #" + QString::number((i+1)) + ": YES";
            }else{
                solution = "Case #" + QString::number((i+1)) + ": NO";
            }
        }else{
            qDebug() << "The result of the whole string is " << finalResultPhrase << " and its impossible to form. For sure solution is NO.";
            solution = "Case #" + QString::number((i+1)) + ": NO";
        }

        qDebug() << "Case # " << i;
        qDebug() << "Case solution " << solution;
        qDebug() << " =================================";
        out << solution << endl;
    }

    //Closing the files.
    reading.close();
    destiny.close();

    qDebug() << "DONE, dont forget to submit your code and solution :D";
}

