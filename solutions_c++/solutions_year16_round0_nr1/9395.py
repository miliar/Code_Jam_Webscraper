#include "ProbelmA.h"

ProbelmA::ProbelmA(QString url, QString filein, QString fileout, QObject *parent) :
    QObject(parent)
{
    fileIn = new QFile(url + "/a/" + filein, this);
    fileOut = new QFile(url + "/a/" + fileout, this);
}

QString ProbelmA::CalculateA()
{
    QString retVal;
    if(fileIn->open(QFile::ReadOnly | QFile::Text) && fileOut->open(QFile::WriteOnly | QFile::Text))
    {
        QString firstLine = fileIn->readLine(100);
        bool ok = 0;
        QTextStream outStream(fileOut);

        for(int i = 0; i < firstLine.toInt(&ok, 10); i++)
        {
            if(ok)
            {
                QString actLine = fileIn->readLine(100);
                long num = actLine.toInt(&ok, 10);
                long lastNum;
                if(ok)
                {
                    QString numbers = "";
                    int multiplier = 1;
                    int maxLoopNumber = 100000;

                    while(!(numbers.contains('0') && numbers.contains('1') && numbers.contains('2') && numbers.contains('3') && numbers.contains('4') && numbers.contains('5') && numbers.contains('6') && numbers.contains('7') && numbers.contains('8') && numbers.contains('9')) && (multiplier < maxLoopNumber))
                    {
                        lastNum = multiplier * num;
                        numbers.append(QString::number(lastNum));
                        multiplier++;
                    }
                    if(multiplier < maxLoopNumber)
                    {
                        QString nextLine = "Case #" + QString::number(i+1) + ": " + QString::number(lastNum) + "\n";
                        retVal.append(nextLine);
                        outStream << nextLine;

                    }
                    else
                    {
                        QString nextLine = "Case #" + QString::number(i+1) + ": INSOMNIA\n";
                        retVal.append(nextLine);
                        outStream << nextLine;
                    }
                }
                else
                {
                    retVal = QString::number(i+1) + ". line read error\n";
                }

            }
            else
            {
                retVal = "first line read error\n";
            }
        }
        fileIn->close();
        fileOut->close();
    }
    else
    {
        retVal = "file open error\n" + fileIn->symLinkTarget() + "\n";
    }
    return retVal;
}
