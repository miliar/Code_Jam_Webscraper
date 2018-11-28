#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int find_edge(string &cake)
{
	int i;
	char base = cake[0];

	for(i=1; i<cake.size(); ++i) {
		if(cake[i] != base)
			return i;
	}
	return i;
}

void toggle(string &cake, int pos)
{
	for(int i=0; i<pos; ++i) {
		if(cake[i] == '+')
			cake[i] = '-';
		else
			cake[i] = '+';
	}
}

int flip(string &cake)
{
	int pos;
	int cnt = 0;
	while(1) {
		pos = find_edge(cake);
		if(pos == cake.size() && cake[0] == '+')
			return cnt;
		toggle(cake, pos);
		cnt++;
	}
	return cnt;
}

int main()
{
	int tcase, n;
	int result;
	string cake;

	cin >> tcase;

	for(int i=1; i<=tcase; ++i) {
		cin >> cake;
		printf("Case #%d: %d\n", i, flip(cake));
	}
	return 0;

}
