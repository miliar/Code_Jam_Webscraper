#include <iostream>
#include <cstring>
#include <QList>
#include <QString>

using namespace std;

QList<char> vowels = {'a', 'e', 'i', 'o', 'u'};

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for (int caseNumber = 0; caseNumber < N; caseNumber++) {
        string wd;
        int n;
        cin >> wd >> n;

        qint64 leftBound = 0, rightBound = 0, result = 0;
        qint64 len = wd.size();
        for (qint64 i = 0; i < len; i++) {
            leftBound = max(leftBound, i);
            while (leftBound <= len - n) {
                while (leftBound <= len - n && vowels.contains(wd[leftBound]))
                    leftBound++;
                if (leftBound > len - n)
                    break;
                bool ok = true;
                for (qint64 j = max(rightBound, leftBound); j < leftBound + n; j++)
                    if (vowels.contains(wd[j])) {
                        leftBound = j;
                        rightBound = leftBound;
                        ok = false;
                        break;
                    }
                if (ok) {
                    rightBound = leftBound + n;
                    break;
                }
            }

            // cout << i << ":" << leftBound << " " << rightBound << endl;

            if (rightBound - leftBound == n)
                result += len - rightBound + 1;
            else break;
        }

        printf("Case #%d: ", caseNumber + 1);
        cout << result << endl;
    }
}

