#include <QCoreApplication>
#include <QFile>
#include <QStringList>
#include <QTextStream>
#include <QDebug>

bool is_debug = false;

QString getAnswerEx(int P, int Q) {
    int p = P, q = Q, res = 0;
    for(int i = 0; i <= 40; ++i) {
        if (is_debug) {
            qDebug() << "generation " << i << " P: " << p << " Q: " << q;
        }

       if (p == q) {
           return res == 0 ? QString::number(i) : QString::number(res);
       } else if (p > q / 2) {
           if (res == 0) {
               if (is_debug) {
                   qDebug() << "answer there";
               }
               res = i + 1;
           }
           p = 2 * p - q;
           //return QString::number(i + 1);
       } else {
           p *= 2;
       }
    }
    return "impossible";
}

QString getAnswer(QString line) {
    if (is_debug) {
        qDebug() << "start getAnswer " << line;
    }

    QStringList arr = line.split("/");
    return getAnswerEx(arr.at(0).toInt(), arr.at(1).toInt());
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStringList params = QCoreApplication::arguments();
    if (params.count() < 3) {
        return 1;
    }

    QFile file_in(params.at(1)); // this is a name of a file text1.txt sent from main method
    if (!file_in.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return 2;
    }

    QTextStream in(&file_in);

    QFile file_out(params.at(2));
    if (!file_out.open(QIODevice::WriteOnly)) {
        return 3;
    }

    is_debug = params.count() > 3 && params.at(3).compare("debug") == 0;

    QTextStream out(&file_out);
    QString line;
    int Idx = -1;
    int CaseNum = 0;
    int LineNumber = 0;

    while (!in.atEnd()) {
        line = in.readLine();
        if (++Idx == 0 && is_debug) {
            qDebug() << "Input case count " << line;
            continue;
        }
        if (is_debug) {
            qDebug() << "Current index " << Idx;
        }
        if (is_debug) {
            qDebug() << "Line number " << LineNumber;
        }

        if (true) {
            out << "Case #" << ++CaseNum << ": " << getAnswer(line) ; //<< " - " << line;
            endl(out);
        } else {
            out << line << " ";
        }
     }
    return 0;
    //return a.exec();
}
