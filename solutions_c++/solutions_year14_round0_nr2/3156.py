// temp.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<iostream>
#include<string>
using namespace std;

//cache块
struct block
{
	int addr;
	string val[8];
	char state;
};

//内存
string mem[300];
//cache
block cache[2][4];

//初始化cache
void blockInit(block* b)
{
	b->addr=0;
	for(int i=0;i<8;i++)
		b->val[i]="00";
	b->state='I';
}

//十六进制转十进制
int convertAddrTo10(char add[5])
{
	int ret = 0;
	for(int i=0;i<4;i++)
		ret = ret*16+(add[i]<='9'?add[i]-'0':add[i]-'A'+10);
	return ret;
}

//十进制转十六进制
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

//向cache或mem中写值
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
		//写回块
		writeValue(&mem[cache[opno][offset].addr],cache[opno][offset].val,8);
		writeValue(cache[(opno+1)%2][offset].val,cache[opno][offset].val,8);
		cache[opno][offset].state = 'I';
	}
}

void readmiss(int opno,int offset){
	if(cache[opno][offset].state=='S')
		;
	else if(cache[opno][offset].state=='E'){
		//写回块
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
	//无效
	if(st=='I'){
		//写缺失挂总线
		if(opexist)
			writemiss(opno,offset);
		writeValue(cache[pno][offset].val+m,value,4);
		cache[pno][offset].addr = address-m;
		cache[pno][offset].state = 'E';
	}
	//独占
	else if(st=='E'){
		//写命中
		if(address-m == cache[pno][offset].addr)
			writeValue(cache[pno][offset].val+m,value,4);
		//写缺失
		else
		{
			writeValue(&mem[cache[pno][offset].addr],cache[pno][offset].val,8);
			//写缺失挂总线
			if(opexist)
				writemiss(opno,offset);
			writeValue(cache[pno][offset].val+m,value,4);
			cache[pno][offset].addr = address-m;
			cache[pno][offset].state = 'E';
		}
	}
	//共享
	else if(st=='S'){
		//无效挂总线
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

	//无效
	if(st=='I'){
		//读缺失挂总线
		if(opexist)
			readmiss(opno,offset);
		writeValue(cache[pno][offset].val+m,&mem[address],4);
		cache[pno][offset].addr = address-m;
		cache[pno][offset].state='S';
	}
	//共享
	else if(st=='S')
	{
		//读缺失
		if(cache[pno][offset].addr!=address-m){
			//读缺失挂总线
			if(opexist)
				readmiss(opno,offset);
			writeValue(cache[pno][offset].val,&mem[address-m],8);
			cache[pno][offset].addr = address-m;
			cache[pno][offset].state='S';
		}
	}
	//独占
	else if(st=='E')
	{
		//读缺失
		if(cache[pno][offset].addr!=address-m){
			//读缺失挂总线
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
