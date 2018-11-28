#include <cstdio>
#include <string>

using namespace std;

struct Qua
{
	char lettre;
	bool signe;
	Qua(char lettre = '1', bool signe = false) : lettre(lettre), signe(signe) {}
	Qua operator *(const Qua& droite) const
	{
		if(lettre == droite.lettre)
			return Qua('1', (lettre != '1') xor signe xor droite.signe);
		else if(lettre == '1')
			return Qua(droite.lettre, signe xor droite.signe);
		else if(droite.lettre == '1')
			return Qua(lettre, signe xor droite.signe);
		else if(lettre == 'i' && droite.lettre == 'j')
			return Qua('k', signe xor droite.signe);
		else if(lettre == 'i' && droite.lettre == 'k')
			return Qua('j', true xor signe xor droite.signe);
		else if(lettre == 'j' && droite.lettre == 'i')
			return Qua('k', true xor signe xor droite.signe);
		else if(lettre == 'j' && droite.lettre == 'k')
			return Qua('i', signe xor droite.signe);
		else if(lettre == 'k' && droite.lettre == 'i')
			return Qua('j', signe xor droite.signe);
		else
			return Qua('i', true xor signe xor droite.signe);
	}
	bool operator ==(const Qua& droite) const
	{
		return signe == droite.signe && lettre == droite.lettre;
	}
	bool operator !=(const Qua& droite) const
	{
		return !(signe == droite.signe && lettre == droite.lettre);
	}
	void affiche()
	{
		if(signe) printf("-");
		printf("%c\n", lettre);
	}
};

int main()
{
	int nbTests;
	scanf("%d", &nbTests);
	for(int iTest = 1; iTest <= nbTests; ++iTest)
	{
		int l, x;
		scanf("%d%d", &l, &x);
		string s, r;
		char buffer[20*1000];
		scanf(" %s", buffer);
		r = buffer;
		for(int i = 0; i < x; ++i)
			s += r;
		Qua cur[4];// = [Qua('1', false), Qua('1', false), Qua('1', false), Qua('1', false)];
		Qua obj[4];// = [Qua('i', false), Qua('j', false), Qua('k', false), Qua('1', false)];
		obj[0] = Qua('i');
		obj[1] = Qua('j');
		obj[2] = Qua('k');
		int j = 0;
		for(int i = 0; i < 3; ++i)
		{
			while(j < (int)s.size() && cur[i] != obj[i])
			{
				cur[i] = cur[i] * Qua(s[j], false);
				++j;
			}
		}
		while(j < (int)s.size())
		{
			cur[3] = cur[3] * Qua(s[j], false);
			++j;
		}
		printf("Case #%d: %s\n", iTest, (cur[0] == obj[0]
							   && cur[1] == obj[1]
							   && cur[2] == obj[2]
							   && cur[3] == obj[3]) ? "YES" : "NO");
	}
	return 0;
}
