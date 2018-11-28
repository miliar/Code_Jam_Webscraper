#include <QVector>
#include <QTextStream>

typedef long long lint;

int solve(QString panList)
{
//    panList.prepend('+');
    panList.append('+');
    int ret = 0;
    for (int i = 0; i < panList.size() - 1; ++i)
    {
        if (panList[i] != panList[i+1])
        {
            ++ret;
        }
    }
    return ret;
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        //int N;
        //ins >> N;
        QString panList = ins.readLine();
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(N) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(panList) << endl;
    }

    return 0;
}
