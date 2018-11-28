#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int T, A, B;
vector<int> fairlist;
vector<int> fairsqlist;

char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

void itoa (int val, char *a)
{
	int i, d;
	d = val;
	i = 0;
	while (d!=0) {
		a[i] = d%10+'0';
		++i;
		d /= 10;
	}
	a[i] = '\0';
	strrev(a);
}


bool checkfair (int val) {
	char valstr[102];
//	itoa(val, valstr);
	sprintf(valstr,"%d",val);
//printf("%s\n",valstr);
	int length = strlen(valstr);
	for (int i = 0; i <= length/2; ++i) {
		if (valstr[i]!=valstr[length-(i+1)]) { return false; }
	}
	return true;
}

int main(void){
	cin >> T;
	for (int i = 1; i <= 1000; ++i) {
		if (checkfair(i)) { fairlist.push_back(i); }
	}
	for (int i = 0; fairlist[i]*fairlist[i] <= 1000; ++i) {
		if (binary_search(fairlist.begin(),fairlist.end(),fairlist[i]*fairlist[i])) {
			fairsqlist.push_back(fairlist[i]*fairlist[i]);
		}
	}
	pair <vector<int>::iterator, vector<int>::iterator> range1,range2;
	for (int i = 1; i <= T; ++i) {
		cin >> A >> B;
		range1 = equal_range(fairsqlist.begin(), fairsqlist.end(), A);
		range2 = equal_range(fairsqlist.begin(), fairsqlist.end(), B);
		cout << "Case #" << i << ": " << (int)distance(range1.first, range2.second) << endl;
	}
	return 0;
}
