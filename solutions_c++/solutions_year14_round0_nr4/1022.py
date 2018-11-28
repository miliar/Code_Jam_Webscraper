/* common *********************************************************************/
#define _CRT_SECURE_NO_WARNINGS
#define ASC 0
#define DESC 1
#include<iostream>
#include<sstream>
#include<fstream>

#include<string>
#include<vector>
#include<list>
#include<map>
#include<algorithm>

#include<exception>
#include<stdexcept>
#include<locale>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>

using namespace std;

void calc();

void GenerateFilename(char* out, char* in, char* add){
	char* p;
	sprintf(out, "%s", in);
	for(p=out+strlen(out)-1; p>=out; p--){
		if(*p=='/' )break;
		if(*p=='\\')break;
		if(*p=='.' ){*p='\0'; break;}
	}
	sprintf(out+strlen(out), "%s", add);
}

void main(int argc, char* argv[]){
	char fname_o[_MAX_PATH];
	GenerateFilename(fname_o, argv[1], "_out.txt");
	FILE* fp_i = freopen(argv[1], "r", stdin);
	FILE* fp_o = freopen(fname_o, "w", stdout);

	int T;
	cin >> T;
	for(int No=1; No<=T; No++){
		cout << "Case #" << No << ": ";
		calc();
	}
	fclose(fp_i);
	fclose(fp_o);
}

/******************************************************************************/

bool warOptimallyKen(list <int> *kens, int naomi){
	for(list <int>::iterator ken = (*kens).begin(); ken != (*kens).end(); ken++){
		if((*ken) > naomi){
			(*kens).remove(*ken);
			return false;
		}
	}
	(*kens).remove(*((*kens).begin()));
	return true;
}

int warOprimallyNaomi(list <int> *naomis){
	int naomi = *((*naomis).begin());
	(*naomis).remove(naomi);
	return naomi;
}

int deceitfulWarOprimallyNaomi(list <int> *naomis, list <int> *kens){
	for(list <int>::iterator naomi = (*naomis).begin(); naomi != (*naomis).end(); naomi++){
		for(list <int>::iterator ken = (*kens).begin(); ken != (*kens).end(); ken++){
			if((*naomi) > (*ken)){
				(*naomis).remove(*naomi);
				return 100000;
			}
		}
	}
	(*naomis).remove(*((*naomis).begin()));
	return 0;

}

void calc(){
	int num;
	list <int> naomis;
	list <int> kens;
	list <int> naomis2;
	list <int> kens2;

	cin >> num;
	for(int ii=0; ii< num; ii++){
		double val;
		cin >> val;
		naomis.push_back((int)(val*100000));
		naomis2.push_back((int)(val*100000));
	}
	for(int ii=0; ii< num; ii++){
		double val;
		cin >> val;
		kens.push_back((int)(val*100000));
		kens2.push_back((int)(val*100000));
	}

	naomis.sort();
	kens.sort();
	int dwp = 0;
	for(int ii=0; ii< num; ii++){
		int naomi = deceitfulWarOprimallyNaomi(&naomis, &kens);
		if(warOptimallyKen(&kens, naomi)){
			dwp++;
		}
	}

	naomis2.sort();
	kens2.sort();
	int wp  = 0;
	for(int ii=0; ii< num; ii++){
		int naomi = warOprimallyNaomi(&naomis2);
		if(warOptimallyKen(&kens2, naomi)){
			wp++;
		}
	}

	cout << dwp << " " << wp << endl;
}
