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

namespace MAIN1 {

void prework() {

} 

QString get1(QString s1) {

	if (s1 == "") return "";
	QString left;
	auto big = max_element(s1.begin(), s1.end());
	QChar w = *big;
	int first = s1.indexOf(w);

	left = s1.left(first);
	s1 = s1.mid(first);

	int c = s1.count(w);
	s1.replace(w, "");

	s1.prepend(get1(left));

	for (int i = 0; i < c; i++) s1.prepend(w);
 
	return s1;
}
void work(int order) { 
	string s;
	cin >> s;
	QString s1(s.c_str());
	 
	cout << get1(s1).toStdString();

}



}


#if 1
int main(int argc, char *argv[])
{

	using namespace MAIN1;
	QCoreApplication a(argc, argv);

	if (freopen("D:\\temp\\output.txt", "w", stdout) == NULL)
		fprintf(stderr, "error redirecting stdout\n");
	if (freopen("D:\\temp\\input.txt", "r", stdin) == NULL)
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