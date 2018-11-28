#include <fstream>
using namespace std;

enum Data
{
	plusone, i, j, k, minusi, minusj, minusk, minusone
};

Data matrix[8][8] =  {
	{ plusone, i, j, k, minusi, minusj, minusk, minusone }, // 1 *
	{ i, minusone, k, minusj, plusone, minusk, j, minusi }, // i *
	{ j, minusk, minusone, i, k, plusone, minusi, minusj }, // j * 
	{ k, j, minusi, minusone, minusj, i, plusone, minusk }, // k *
	{ minusi, plusone, minusk, j, minusone, k, minusj, i }, // -i *
	{ minusj, k, plusone, minusi, minusk, minusone, i, j }, // -j *
	{ minusk, minusj, i, plusone, j, minusi, minusone, k }, // -k *
	{ minusone, minusi, minusj, minusk, i, j, k, plusone } // -1 *
};

Data compute(Data current, char multiplier)
{
	Data mult;
	if (multiplier == 'i')
		mult = i;
	if (multiplier == 'j')
		mult = j;
	if (multiplier == 'k')
		mult = k;

	return matrix[current][mult];
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	char str[10000];

	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		bool result = false;
		int L, X;
		fin >> L >> X;
		
		fin >> str;
		int length = L*X;
		char *line = new char[length+1];
		for (int i = 0; i < length; i++)
			line[i] = str[i%L];
		line[length] = 0;

		Data iresult = plusone;
		for (int i = 0; i < length - 2; i++)
		{
			iresult = compute(iresult, line[i]);

			if (iresult == Data::i)
			{
				Data jresult = plusone;
				for (int j = i + 1; j < length - 1; j++)
				{
					jresult = compute(jresult, line[j]);

					if (jresult == Data::j)
					{
						Data kresult = plusone;
						for (int k = j + 1; k < length; k++)
						{

							kresult = compute(kresult, line[k]);
						}
						if (kresult == Data::k)
						{
							result = true;
							goto exit;
						}
					}
				}
			}
		}

	exit:
		fout << "Case #" << (t + 1) << ": " << (result ? "YES" : "NO") << endl;
	}
}

