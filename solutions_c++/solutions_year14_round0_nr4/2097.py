#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <list>

#define DELTA (0.0000001)

using namespace std;

int main(){
int iter;
cin >> iter;
int iterr=0;
while(++iterr <= iter){
	int n;
	cin >> n;
	double nao[n];
	double ken[n];
	for(int i=0;i<n;i++)
		cin >> nao[i];
	std::sort(nao,nao + n );

	for(int i=0;i<n;i++)
		cin >> ken[i];
	std::sort(ken,&ken[n]);

/*
	//print sorted
	cout << endl;
	for(int i=0;i<n;i++)
		cout << nao[i] << "\t";
	cout << endl;
	for(int i=0;i<n;i++)
		cout << ken[i] << "\t";
	cout << endl;
*/
	int war=0;int dwar=0;
	{
		//optimal war (naomi is blind)
		list<double> k(ken,ken+n);
		int nstart=0;int nend=n-1;
		for(int i=0;i<n;i++){
			if(nao[nend]>k.back()){
				war++; //naomi gets a point
				nend--;k.pop_front();
			}else{
				auto it = k.begin();
				/*
				while(*it<nao[nstart])
					it++;
				nstart--;
				*/
				while(*it<nao[nend])
					it++;
				nend--;
				k.erase(it); //ken gets a point
			}
		}
	}
	{
		//optimal d war
		list<double> k(ken,ken+n);
		list<double> na(nao,nao+n);
		auto ki = k.begin();
		auto ni = na.begin();
		do{
			while(*ni<*ki){
				ni++;
				if(ni==na.end())
					goto mainloopexit;
			}
			//naomi wins
			dwar++;
			ni++;
			ki++;

mainloopexit:;
		}while(ni!=na.end());
		//ken wins the rest
		/*
		for(int i=0;i<n;i++){
			if(na.back()>k.back()){
				dwar++; //naomi gets a point
				na.pop_back();
				k.pop_front();
			}else{
				k.pop_back(); //ken gets a point but loses the heaviest
				na.pop_front(); //naomi lies and gives the lightest
			}
		}
		*/
	}

	//.precision(14 +(int)log10(t));
	cout << "Case #" << iterr <<": " << dwar << " " << war<< endl;
}
getchar();

return 0;
}
