#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include <iomanip>
typedef long long int LL;
using namespace std;
int main()
{
	ofstream myfile;
 	myfile.open ("cookie_output.txt");
 	double C,F,X,P,total,temp1,temp2;
 	int t;
 	myfile<<setprecision(7)<<fixed;
 	
	cin>>t;
	for(int i=1;i<=t;++i){	
		P = 2;
		total=0.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		while(true){
			temp1 = total + (X/P);
			temp2 = total + (C/P)+(X/(P+F));
			if(temp1 <= temp2){
				total = total + (X/P);
				break;
			}
			else
				total = total + (C/P);
			P = P + F;
		}
		myfile<<"Case #"<<i<<":"<<" "<<total<<endl;
	}
	return 0;
}

