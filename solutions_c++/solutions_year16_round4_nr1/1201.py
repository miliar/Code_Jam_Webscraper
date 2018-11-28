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

#if 1

void prework() {

} 

QString test(int x, int n) {
	if (n == 0) {
		if (x == 0) return 'R';
		if (x == 1) return 'P';
		if (x == 2) return 'S';
	}
	QString a, b;
	a = test((x + 2) % 3, n - 1);
	b = test(x, n - 1);
	if (a < b) return a + b;
	return b + a;
}
void work(int order) {
	int n, p, s, r;
	cin >> n >> r >>p>> s;
	QVector<int > a(3), b(3), c(3);
	a[0] = 0;
	a[1] = 0;
	a[2] = 1;

	for (int i = 0; i < n; i++) {
		qDebug() << a;
		b[2] = a[0];
		b[1] = a[2];
		b[0] = a[1];
		a[0] += b[0];
		a[1] += b[1];
		a[2] += b[2];
	}
	QString re;
	if (r == a[0] && p == a[1] && s == a[2]) {
		re = test(2, n);
	}
	else if (r == a[1] && p == a[2] && s == a[0]) {
		re = test(1, n);
	}
	else if (r == a[2] && p == a[0] && s == a[1]) {
		re = test(0, n);
	}
	else {
		re = "IMPOSSIBLE";
	}
	cout << re.toUtf8().constData();
}

 


int main(int argc, char *argv[])
{
	 
	QCoreApplication a(argc, argv);

	if (freopen("..\\temp\\output.txt", "w", stdout) == NULL)
		fprintf(stderr, "error redirecting stdout\n");
	if (freopen("..\\temp\\input.txt", "r", stdin) == NULL)
		fprintf(stderr, "error redirecting stdin\n");
	int t;
	cin >> t;
	prework();
	for (int i = 0; i<t; i++) {

		qDebug() << "case " << i + 1 <<endl;
		cout << "Case #" << i + 1 << ": ";

		work(i + 1);
		cout << endl;
	}
	qDebug() << "end!";
	return 0;
	return a.exec();
}

#endif