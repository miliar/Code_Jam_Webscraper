// temp.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#include<iostream>
#include<string>
using namespace std;

//cache��
struct block
{
	int addr;
	string val[8];
	char state;
};

//�ڴ�
string mem[300];
//cache
block cache[2][4];

//��ʼ��cache
void blockInit(block* b)
{
	b->addr=0;
	for(int i=0;i<8;i++)
		b->val[i]="00";
	b->state='I';
}

//ʮ������תʮ����
int convertAddrTo10(char add[5])
{
	int ret = 0;
	for(int i=0;i<4;i++)
		ret = ret*16+(add[i]<='9'?add[i]-'0':add[i]-'A'+10);
	return ret;
}

//ʮ����תʮ������
void convertAddrTo16(int addr,char add[5])
{
	for(int i=3;i>=0;i--)
	{
		int a=addr%16;
		add[i]=a>9?a-10+'A':a+'0';
		addr/=16;
	}
	add[4]='\0';
}

//��cache��mem��дֵ
void writeValue(string* des,string* src,int n)
{
	for(int i=0;i<n;i++)
		*(des+i) = *(src+i);
}

void debug()
{
	int i,j;
	char add[5];
	for(i=0;i<2;i++){
		for(j=0;j<4;j++)
		{
			convertAddrTo16(cache[i][j].addr,add);
			printf("P%d:%s:",i,add);
			for(int k=4;k<8;k++)
				cout<<cache[i][j].val[k]<<" ";
			for(int k=0;k<3;k++)
				cout<<cache[i][j].val[k]<<" ";
			cout<<cache[i][j].val[3]<<":"<<cache[i][j].state<<endl;
		}
		cout<<endl;
	}
	for(i=0;i<=256;i+=8)
	{
		convertAddrTo16(i,add);
		printf("MM:%s:",add);
		for(j=4;j<8;j++)
			cout<<mem[i+j]<<" ";
		for(j=0;j<3;j++)
			cout<<mem[i+j]<<" ";
		cout<<mem[i+3]<<endl;
	}
}

void writemiss(int opno,int offset){
	if(cache[opno][offset].state=='S')
		cache[opno][offset].state = 'I';
	else if(cache[opno][offset].state=='E'){
		//д�ؿ�
		writeValue(&mem[cache[opno][offset].addr],cache[opno][offset].val,8);
		writeValue(cache[(opno+1)%2][offset].val,cache[opno][offset].val,8);
		cache[opno][offset].state = 'I';
	}
}

void readmiss(int opno,int offset){
	if(cache[opno][offset].state=='S')
		;
	else if(cache[opno][offset].state=='E'){
		//д�ؿ�
		writeValue(&mem[cache[opno][offset].addr],cache[opno][offset].val,8);
		cache[opno][offset].state = 'S';
	}
}

void write(int pno,int address,string value[4])
{
	int t=address/8;
	int m=address%8;
	int offset=t%4;
	int opno=(pno+1)%2;
	bool opexist = 0;
	if(cache[opno][offset].addr==address-m)
		opexist=1;
	char st=cache[pno][offset].state;
	//��Ч
	if(st=='I'){
		//дȱʧ������
		if(opexist)
			writemiss(opno,offset);
		writeValue(cache[pno][offset].val+m,value,4);
		cache[pno][offset].addr = address-m;
		cache[pno][offset].state = 'E';
	}
	//��ռ
	else if(st=='E'){
		//д����
		if(address-m == cache[pno][offset].addr)
			writeValue(cache[pno][offset].val+m,value,4);
		//дȱʧ
		else
		{
			writeValue(&mem[cache[pno][offset].addr],cache[pno][offset].val,8);
			//дȱʧ������
			if(opexist)
				writemiss(opno,offset);
			writeValue(cache[pno][offset].val+m,value,4);
			cache[pno][offset].addr = address-m;
			cache[pno][offset].state = 'E';
		}
	}
	//����
	else if(st=='S'){
		//��Ч������
		if(opexist)
			cache[opno][offset].state = 'I';
		writeValue(cache[pno][offset].val+m,value,4);
		cache[pno][offset].addr = address-m;
		cache[pno][offset].state = 'E';
	}
}

void read(int pno,int address)
{
	int t=address/8;
	int m=address%8;
	int offset=t%4;
	int opno=(pno+1)%2;
	bool opexist = 0;
	if(cache[opno][offset].addr==address-m)
		opexist=1;
	char st=cache[pno][offset].state;

	//��Ч
	if(st=='I'){
		//��ȱʧ������
		if(opexist)
			readmiss(opno,offset);
		writeValue(cache[pno][offset].val+m,&mem[address],4);
		cache[pno][offset].addr = address-m;
		cache[pno][offset].state='S';
	}
	//����
	else if(st=='S')
	{
		//��ȱʧ
		if(cache[pno][offset].addr!=address-m){
			//��ȱʧ������
			if(opexist)
				readmiss(opno,offset);
			writeValue(cache[pno][offset].val,&mem[address-m],8);
			cache[pno][offset].addr = address-m;
			cache[pno][offset].state='S';
		}
	}
	//��ռ
	else if(st=='E')
	{
		//��ȱʧ
		if(cache[pno][offset].addr!=address-m){
			//��ȱʧ������
			writeValue(&mem[cache[pno][offset].addr],cache[pno][offset].val,8);
			writeValue(cache[pno][offset].val,&mem[address-m],8);
			cache[pno][offset].addr = address-m;
			cache[pno][offset].state='S';
		}
	}
}
struct at{
       char a;
       int b;
       static long d ;
	};
int main()
{
	int pno;
	char add[5];
	string value[4];
	char op;

	
	cout<<sizeof(at);

	//for(int i=0;i<2;i++)
	//	for(int j=0;j<4;j++)
	//		blockInit(&cache[i][j]);
	//for(int i=0;i<300;i++)
	//	mem[i]="00";

	//while(1)
	//{
	//	scanf("%c",&op);
	//	if(op=='D')
	//	{
	//		debug();
	//	}
	//	else
	//	{
	//		scanf(":P%d:%4s",&pno,add);
	//		int address = convertAddrTo10(add);
	//		if(op=='W'){
	//			getchar();
	//			for(int i=0;i<4;i++)
	//				cin>>value[i];
	//			write(pno,address,value);
	//		}
	//		else
	//			read(pno,address);
	//	}
	//	getchar();

	//}


	return 0;

}
