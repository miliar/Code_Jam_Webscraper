#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>

using namespace std;

bool my_greater(const double&, const double&);
int play_war(list<double> &, list<double> &);
int deciet(list<double> &, list<double> &);


int main()
{
	ifstream reader;
	ofstream writer;

	reader.open("input.txt");
	writer.open("output.txt");

	int cases;

	reader >> cases;	
	
	for(int c = 0; c < cases; c++){


		if((c+1)%10 == 0){cout << "Case #" << c+1 << endl;}

		int n;
		double val;
		reader >> n;
	
		list<double> N, K;	
		for(int i = 0; i < n; i++){
			reader >> val; N.push_back(val);
		}
		for(int i = 0; i < n; i++){
			reader >> val; K.push_back(val);
		}

		N.sort(my_greater); K.sort(my_greater);
		list<double>::iterator Khar;
		for(Khar = N.begin(); Khar != N.end(); Khar++)
			cout << (*Khar) << " ";

		writer << "Case #" <<  c+1 << ": " << deciet(N,K) << " " << play_war(N,K) << endl;
	}
}


bool my_greater(const double &d1, const double &d2){
	return d1 > d2;
}

int play_war(list<double> &N, list<double> &K){
	int n_score = 0;
	list<double>::iterator Ni = N.begin();
	list<double>::iterator Ki = K.begin();
	list<double>::iterator end = N.end();

	while(Ni != end) {
		if((*Ki) > (*Ni))
			Ki++;
		else
			n_score++;
		Ni++;
	}

	return n_score;

}

int deciet(list<double> &N, list<double> &K){
	int n_score = 0;
	list<double>::iterator Ni = N.end(); Ni--;
	list<double>::iterator Ki = K.end(); Ki--;
	int moves = 0; 
	int final = N.size();

	while(moves < final){
		cout << "N: " << (*Ni) << "		K: " << (*Ki) << "		" << endl;
		if((*Ni) > (*Ki))
		{Ni--; Ki--; n_score++;}
		else		
		{Ni--;}
		moves ++;
	}

	return n_score;


}
