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
	int N;
	cin >> N;
	string words[100];
	int pos[100];
	int num[100];

	for(int ii=0; ii<N; ii++){
		cin >> words[ii];
		pos[ii] = 0;
	}

	int ans = 0;
	while(1){
		if(pos[0] >= (int)words[0].length()) break;
		char s = words[0].at(pos[0]);
		int min_num = 99999999;
		int max_num = 0;
		for(int ii=0; ii<N; ii++){
			num[ii] = 0;
			while(1){
				if(pos[ii] >= (int)words[ii].length()) break;
				if(words[ii].at(pos[ii]) != s) break;
				pos[ii]++;
				num[ii]++;
			}
			if(num[ii] == 0){
				cout << "Fegla Won" << endl;
				return;
			}
			min_num = min(min_num, num[ii]);
			max_num = max(max_num, num[ii]);
		}

		int min_ans = 99999999;
		for(int ii=min_num; ii<= max_num; ii++){
			int sum = 0;
			for(int jj=0; jj<N; jj++){
				sum += abs(ii - num[jj]);
			}
			min_ans = min(min_ans, sum);
		}
		ans += min_ans;
	}

	for(int ii=0; ii<N; ii++){
		if(pos[ii] != (int)words[ii].length()){
			cout << "Fegla Won" << endl;
			return;
		}
	}

	cout << ans << endl;
}
