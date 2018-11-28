#include <QCoreApplication>
#include <iostream>
#include <QString>
using namespace std;

QList<qint64> fairPals;
bool isPalindrome(qint64 x)
{
    QString s;
    s.setNum(x);
    int n = s.length();
    for (int i = 0; i * 2 < n; i++)
        if (s.at(i) != s.at(n - i - 1))
            return false;
    return true;
}

int main(int argc, char *argv[])
{
    fairPals.clear();
    for (qint64 i = 1; i < 10000000; i++)
        if (isPalindrome(i) && isPalindrome((i * i)))
            fairPals.append(i * i);
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for (int caseNumber = 0; caseNumber < N; caseNumber++) {
        qint64 A, B;
        cin >> A >> B;
        int leftCount = fairPals.length(), rightCount = fairPals.length();
        for (int i = 0; i < fairPals.length(); i++) {
            qint64 value = fairPals.at(i);
            if (leftCount > i && value >= A)
                leftCount = i;
            if (rightCount > i && value > B)
                rightCount = i;
        }
        printf("Case #%d: %d\n", caseNumber + 1, rightCount - leftCount);
    }
}
