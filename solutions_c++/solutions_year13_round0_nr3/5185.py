// 2012codejam_3.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int a[10000];

int _tmain(int argc, _TCHAR* argv[])
{
	int n,i,j,k,len;
	int st,en;
	char tem[100];
	int flag;
	ifstream ifs;
	ifs.open("input.txt");
	
	ofstream ofs;
	ofs.open("output.txt");

	ifs >> n;

	for(i=1;i<40;i++)
	{
		_itoa_s(i,tem,10);
		len=strlen(tem);
		flag=0;
		for(j=0;j<len/2;j++)
			if(tem[j] != tem[len-1-j])flag++;
		if (flag == 0){
			_itoa_s(i*i,tem,10);
			len=strlen(tem);
			flag=0;
			for(j=0;j<len/2;j++)
				if(tem[j] != tem[len-1-j])flag++;
			if(flag == 0)a[i*i]++;
		}
	}

	for(i=0;i<n;i++)
	{
		ifs >> st >> en;
		k=0;
		for(j=st;j<=en;j++)
			k+=a[j];
		ofs << "Case #" << i+1 << ": " << k << endl;
	}
	return 0;
}

