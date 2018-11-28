#include<iostream>
#include <stdio.h>
using namespace std;

int main(){
	int numberOfTestCases;
	cin>>numberOfTestCases;
	int k=1;
	FILE *myfile;
	myfile = fopen ("output.txt","w");
	while(numberOfTestCases){
		double c=0;
		double f=0;
		double x=0;
		cin>>c>>f>>x;
		double current=x/2.0;
		double prev=0;
		int i=1;
		do{
			prev=current;
			double AnsPart2=x/(2+f*i);
			double AnsPart1=0;
			int j=0;
			while(j<i){
				AnsPart1+=1/(2+f*j);
				j++;
			}
			AnsPart1=AnsPart1*c;
			current=AnsPart1+AnsPart2;
			i++;
		}while(prev>current);
		numberOfTestCases--;
		//myfile<<"Case #"<<k<<": "<<prev;
		fprintf (myfile,"Case #%d: %.7f\n",k,prev);
		k++;
	}
	fclose(myfile);
	return 0;
}