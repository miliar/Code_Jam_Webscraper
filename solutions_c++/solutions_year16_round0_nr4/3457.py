#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

long long int convert(string input, int base) {
	long long int res = 0;
	int n, i;

	n = input.size();
	for (i = 0; i < n; i++) {
		if (input[i] == '1') {
			res = res + pow(base, n - i - 1);
		}
	}
	return res;
}

void next(string &cur) {
	int i;
	
	for (i = cur.size() - 1; i >= 0; i--) {
		if (cur[i] == '0') {
			cur[i] = '1';
			break;
		}
		else {
			cur[i] = '0';
		}
	}
}

long long int div(long long int n) {
	long long int i;

	for (i = 3; i < 1000000; i = i + 2) {
		if (n % i == 0)
			return i;
	}
	return 0;
}

int main() {
	int t, k, c, count, s;

	scanf("%d", &t);
	count = 1;
	while (t--) {
		scanf("%d %d %d", &k, &c, &s);
		cout << "Case #" << count << ": ";
		count++;
		for (int i = 1; i <= s; i++)
			cout << i << " ";
		cout << endl;
	}

	return 0;

	/* Problem C
	int t, c, j, n, i;
	long long int temp;
	string input, aux;

	scanf("%d", &t);
	c = 1;
	while (t--) {
		map<string, vector<long long int> > output;
		
		input = "";
		scanf("%d %d", &n, &j);
		for (i = 2; i < n; i++) {
			input = input + "0";
		}
		aux = "1" + input + "1";
		while (true) {
			output[aux] = vector<long long int>(9, 0);
			for (i = 2; i <= 10; i++) {
				temp = convert(aux, i);
				if (temp % 2 == 0) {
					temp = 2;
				} else {
					temp = div(temp);
				}
				if (temp == 0)
					break;
				else
					output[aux][i - 2] = temp;
			}
			if (i == 11) {
				j--;
			} else {
				output.erase(aux);
			}
			if (j == 0) {
				cout << "Case #" << c << ":" << endl;
				c++;
				for (auto it = output.begin(); it != output.end(); it++) {
					for (i = 0; i < it->first.size(); i++ )
						cout << it->first[i];
					cout << " ";
					for (i = 0; i < 9; i++) {
						cout << it->second[i] << " ";
					}
					cout << endl;
				}
				break;
			}
			next(input);
			aux = "1" + input + "1";
		}
	}
		
	return 0;

	*/

	/* Problem B
	int t, c, n, i, j;
	char input[101];
	string aux;

	scanf("%d", &t);
	c = 1;
	while (t--) {
		scanf("%s", input);
		aux = string(input);
		n = 0;
		while (true) {
			if (aux[0] == '-') {
				i = 0;
				while (aux[i + 1] == '-') 
					i++;
				while (i >= 0) {
					aux[i] = '+';
					i--;
				}
			} else {
				i = 0;
				while (aux[i + 1] == '+')
					i++;
				if (i == aux.size() - 1) {
					cout << "Case #" << c << ": " << n << endl;
					c++;
					break;
				}
				while (i >= 0) {
					aux[i] = '-';
					i--;
				}
			}
			n++;
		}
	}


	return 0;

	*/

	/* Problem A
	int t, n, i, count, p, m, times, aux;
	
	scanf("%d", &t);
	p = 1;
	while (t--) {
		vector<bool> seen(10, false);
		scanf("%d", &n);
		times = 1;
		if (n == 0) {
			cout << "Case #" << p << ": INSOMNIA" << endl;
			p++;
			continue;
		}
		while (true) {
			m = times * n;
			aux = m;
			while (m != 0) {
				seen[m % 10] = true;
				m = m / 10;
			}
			count = 0;
			for (i = 0; i < 10; i++) {
				if (seen[i])
					count++;
			}
			if (count == 10) {
				cout << "Case #" << p << ": " << aux << endl;
				p++;
				break;
			}
			times++;
		}
	}
	return 0;
	*/
}