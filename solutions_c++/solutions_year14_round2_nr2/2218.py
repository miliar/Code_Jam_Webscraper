#include <QtCore>

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QFile infile("input.txt");
	QTextStream ins(&infile);
	QFile outfile("output.txt");
	QTextStream outs(&outfile);
	infile.open(QFile::ReadOnly | QFile::Text);
	outfile.open(QFile::WriteOnly | QFile::Text);
	int t;
	ins >> t;
	for(int i = 1; i <=t; i++)
	{
		int a, b, k;
		ins >> a >> b >> k;
		int count = 0;
		for(int x = 0; x < a; x++)
		{
			for(int y = 0; y < b; y++)
			{
				if((x&y)<k)
				{
					count++;
				}
			}
		}
		outs << "Case #" << i << ": " << count << endl;
	}
	qDebug() << "Finished" << endl;
	return a.exec();
}
