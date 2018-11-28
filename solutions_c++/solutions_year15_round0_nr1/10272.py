#include <QFile>
#include <QDebug>
#include <QDir>
#include <QStringList>
#include <QMultiHash>
#include <QStack>

QMultiHash<int, int> getShynessPersonsMap(QString number) {
    QMultiHash<int, int> shynessPersonsMap;
    for (int i = 0; i < number.count(); ++i) {
        shynessPersonsMap.insert(i, QString(number.at(i)).toInt());
    }
    return shynessPersonsMap;
}

int main()
{
    //QMultiHash<int, int> personsShynessMap = new QMultiHash<int, int>();

    int testsNumber = 0;
    QFile input("A-small-attempt0.in");
    QFile output("output.txt");

    if (input.open(QIODevice::ReadOnly | QIODevice::Text) && output.open(QIODevice::WriteOnly)) {

        testsNumber = input.readLine().trimmed().toInt();
        qDebug() << testsNumber;
        QTextStream stream(&output);
        for (int i = 0; i < testsNumber; ++i) {

            QString testCase = input.readLine().trimmed();
            QMultiHash<int, int> shynessPersonsMap = getShynessPersonsMap(testCase.split(" ").value(1));
            int minPersons2Add = 0;
            int standingPersons = 0;
            int count = 0;
            for (int shyness = 0; shyness <= shynessPersonsMap.keys().count(); ++shyness) {
                count += shynessPersonsMap.value(shyness);
                if ((shynessPersonsMap.value(shyness) != 0) && (standingPersons >= shyness))
                    standingPersons += shynessPersonsMap.value(shyness);

                else if ((shynessPersonsMap.value(shyness) != 0) && (standingPersons < shyness)) {
                    minPersons2Add += shyness - standingPersons;
                    standingPersons += minPersons2Add + shynessPersonsMap.value(shyness);
                }
            }

            stream << "Case #" << i + 1  << ": " << minPersons2Add << endl;
        }
    }

    input.close();
    output.close();

    return 0;
}


