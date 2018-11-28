#include <QCoreApplication>
#include <QFile>
#include <QStringList>
#include <QTextStream>
#include <QDebug>
#include <QtGlobal>
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QPair>

bool is_debug = false;

QString getAnswer(int K, int C, int S) {
    if (is_debug) {
        qDebug() << "start getAnswer" << K << C << S;
    }
    if (C == 1 && S < K) {
        return "IMPOSSIBLE";
    }
    if (C > 1 && S < K - 1) {
        return "IMPOSSIBLE";
    }
    if (K == 1) {
        return "1";
    }
    QString res;
    if (C == 1) {
        for (int i = 1; i <= K; ++i) {
            if (!res.isEmpty()) {
                res.append(" ");
            }
            res.append(QString::number(i));
        }
    } else {
        for (int i = 2; i <= K; ++i) {
            if (!res.isEmpty()) {
                res.append(" ");
            }
            res.append(QString::number(i));
        }
    }

    return res;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStringList params = QCoreApplication::arguments();
    if (params.count() < 3) {
        return 1;
    }

    qDebug() << params;
    qDebug() << params.at(1);
    QFile file_in(params.at(1));
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
    QString answer;

    QDateTime start;
    QDateTime finish;
    QStringList sl;

    while (!in.atEnd()) {
        line = in.readLine();
        if (++Idx == 0) {
            if (is_debug) qDebug() << "Input case count " << line;
            continue;
        }
        if (is_debug) {
            //qDebug() << "Current index " << Idx;
        }
        start = QDateTime::currentDateTime();
        sl = line.split(" ");
            answer = "Case #" + QString::number(++CaseNum) + ": " + getAnswer(sl.at(0).toInt(), sl.at(1).toInt(), sl.at(2).toInt());
            out << answer;
            endl(out);
            if (is_debug) {
                qDebug() << line << answer;
            }
        finish = QDateTime::currentDateTime();
        if (is_debug) {
            //qDebug() << "LineProcessed" << finish.toTime_t() - start.toTime_t();
        }

    }//*/
    return 0;
    //return a.exec();
}
