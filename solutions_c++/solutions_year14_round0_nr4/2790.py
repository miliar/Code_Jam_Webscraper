#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int T;

	ifstream fin("D:/D-small-attempt0.in");
	fin>>T;
	for(int t=0;t<T;t++)
	{
		int N;
		fin>>N;
		vector<double> ken(N);
		vector<double> naomi(N);
		for(int i=0;i<N;i++){
			fin>>naomi[i];
		}
		for(int i=0;i<N;i++){
			fin>>ken[i];
		}
		sort(ken.begin(),ken.end());
		sort(naomi.begin(),naomi.end());
		/*for(int i=0;i<ken.size();i++)
			cout<<ken[i]<<" ";
		cout<<endl;
		for(int i=0;i<naomi.size();i++)
			cout<<naomi[i]<<" ";
		cout<<endl;*/
		int head=0;
		int tail=ken.size()-1;
		int win1=0;
		for(int i=0;i<naomi.size();i++){
			if (naomi[i]<ken[head])
				tail--;
			if (naomi[i]>ken[head]){
				head++;
				win1++;
			}
		}

		head=0;
		tail=N-1;
		int win2=0;

		for(int i=0;i<naomi.size();i++){
			while (head<N && naomi[i]>ken[head])
				head++;
			if (head==N)
				win2++;	
			else{
				head++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<win1<<" "<<win2<<endl;

	}
	system("pause");
}