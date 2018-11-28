#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector> 
#include <set> 
#include <math.h> 

using namespace std;
 
int main()
{
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("A-large.out");
	string line;
	int t;
	istringstream stream2;
	getline(infile, line);
	stream2.str(line);
	stream2 >> t;

	for (int i = 0; i < t; i++) {
		int n;
		long a;
		istringstream stream;
		getline(infile, line);
		stream.str(line);
		stream >> a >> n;

		multiset<long> s;
		long new_mote;
		istringstream stream1;
		getline(infile, line);
		stream1.str(line);
		for (int j = 0; j < n; j++) {
			stream1 >> new_mote;
			s.insert(new_mote);
		}

		int result = 0;
		if (a == 1) {
			result = s.size();
		}
		else {
			long a_now = a;
			int index = 0, add[s.size()];
			for (multiset<long>::iterator si = s.begin(); si != s.end(); si++) {
				int k = 0;
				while(1) {
					if (a_now > *si){
						add[index] = k;
						a_now += *si;
						break;
					}
					else {
						a_now = 2 * a_now - 1;
						k++;
					}
				}
				index++;
			}

			int total = 0;
			result = n;
			for (int j = 0; j < n; j++) {
				total += add[j];
				int tmp = total + n - 1 - j;
				if (tmp < result)
					result = tmp;

				/*
				if (total >= j) {
					result += j;
					break;
				}
				else {
					result += add[n - j];
					total -= add[n - j];
				}
				*/
			}
		}

		ostringstream ss;
		ss << "Case #" << (i + 1) << ": " << result << '\n';
		outfile << ss.str(); 
	}

	infile.close();
	outfile.close();
  return 0;
}
