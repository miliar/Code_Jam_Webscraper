#include <QCoreApplication>
#include <QString>
#include <QTextStream>
#include <QMap>
#include <QSet>
#include <QList>


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
	long long n;
	cin >> n;
	if (n == 0) {

		cout << "INSOMNIA";
		return;
	}
	QSet < int > pool;
	for (int i = 0;  ; i++) {
		long long x;
		x = n * (i+1);
		while (x > 0) {
			int a = x % 10;
			pool.insert(a);
			x /= 10;
		}
		if (pool.size() == 10) {
			cout << n * (i+1);
			return;
		}

	}
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
