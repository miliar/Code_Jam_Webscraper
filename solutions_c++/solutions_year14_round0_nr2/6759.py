#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QStringList>
#include <QTextStream>
#include <QDebug>

void CookieClickerA() {
    QFile inputFile("B-large.in");
    QFile outputFile("B-large.out");
    inputFile.open(QIODevice::ReadOnly);
    outputFile.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream in(&inputFile);
    QTextStream out(&outputFile);
    QStringList lineNumbers;
    double time, curTime, c, f, x, cps;
    int problemCount = in.readLine().toInt();
    for(int i = 1; i <= problemCount; i++) {
        lineNumbers = in.readLine().split(" ");
        c = lineNumbers[0].toDouble();
        f = lineNumbers[1].toDouble();
        x = lineNumbers[2].toDouble();
        cps = 2;
        time = x / cps;
        curTime = 0;
        bool newFarm = true;
        while(newFarm) {
            curTime += c / cps;
            cps += f;
            if((curTime + x / cps) <= time) {
                time = curTime + x / cps;
            } else {
                newFarm = false;
            }
        }
        out << "Case #" << i << ": " << QString::number(time, 'd', 7) << "\n";
    }
    inputFile.close();
    outputFile.close();
}

int main(int argc, char *argv[])
{
    //QCoreApplication a(argc, argv);

    CookieClickerA();

    return 0;
    //return a.exec();
}
