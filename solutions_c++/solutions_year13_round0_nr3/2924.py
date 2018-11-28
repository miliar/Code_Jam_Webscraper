/*
 * (C) Copyright Martin Juhlin, 2013
 * martin.juhlin@gmal.com
 */

#include <textio.h>
#include <QMap>
#include <math.h>

int testCase(TextInput* ti);
bool testIfPalindromes(qint64 number);

int main(int argc, char ** argv)
{
    TextInput * ti = TextInput::setupOrExit(argc, argv);
    TextOutput to;
    int cases = ti->readNumber();
    for (int c = 0; c < cases; c++) {
        int res = testCase(ti);
        to.out(res);
        to.endl();
    }
    
    delete ti;
    return 0;
}

int testCase(TextInput* ti)
{
    // QByteArray dim = ti->readline();
    QList<qint64> dim = ti->readVector();
    qint64 A = dim.at(0);
    qint64 B = dim.at(1);

    double halfD = floor(sqrt(A)) - 1;
    double endD = floor(sqrt(B)) + 1;
    
    // qDebug("a=%lld b=%lld", A, B);
    // qDebug("halfD = %f endD=%f", halfD, endD);
    
    qint64 end = endD;
    
    int count = 0;
    for (qint64 square = halfD; square < end; square++) {
        if (testIfPalindromes(square)) {
            qint64 normal = square * square;
            if (normal >= A && normal <= B) {
                if (testIfPalindromes(normal)) {
                    count++;
                    // qDebug("found %lld", normal);
                }
            }
        }
    }
    return count;
}


bool testIfPalindromes(qint64 number)
{
    QByteArray val = QByteArray::number(number);
    
    for (int i = 0; i < val.size() / 2; i++) {
        char a = val.at(i);
        char b = val.at(val.size() - i - 1);
        if (a != b)
            return false;
        //qDebug("IF: a=%c b=%c : %s", a, b, val.data());
    }
    return true;
}








