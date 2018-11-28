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



int left1[33][11][10000]; 
void work(int order) { 
	int prime[10000];
	prime[0] = 2;
	int count = 1;
	int now = 1;
	while (now < 40000) {
		now += 2;
		bool ok = true;
		for (int i = 0; i < count; i++) {
			if (now % prime[i] == 0)  {
				ok = false;
				break;
			}
			if (prime[i] * prime[i] >= now) break;
		}
		if (!ok) continue;
		prime[count++] = now;
	}
	int test;
	test = 1;

	for (int i = 2; i <= 10; i++) {
			for (int k = 0; k < count; k++) {
				int base = 1;
				for (int j = 0; j < 32; j++) {
					left1[j][i][k] = base;
					base = base * i % prime[k];
				}
			}
	}
	int len = 32;
	int all = 500;
	unsigned int need = (1 << (len-1)) + 1;
	QSet< unsigned int > pool;
	while (pool.size() < all) {
		unsigned int now = rand()  ;
		now |= need;
		if (pool.contains(now)) continue;

		qDebug() << now;
		int re[11];
		bool ok;
		for (int i = 2; i <= 10; i++) {
			 ok = false;
			for (int k = 0; k < count; k++) {
				int yu = 0;
				for (int j = 0; j < len; j++) {
					if ((now & (1 << j)) == 0) continue;
					yu += left1[j][i][k];
				}
				if (yu % prime[k] != 0) continue;
				ok = true;
				re[i] = prime[k];
				break;
			}
			if (!ok) break;
		}

		if (!ok) continue;
		pool.insert(now);
		cout << endl;
		for (int i = len-1; i >= 0; i--) {
			if ((now & (1 << i)) > 0) cout << 1;
			else cout << 0; 
		}
		for (int i = 2; i <= 10; i++) {
			cout << ' ' << re[i];
		}
		qDebug() <<  " ok ";
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
