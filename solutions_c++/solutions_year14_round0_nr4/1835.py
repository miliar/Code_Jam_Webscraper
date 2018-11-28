#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

FILE *in, *out;


int main(){

	int t=0;
	int i=0, j=0;
	int n=0;

	in=fopen("D-large.in","r");
	out=fopen("D-large.out","w");

//	in=fopen("input.txt","r");
//	out=fopen("output.txt","w");



	fscanf(in,"%d",&t);


	for(int a=0; a<t; a++){
		
		vector <double> naomi;
		vector <double> ken;
		vector <double> naomi2;
		vector <double> ken2;
		double temp;
		int big=0, small=0;

		fprintf(out,"Case #%d: ",a+1);
//		printf("Case #%d: ",a+1);

		fscanf(in,"%d",&n);

		for(i=0; i<n; i++){
			fscanf(in,"%lf",&temp);
			naomi.push_back(temp);
			naomi2.push_back(temp);
		}
		for(i=0; i<n; i++){
			fscanf(in,"%lf",&temp);
			ken.push_back(temp);
			ken2.push_back(temp);
		}

		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		
		sort(naomi2.begin(),naomi2.end());
		sort(ken2.begin(),ken2.end());

		while(1){	
			int cnt=0;
			for(i=0; i<naomi.size(); i++){
				if(naomi[i]>ken[i]) cnt++;
				else break;
			}

			if(cnt==naomi.size()){
				big+=naomi.size();
				break;
			}
			else if(naomi.back()<ken.front()){
				big+=0;
				break;
			}
			else{
					naomi.erase(naomi.begin());
					ken.pop_back();
			}
			if(naomi.empty()) break;

		}

		fprintf(out,"%d ",big);

		while(1){	
			int cnt=0;
			for(i=0; i<naomi2.size(); i++){
				if(naomi2[i]<ken2[i]) cnt++;
				else break;
			}

			if(cnt==naomi2.size()){
				small+=0;
				break;
			}
			
			else{
					small++;
					naomi2.pop_back();
					ken2.erase(ken2.begin());

			}
			if(naomi2.empty()) break;

		}




		fprintf(out,"%d\n",small);





	}
	fclose(in);
	fclose(out);

	return 0;


}