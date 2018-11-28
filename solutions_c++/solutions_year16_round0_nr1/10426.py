#include <iostream>
#include <fstream>
using namespace std;


int main(){

	int t;

	//ofstream outFile;
	//outFile.open("output.txt");

	cin >>t;
	for(int i=0; i<t; i++){
		int ans_cnt =0;
		unsigned long long int N;
		unsigned long long int tmp;
		int adigit;
		int mult=1;
		cin >> N;
		int digits[10];
		for (int j=0; j<10; j++)
			digits[j]=0;
		//int zero_swt;
		if (N==0){
			cout << "Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
			continue;
		}

		while (ans_cnt!=10){
			tmp =N*mult;
			mult++;
			//zero_swt=0;
			//cout<<"mult: "<<mult<<endl;
			
			while (tmp!=0){
				//cout<<tmp<<endl;
				adigit = tmp%10;
				//if (adigit==0)
					//zero_swt++;
				//cout<<"adigit: "<<adigit<<endl;
				tmp = tmp/10;
				if (digits[adigit]==0){
					digits[adigit]++;
					//cout<<adigit<<endl;
					ans_cnt++;

				}

			}
			


		}
		cout << "Case #"<<(i+1)<<": "<<N*(mult-1)<<endl;
	}
	//outFile.close();	
	return 0;
}