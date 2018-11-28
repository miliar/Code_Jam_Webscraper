#include <QCoreApplication>
#include <QFile>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QFile filein("A-large.in");
    filein.open(QIODevice::ReadOnly | QIODevice::Text);
    QFile fileout("A-small-practice.out");
    fileout.open(QIODevice::WriteOnly | QIODevice::Text);
    QByteArray Nba = filein.readLine();
    uint T = QString(Nba).toInt();
    qDebug() << T;
    for (int caseId = 0; caseId < T; caseId++)
    {
        QString CaseString = QString(filein.readLine());
        QStringList CaseStringList = CaseString.split(" ");
        qDebug() << "Case" << caseId << "C" << CaseStringList.at(0) << CaseStringList.at(1);
        QString shynesString = CaseStringList.at(1);
        shynesString=shynesString.trimmed();
        QVector<int> shyness;
        for (int i = 0; i<shynesString.size(); i++)
        {
            shyness.append(QString(shynesString.at(i)).toInt());
        }
        bool solved = false;
        int additionalGuests=0;
        int level0Guests = shyness.at(0);
        while (!solved)
        {
            qDebug() << shyness;
            int standing=0;
            int required=0;
            bool acheived=true;
            foreach (int count, shyness) {
                if (required>standing)
                    acheived=false;
                standing+=count;
                required++;
            }
            if (acheived)
                solved=true;
            if (!solved)
                additionalGuests++;
            shyness.pop_front();
            shyness.push_front(level0Guests+additionalGuests);
        }
        qDebug() << additionalGuests;
        fileout.write(QString("Case #").append(QString::number(caseId+1)).append(": ").append(QString::number(additionalGuests)).append("\n").toLocal8Bit());
    }
}

