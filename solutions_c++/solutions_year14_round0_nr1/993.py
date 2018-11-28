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

void calc(){
	char buff[1024];
	int number[17];

	memset(number, 0, sizeof(number));

	int choseRow;
	cin >> choseRow;
	for(int ii=0; ii<choseRow; ii++){
		cin.getline(buff, sizeof(buff));
	}
	for(int ii=0; ii<4; ii++){
		int val;
		cin >> val;
		number[val] = 1;
	}
	for(int ii=choseRow; ii<=4; ii++){
		cin.getline(buff, sizeof(buff));
	}

	int sum=0;
	int ans=0;
	cin >> choseRow;
	for(int ii=0; ii<choseRow; ii++){
		cin.getline(buff, sizeof(buff));
	}
	for(int ii=0; ii<4; ii++){
		int val=0;
		cin >> val;
		if(number[val]){
			ans=val;
			sum++;
		}
	}
	for(int ii=choseRow; ii<=4; ii++){
		cin.getline(buff, sizeof(buff));
	}

	if(      sum==1 ){ cout << ans;                  }
	else if( sum >1 ){ cout << "Bad magician!";      }
	else if( sum==0 ){ cout << "Volunteer cheated!"; }
	cout << endl;
}
