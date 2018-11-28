#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX_LENGTH = 10001;

enum QUATERNION_RESULT
{
	RESULT_ONE = 0,
	RESULT_MINUS_ONE,
	RESULT_I,
	RESULT_MINUS_I,
	RESULT_K,
	RESULT_MINUS_K,
	RESULT_J,
	RESULT_MINUS_J
};

QUATERNION_RESULT QUATERNION_MULTIPLY[][8] =
{
	{RESULT_ONE, RESULT_MINUS_ONE, RESULT_I, RESULT_MINUS_I, RESULT_K, RESULT_MINUS_K, RESULT_J, RESULT_MINUS_J},
	{RESULT_MINUS_ONE, RESULT_ONE, RESULT_MINUS_I, RESULT_I, RESULT_MINUS_K, RESULT_K, RESULT_MINUS_J, RESULT_J},
	{RESULT_I, RESULT_MINUS_I, RESULT_MINUS_ONE, RESULT_ONE, RESULT_MINUS_J, RESULT_J, RESULT_K, RESULT_MINUS_K},
	{RESULT_MINUS_I, RESULT_I, RESULT_ONE, RESULT_MINUS_ONE, RESULT_J, RESULT_MINUS_J, RESULT_MINUS_K, RESULT_K},
	{RESULT_K, RESULT_MINUS_K, RESULT_J, RESULT_MINUS_J, RESULT_MINUS_ONE, RESULT_ONE, RESULT_MINUS_I, RESULT_I},
	{RESULT_MINUS_K, RESULT_K, RESULT_MINUS_J, RESULT_J, RESULT_ONE, RESULT_MINUS_ONE, RESULT_I, RESULT_MINUS_I},
	{RESULT_J, RESULT_MINUS_J, RESULT_MINUS_K, RESULT_K, RESULT_I, RESULT_MINUS_I, RESULT_MINUS_ONE, RESULT_ONE},
	{RESULT_MINUS_J, RESULT_J, RESULT_K, RESULT_MINUS_K, RESULT_MINUS_I, RESULT_I, RESULT_ONE, RESULT_MINUS_ONE}
};

void BUILDIsKs(char* szMisSpell, int nLength, vector<QUATERNION_RESULT>& vecI, vector<int>& vecIIndices, vector<int>::size_type& i, vector<int>& vecK, vector<int>::size_type& k)
{
	QUATERNION_RESULT	eKResult;
	QUATERNION_RESULT	eKIndex;
	QUATERNION_RESULT	eIIndex;
	i = 0;
	k = 0;

	if (szMisSpell[0] == 'i')
	{
		vecI[0] = RESULT_I;
		vecIIndices[i] = 0;
		++i;
	}
	else if (szMisSpell[0] == 'j')
		vecI[0] = RESULT_J;
	else
		vecI[0] = RESULT_K;

	if (szMisSpell[nLength - 1] == 'i')
		eKResult = RESULT_I;
	else if (szMisSpell[nLength - 1] == 'j')
		eKResult = RESULT_J;
	else
	{
		eKResult = RESULT_K;
		vecK[0] = nLength - 1;
		++k;
	}

	for (int j = 1; j < nLength; ++j)
	{
		if (szMisSpell[j] == 'i')
			 eIIndex = RESULT_I;
		else if (szMisSpell[j] == 'j')
			eIIndex = RESULT_J;
		else
			eIIndex = RESULT_K;

		if (szMisSpell[nLength - 1 - j] == 'i')
			eKIndex = RESULT_I;
		else if (szMisSpell[nLength - 1 - j] == 'j')
			eKIndex = RESULT_J;
		else
			eKIndex = RESULT_K;

		vecI[j] = QUATERNION_MULTIPLY[vecI[j - 1]][eIIndex];

		if (vecI[j] == RESULT_I)
		{
			vecIIndices[i] = j;
			++i;
		}

		eKResult = QUATERNION_MULTIPLY[eKIndex][eKResult];

		if (eKResult == RESULT_K)
		{
			vecK[k] = nLength - 1 - j;
			++k;
		}
	}
}

bool CanIJKBuilt(vector<QUATERNION_RESULT>& vecI, vector<int>& vecIIndices, vector<int>::size_type iSize, vector<int>& vecKIndices, vector<int>::size_type kSize)
{
	if (iSize == 0 || kSize == 0)
		return false;

	for (int i = 0; i < iSize; ++i)
	{
		vector<int>::iterator iter = upper_bound(vecKIndices.begin(), vecKIndices.begin() + kSize, vecIIndices[i]);

		if (iter == (vecKIndices.begin() + kSize))
			return false;

		while (iter != (vecKIndices.begin() + kSize))
		{
			if (*iter == 0)
			{
				++iter;
				continue;
			}

			if (*iter > (vecIIndices[i] + 1))
			{
				if (QUATERNION_MULTIPLY[RESULT_I][RESULT_J] == vecI[*iter - 1])
					return true;
			}
			++iter;
		}
	}

	return false;
}

int main()
{
	int							nCases, nIndex = 0;
	ifstream					InFile("C-small-attempt2.in");
	ofstream					OutFile("C-small-attempt2.out", ios_base::ate || ios_base::out);
	char						szMisSpell[MAX_LENGTH];
	char						szMisSpellInput[MAX_LENGTH];
	int							L, X;
	vector<QUATERNION_RESULT>	vecI(MAX_LENGTH, RESULT_I);
	vector<int>					vecIIndices(MAX_LENGTH, 0);
	vector<int>					vecKIndices(MAX_LENGTH, 0);
	vector<int>::size_type		iSize;
	vector<int>::size_type		kSize;
	
	InFile >> nCases;

	if (OutFile.is_open())
	{
		while (nCases--)
		{
			InFile >> L >> X >> szMisSpellInput;

			for (int i = 0; i < X; ++i)
				strcpy(szMisSpell + (i * L), szMisSpellInput);

			BUILDIsKs(szMisSpell, L*X, vecI, vecIIndices, iSize, vecKIndices, kSize);
			reverse(vecKIndices.begin(), vecKIndices.begin() + kSize);

			if (CanIJKBuilt(vecI, vecIIndices, iSize, vecKIndices, kSize))
				OutFile << "Case #" << ++nIndex << ": YES" << endl;
			else
				OutFile << "Case #" << ++nIndex << ": NO" << endl;
		}
	}

	return 0;
}