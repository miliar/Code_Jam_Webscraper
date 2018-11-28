#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <string>
//#include <cstdio>
using namespace std;



int main()
{
	
	//freopen("in.in","r",stdin);
	//freopen("Codejam 0.4Large.out","w",stdout);

	int T,N;
	cin>>T;


	for(int i=0; i<T; i++)
	{
	cin>>N;
	vector <double> naomi(N);
	vector <double> ken(N);


	for(int i=0; i<N; i++) cin>>naomi[i];
	for(int i=0; i<N; i++) cin>>ken[i];

	sort(naomi.begin(),naomi.end());
	sort(ken.begin(),ken.end());

	int count1 = 0;
	int n = 0, k=0;

	for(int i=0; i<N ;i++)
	{
		if(naomi[i]>ken[k]) {k++; count1++;}
	}

	int count2 = 0;
	n=0,k=0;
	while(k<N)
	{
		if(ken[k]>naomi[n]) {count2++; n++; k++;}
		else k++;
	}

	cout<<"Case #"<<i+1<<": "<<count1<<" "<<N-count2<<endl;


	}


	return 0;
}

