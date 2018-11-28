// googleCode.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
bool isFair(char *a, int len) {
	for(int i=0; i<len/2;i++) {
		if (a[i] != a[len-1-i]) return false;
	}
	return true;
};
void num2char(int x, char *outchar, int &outlen) {
	string temp("") ;
	do {
		temp.push_back(x%10);
		x /= 10;
	}while (x);
	outlen = temp.length();
	for (int i=0; i<outlen; i++) {
		outchar[i] = temp.c_str()[outlen-1-i];
	}
	outchar[outlen] = '\0';
};
int main()
{
	freopen("data.in","r",stdin); //�����ض����������ݽ���in.txt�ļ��ж�ȡ   
	freopen("data.out","w",stdout); //����ض���������ݽ�������out.txt�ļ���   
	
	int t;
	cin>>t;
	char outchar[10000];
	int outlen;
	for (int x=1; x<=t; x++) {
		int a,b;
		int num=0;
		cin>>a>>b;
		int start = floor(sqrt(a*1.0));
		int end = floor(sqrt(b*1.0));
		if (start*start == a ){
			num2char(a,outchar,outlen);
			if (isFair(outchar,outlen)) {
				num++;
			}
		}
		for (int i=start+1; i<=end; i++) {
			num2char(i,outchar,outlen);
			if (isFair(outchar,outlen)) {
				num2char(i*i,outchar,outlen);
				if (isFair(outchar,outlen)) {
					num++;
				}
			}
		}
		cout<<"Case #"<<x<<": "<<num<<endl;
		
	}
//	fclose(stdin);//�ر��ļ�   
//	fclose(stdout);//�ر��ļ�  
	return 0;
}