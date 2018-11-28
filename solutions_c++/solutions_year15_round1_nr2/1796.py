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

QString getAnswer(int B, int N, QStringList BT) {
    if (is_debug) {
        qDebug() << "start getAnswer" << B << N << BT;
    }
    if (B == 1) {
        return "1";
    }
    int BN = 0, min_time = 0, max_cost = 0, curr_cost, first_item = BT.at(0).toInt(), item_eq = 0;
    QList<int> queue;
    QList<int> cost;

    for (int i = 0; i < B; ++i) {
        queue.append(0);
        curr_cost = BT.at(i).toInt();
        cost.append(curr_cost);
        if (max_cost < curr_cost) {
            max_cost = curr_cost;
        }
        if (curr_cost == first_item) {
            ++item_eq;
        }
    }

    if (item_eq == B) {
        return QString::number(N % B == 0 ? B : N % B);
    }

    int check, check_res, period;
    for (int i = 1; i <= N; ++i) {
        check = max_cost * i;
        check_res = 0;
        for (int j = 0; j < B; ++j) {
            if (check % cost.at(j) == 0) {
                ++check_res;
            }
        }
        if (check_res == B) {
            period = i;
            break;
        }
    }
    qDebug() << "period" << period;

    int repeat_after = 0, tmp;
    for (int j = 0; j < B; ++j) {
        tmp = max_cost * period / cost.at(j);
        repeat_after += tmp;
        //qDebug() << "t" << tmp << "ra" << repeat_after;
    }
    qDebug() << "repeat_after" << repeat_after;
    int start_from = 0;
    if (period != 1 && N % repeat_after == 0) {
        start_from = repeat_after * (N / repeat_after - 1) + 1;
    } else {
        start_from = N - N % repeat_after + 1;
    }


    qDebug() << "start_from" << start_from;

    if (start_from == 0 || start_from >= N) {
        return "1";
    }

    for (int i = start_from; i <= N; ++i) {
        min_time = queue.at(0);
        for (int j = 1; j < B; ++j) {
            if (queue.at(j) < min_time) {
                min_time = queue.at(j);
            }
        }
        //qDebug() << "i" << i << "min_time" << min_time << queue;

        for (int j = 0; j < B; ++j) {
            if (queue.at(j) == min_time) {
                queue.replace(j, queue.at(j) + cost.at(j));
                BN = j + 1;
                break;
            }
        }
    }

    return QString::number(BN);
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
    QStringList sl;
    QString answer;
    int B, N;

    QDateTime start;
    QDateTime finish;

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
        if (Idx % 2 == 1) {
            B = sl.at(0).toInt();
            N = sl.at(1).toInt();
        } else {
            answer = "Case #" + QString::number(++CaseNum) + ": " + getAnswer(B, N, sl);
            out << answer;
            endl(out);
            if (is_debug) {
                qDebug() << line << answer;
            }
        }
        finish = QDateTime::currentDateTime();
        if (is_debug) {
            //qDebug() << "LineProcessed" << finish.toTime_t() - start.toTime_t();
        }

    }
    return 0;
    //return a.exec();
}
