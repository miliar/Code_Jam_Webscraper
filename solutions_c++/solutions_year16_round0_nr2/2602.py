#include <QCoreApplication>
#include <QString>
#include <QTextStream>
#include <QMap>
#include <QSet>
#include <QList>
#include <QString>

#include <iostream>
#include <string>
#include <QDebug>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
using namespace std;


void prework() {

}



void work(int order) { 
	char  s0[1000];
	cin >> s0;
	QString s(s0); 
	int count = 0;
	char target = '+';
	for (int i = s.size() - 1; i  >=0; i--) {
		if (s[i] == target) {
			continue;
		}
		else {
			count++;
			if (target == '+') {
				target = '-';
			}
			else {
				target = '+';
			}
		}
	}
	cout << count;
}

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	if (freopen("D:\\temp\\output.txt", "w", stdout) == NULL)
		fprintf(stderr, "error redirecting stdout\n");
	if (freopen("D:\\temp\\input.txt", "r", stdin) == NULL)
		fprintf(stderr, "error redirecting stdin\n");
	int t;
	cin >> t;
	prework();
	for (int i = 0; i<t; i++) {

		qDebug() << "case " << i + 1;
		cout << "Case #" << i + 1 << ": ";

		work(i + 1);
		cout << endl;
	}
	qDebug() << "end!";
	return 0;
	return a.exec();
}
