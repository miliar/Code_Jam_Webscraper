#include <QtCore/QCoreApplication>
#include <QtDebug>
#include <QString>
#include <QList>
#include <QFile>
#include <QStringList>

// returns false if left has any smaller than right
bool compareLists(QList<double> left, QList<double> right)
{
    Q_ASSERT(left.count() == right.count());

    bool retVal = true;

    for(int i = 0; i < left.count(); i++)
    {
        if (left[i] < right[i])
            return false;
    }

    return true;
}


QList<double> readDoubles(QFile& inputFile)
{
    QString rowOfDoubles = QString(inputFile.readLine());
    QStringList doublesText = rowOfDoubles.split(" ");

    QList<double> retVal;
    foreach(QString singleDoubleNumber, doublesText)
    {
        retVal.append(singleDoubleNumber.toDouble());
    }

    return retVal;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    if (argc != 3)
    {
        qDebug() << "Usage:  ./war in.txt out.txt";
        return 0;
    }

    QFile inputFile(a.arguments().at(1));
    QFile outputFile(a.arguments().at(2));

    inputFile.open(QIODevice::ReadOnly);
    outputFile.open(QIODevice::WriteOnly);

    int totalCases = QString(inputFile.readLine()).toInt();

    for(int caseNum = 1; caseNum <= totalCases; caseNum++)
    {
        int numPieces = QString(inputFile.readLine()).toInt();

        QList<double> naomi = readDoubles(inputFile);
        QList<double> ken = readDoubles(inputFile);

        qSort(naomi.begin(), naomi.end());
        qSort(ken.begin(), ken.end());

        qDebug() << "N" << naomi;
        qDebug() << "K" << ken;

        // Fair play
        QList<double> naomiFair = naomi;
        QList<double> kenFair = ken;

        int naomiFairWins = 0;

        while (!naomiFair.empty())
        {
            double naomiPlay = naomiFair.takeFirst();


            for(int i = 0; i < kenFair.count(); i++)
            {
                if (kenFair[i] > naomiPlay)
                {
                    qDebug() << "Ken won with" <<  kenFair[i] << "against" << naomiPlay;
                    kenFair.removeAt(i);
                    break;
                }
            }

            if (kenFair.count() > naomiFair.count())
            {
                // Ken didn't have a winning card
                qDebug() << "Ken lost with" <<  kenFair[0] << "against" << naomiPlay;
                kenFair.removeFirst();
                naomiFairWins++;
            }

        }

        qDebug() << "NF wins" << naomiFairWins;

        // Deitful

        QList<double> naomiDec = naomi;
        QList<double> kenDec = ken;
        int numDecWins = 0;

        for(int i = 0; i < naomi.count(); i++)
        {
            bool doesNaomiWinAll = compareLists(naomiDec, kenDec);

            if (doesNaomiWinAll)
            {
                numDecWins = naomi.count() - i;
                break;
            }
            else
            {
                naomiDec.removeFirst();
                kenDec.removeLast();
            }
        }

        qDebug() << "Dec wins" << numDecWins;

        QString outputText = QString("Case #%1: %2 %3\n").arg(caseNum).arg(numDecWins).arg(naomiFairWins);
            outputFile.write(outputText.toAscii().data());
            qDebug(outputText.trimmed().toAscii().data());



    }







    inputFile.close();
    outputFile.close();
}
