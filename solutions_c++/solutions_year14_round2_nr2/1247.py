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
		cerr << "Case #" << No << endl;
		cout << "Case #" << No << ": ";
		calc();
	}
	fclose(fp_i);
	fclose(fp_o);
}

/******************************************************************************/

void calc(){
	long long int A;
	long long int B;
	long long int K;
	cin >> A;
	cin >> B;
	cin >> K;

	int ans = 0;
	for(long long int ii = 0; ii < A; ii++){
		for(long long int jj = 0; jj < B; jj++){
			if((ii&jj) < K){
				ans++;
			}
		}
	}

	cout << ans << endl;
}
