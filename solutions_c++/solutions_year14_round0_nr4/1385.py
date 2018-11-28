#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
double fRand(double fMin, double fMax);
int main()
{
	int cases;
	cin >> cases;
	
	for(int a=1; a<=cases; a++) {
	
		
		int N;
		cin >> N;
		
		double tab1[N], tab2[N];
		
		for(int i=0; i<N; i++) {
			cin >>tab1[i];
		}
		for(int i=0; i<N; i++) {
			cin >>tab2[i];
		}
		
		vector<double> vec1 (tab1, tab1+N);
		vector<double> vec2 (tab2, tab2+N);
		vector<double> vec3 (tab2, tab2+N);
		
		sort(vec1.begin(), vec1.end());
		sort(vec2.begin(), vec2.end());
		sort(vec3.begin(), vec3.end());
		
	//	for(int i=0; i<N; i++) {
	//		cout << tab1[i] << " "; }
		/*
		for (std::vector<double>::iterator it=vec1.begin(); it!=vec1.end(); ++it)
			std::cout << ' ' << *it;
		cout<<endl;
		
		for (std::vector<double>::iterator it=vec2.begin(); it!=vec2.end(); ++it)
			std::cout << ' ' << *it;
		cout<<endl;
		
		cout<<endl;
		*/
		//brutal...
		
		int war = 0, decWar = 0;
		int fromBeg=0, fromEnd= N-1;
		
		
		for(int i=0; i<N; i++) {
			bool win=true, winDec=true;
			for(int j=0; j<N; j++) {
				if(vec1[i] < vec2[j]) {
					vec2[j] = -1.;
					j=N;	//out
					win = false;
				}
			}
			
			if(vec1[i] < vec3[fromBeg]) {
			//	vec3[fromEnd]=-1.;	//not necessary
				fromEnd--;
				winDec=false;
			}
			else {
			//	vec3[fromBeg] = -1.;
				fromBeg++;
			}
			
			if(win == true) {
				war++;
			}
			if(winDec == true) {
				decWar++;
			}
		}
		
		cout<<"Case #" << a << ": " << decWar << " " << war << endl;
	}
	
	return 0;
}
