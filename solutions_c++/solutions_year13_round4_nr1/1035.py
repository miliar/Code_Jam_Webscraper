#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

void problem2A(istream& in, ostream& out){
	int numCases;
	in >> numCases;

	long mod = 1000002013;

	for(int c = 0; c < numCases; c++){
		long N;
		in >> N;

		map<long, long> routes;

		long* tickets = new long[N];

		for(int i = 0; i < N; i++){
			tickets[i] = 0;
		}

		long properTotal = 0;

		int M;
		in >> M;
		for(int m = 0; m < M; m++){
			long start, end, num;
			in >> start >> end >> num;
			end -= 1;
			start -= 1;
			map<long, long>::iterator i = routes.find(end);
			if(i != routes.end()){
				long newNum = i->second + num;
				routes[end] = newNum;
			} else {
				routes.insert(pair<long, long>(end, num));
			}
			tickets[start] += num;

			long k = end - start;
			properTotal += (k*N - (k*k + k)/2 + k) * num;
			properTotal %= mod;
		}

		long total = 0;

		for(map<long, long>::iterator i = routes.begin(); i != routes.end(); i++){
			long end = i->first;
			long numLeaving = i->second;

			long j = end;
			while(numLeaving > 0){
				int numTickets = (numLeaving > tickets[j] ? tickets[j] : numLeaving);
				if(numTickets > 0){
					long k = end - j;
					tickets[j] -= numTickets;
					numLeaving -= numTickets;
					total += (k*N - (k*k + k)/2 + k) * numTickets;
					total %= mod;
				}
				j--;
			}

		}

		out << "Case #" << (c+1) << ": " << (properTotal - total + mod) % mod << endl;

		delete [] tickets;

	}

}

int main(){
	string input = "round2/A-small-attempt2.in";
	string output = "round2/A-small-attempt2.out";

	ifstream fin;

	fin.open(input.c_str());

	ofstream fout;
	fout.open(output.c_str());

	problem2A(fin, fout);

	fin.close();
	fout.close();
}
