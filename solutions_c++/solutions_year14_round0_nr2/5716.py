#include <cstdio>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
double arrf[101];
double arrc[101];
double arrx[101];
double ans[101];
int main(){
	FILE *ifp;
	FILE *ofp;
	ifp=fopen("B-small-attempt0.in","r");
	ofp=fopen("outputfile.txt","w");
	int t,caseno;
	fscanf(ifp,"%d",&t);
	caseno=1;
	double den,temp,tempans;
	while(caseno<=t){
	fscanf(ifp,"%lf %lf %lf",&arrc[caseno],&arrf[caseno],&arrx[caseno]);
	caseno++;
	}
	caseno=1;
	while(caseno<=t){
		den=2.0;
		ans[caseno]=arrx[caseno]/den;
		temp=arrc[caseno]/den;
		tempans=arrx[caseno]/(den+arrf[caseno])+temp;
		while(tempans<ans[caseno]){
			ans[caseno]=tempans;
			den=den+arrf[caseno];
			temp+=arrc[caseno]/den;
			tempans=arrx[caseno]/(den+arrf[caseno])+temp;
		}
	caseno++;
	}
	
	caseno=1;
	while(caseno<=t){
		fprintf(ofp,"Case #%d: %.7lf\n",caseno,ans[caseno]);
	caseno++;
	}
	fclose(ifp);
	fclose(ofp);
return 0;
}
