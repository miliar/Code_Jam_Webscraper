#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QStringList>
#include <QTextStream>
#include <QDebug>

void MagicTrick() {
    QFile inputFile("A-small-attempt0.in");
    QFile outputFile("A-small-attempt0.out");
    inputFile.open(QIODevice::ReadOnly);
    outputFile.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream in(&inputFile);
    QTextStream out(&outputFile);
    QStringList lineNumbers;
    QStringList otherNumbers;
    QString line;
    int solution;
    int chosenRow;
    int problemCount = in.readLine().toInt();
    for(int i = 1; i <= problemCount; i++) {
        chosenRow = in.readLine().toInt();
        for(int j = 1; j < 5; j++) {
            line = in.readLine();
            if(j == chosenRow)
                lineNumbers = line.split(" ");
        }
        chosenRow = in.readLine().toInt();
        for(int j = 1; j < 5; j++) {
            line = in.readLine();
            if(j == chosenRow)
                otherNumbers = line.split(" ");
        }
        solution = 0;
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                if(lineNumbers[j].toInt() == otherNumbers[k].toInt()) {
                    if(solution == -1) break;
                    if(solution != 0) {
                        out << "Case #" << i << ": Bad magician!\n";
                        solution = -1;
                    } else {
                        solution = lineNumbers[j].toInt();
                    }
                }
            }
        }
        if(solution == 0) {
            out << "Case #" << i << ": Volunteer cheated!\n";
        } else {
            if(solution != -1) out << "Case #" << i << ": " << solution << "\n";
        }
    }
    inputFile.close();
    outputFile.close();
}

int main(int argc, char *argv[])
{
    //QCoreApplication a(argc, argv);

    MagicTrick();

    return 0;
    //return a.exec();
}
