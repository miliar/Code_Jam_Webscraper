// Diva.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <vector>

struct stQuad{
	bool positivie;
	char value;
} qIdentity, qI, qJ, qK;



stQuad multiplyQuad(const stQuad& a, const stQuad& b){
	stQuad result;

	int multiplier = 1;
	switch (a.value)
	{
		case '1':
		{
			result.value = b.value;
		}
		break;
		case 'i':
		{
			switch (b.value){
				case '1': result.value = 'i'; break;
				case 'i': result.value = '1'; multiplier = -1;  break;
				case 'j': result.value = 'k'; break;
				case 'k': result.value = 'j'; multiplier = -1; break;
			}
		}
		break;
	    case 'j':
		{
			switch (b.value){
				case '1': result.value = 'j'; break;
				case 'i': result.value = 'k'; multiplier = -1;  break;
				case 'j': result.value = '1'; multiplier = -1; break;
				case 'k': result.value = 'i'; break;
			}
		}
		break;
		case 'k':
		{
			switch (b.value){
				case '1': result.value = 'k'; break;
				case 'i': result.value = 'j'; break;
				case 'j': result.value = 'i'; multiplier = -1; break;
				case 'k': result.value = '1'; multiplier = -1; break;
			}
		}
		break;

		default:
		{
			printf("ioh oh oh o ho h");
		}
	}

	result.positivie = !(a.positivie ^ b.positivie);
	if (multiplier == -1)
	{
		result.positivie = !result.positivie;
	}

	return result;
}


bool _match(const stQuad& a, const stQuad& b){
	return a.value == b.value && a.positivie == b.positivie;
}

bool match(const std::vector<stQuad>& input, int from, int to, const stQuad& target)
{
	if (from == to){
		return _match(input[from], target);
	}

	stQuad tmp = qIdentity;
	while (from < to)
	{
		tmp = multiplyQuad(tmp, input[from++]);
	}

	return _match(tmp, target);
}

bool solve(int caseNumber){
	qIdentity.value = '1';
	qIdentity.positivie = true;

	qI.value = 'i';
	qI.positivie = true;

	qJ.value = 'j';
	qJ.positivie = true;

	qK.value = 'k';
	qK.positivie = true;

	int L, X; scanf("%d %d", &L, &X);

	std::vector<stQuad> tmp;

	for (auto i = 0; i < L; i++){
		char c;
		scanf("%c", &c);
		if (c == '\n')
		{
			i--;
			continue;
		}

		stQuad q;
		q.value = c;
		q.positivie = true;

		tmp.push_back(q);
	}

	std::vector<stQuad> input;
	for (auto i = 0; i < X; i++){
		for (auto i : tmp){
			input.push_back(i);
		}
	}

	if (L*X < 3)
		return false;

	if (L * X == 3){
		return match(input, 0, 0, qI) &&
			match(input, 1, 1, qJ) &&
			match(input, 2, 2, qK);
	}

	std::vector<int> iMatches;
	std::map<int, int> kMatches;

	stQuad first = qIdentity;
	for (auto i = 0; i < L*X-1; i++){
		first = multiplyQuad(first, input[i]);
		if (_match(first, qI)){
			iMatches.push_back(i+1);
		}
	}

	if (iMatches.size() == 0)
		return false;

	first = qIdentity;
	for (auto i = L*X - 1; i >= 0;  i--){
		first = multiplyQuad(input[i], first);

		if (_match(first, qK)){
			kMatches[i] = i;
		}
	}

	if (kMatches.size() == 0)
		return false;

	for (auto& i : iMatches){
		first = qIdentity;

		for (auto j = i; j < L*X - 1; j++)
		{
			first = multiplyQuad(first, input[j]);
			bool isK = kMatches.find( j + 1) != kMatches.end();

			if (isK && _match(first, qJ)){
				return true;
			}
		}
	}

	return false;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int t; scanf("%d", &t);
	int caseNumber = 1;
	while (t--) {
		printf("Case #%d: %s\n", caseNumber, solve(caseNumber) ? "YES" : "NO");
		caseNumber++;

		fflush(stdout);
	}
	return 0;
}

