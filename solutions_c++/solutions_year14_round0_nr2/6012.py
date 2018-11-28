#include <bits/stdc++.h>

using namespace std;

int main(){
	int T ;
	double C , F , F1 , X , tot , totemp1 , totemp2;
	cin>>T;
	ofstream cout;
	FILE *file = fopen("outputFile.txt","w");
	for (int t = 1; t <= T; ++t)
	{
		cin>>C;
		cin>>F;
		F1 = 2;
		cin>>X;
		tot=totemp1=totemp2=0;
		while(totemp1 >= totemp2){
			totemp1 = tot + X/F1;
			tot+=C/F1;
			F1+=F;
			totemp2 = tot + X/F1 ;
		}
		fprintf(file,"Case #%d: %.7f\n",t,totemp1);
	}
	return 0;
}