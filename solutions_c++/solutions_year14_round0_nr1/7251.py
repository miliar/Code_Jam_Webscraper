// google.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>
#include<fstream>

using namespace std;

//#include "stdlib.h"

int main(int argc, char* argv[])
{
	FILE *fp;
	FILE *out;
	if( (fp=fopen("A-small-attempt4.in","r" ))==NULL )
		cout<<"\n���ܴ�in�ļ�" <<endl;
	ofstream fout("A-small-attempt3.out");

//	if( (out=fopen("A-small-attempt0.txt","w" ))==NULL )
//		cout<<"\n���ܴ�out�ļ�" <<endl;

	int array[2][4];
//	int *p;
	int T,m;
	int i,j;
	int k;//�治ʹ������
//	int seg;
	int row1,row2;
	string key;
	int num;
	fscanf(fp,"%d",&T);
	for(m=0;m<T;m++)
	{
		fscanf(fp,"%d",&row1);
		for( i=0 ; i < (row1-1)*4 ; i++ )
			fscanf(fp,"%d", &k); //����¼δѡ����
		//cout <<k<<"njilu"<<endl;}
		for(i=0;i<4;i++)  //��¼ѡ����
			fscanf(fp,"%d", &array[0][i]);
		//cout <<"jilu"<<endl;}
		for(i=row1*4 ; i<16;i++)
			fscanf(fp,"%d",&k);



		fscanf(fp,"%d",&row2);     //�ڶ�������
		//cout <<row2<<endl;
		for( i=0 ; i < (row2-1)*4 ; i++ )
			fscanf(fp,"%d", &k); //����¼δѡ����
		key="";
		for(i=0;i<4;i++)				//��¼ѡ����
		{
			fscanf(fp,"%d", &array[1][i]);
			for(j=0;j<4;j++)
				if(array[1][i]==array[0][j])
					if( key=="")
					{
						key = "s";
						num=array[0][j];
					}
					else if( key!="" )
					{
						key = "Bad magician!";
					}
		}
		for(i=row2*4 ; i<16;i++)
			fscanf(fp,"%d",&k);
		if(key == "")
			key = "Volunteer cheated!";
		if(key != "s")
//		{	cout << "heng ";
			fout<<"Case #"<<m+1 <<": "<<key<<endl;

		//	cout <<"Case #"<<m+1 <<": "<<key<<endl;
		else
//		{	cout << "oo";
			fout<<"Case #"<<m+1<<": "<<num<<endl;
	}
	return 0;
}
