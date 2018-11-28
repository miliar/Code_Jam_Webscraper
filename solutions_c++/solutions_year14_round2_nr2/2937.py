#include<fstream> //freopen相应的版本
#include<iostream>

#include <list> 
#include <string>
#include <typeinfo>
#include <fstream>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>



using namespace std;

//#define STDIO//关键开关,上传的时候一定要打开


#ifdef STDIO
	 #define fin cin
	 #define fout cout
#else

	ifstream fin("data.in");
	ofstream fout("data.out");

#endif
// void swap(int * a, int *b);

#define MAX(a,b,c)  (a>b?a:b)>c?(a>b?a:b):c

 
//模板函数：将string类型变量转换为常用的数值类型（此方法具有普遍适用性）
 
double stringToNum(const string& str)  
{  
    istringstream iss(str);  
    double num;  
    iss >> num;  
    return num;      
} ; 

void Swap(int &a, int &b);
vector<string > split(const string src, string separate_character);
class stone
{
	
	public: stone(){};
		int aa; 
		int bb;
		void pp()
	{
		fout<<aa<<"  "<<bb<<endl;
	};

};


int main()
{

/* 
	 int a ,b;
	while(fin>>a>>b)//input forever
	 {
		fout<<a+b<<"\n";
	} */

	//fout<<stringToNum("987465")<<endl;fout<<stringToNum("987465")+2<<endl;
	
	int CaseN=0;
	fin>>CaseN;
	for(int i=0;i<CaseN;i++)	
	{
/*
		int N;
		fin>>N;
		for(int i=0;i<=N;i++)	
		{ 
			string ok;
		 getline(fin,ok);
		 fout<<ok<<endl;;
		}
		*/

		int A=0; int B=0; int K=0;

		fin>>A>>B>>K;
		int counter=0;
		for(int ii=0;ii<A;ii++)
		{	
			for(int j=0;j<B;j++)
			{

				if((ii&j)<K) { counter++;}	
			}
		}
	fout<<"Case #"<<(i+1)<<": "<<counter<<endl;;
	}


	/* string ok;
	//while( getline(fin,ok) )//一个行一行读取
	vector<string> v;
	for(int i=0;i<=CaseN;i++)	
	{
		getline(fin,ok);
		v.push_back(ok);
		
	}
		for(int j=0;j<v.size();j++)
			fout<<v[j]<<endl;



	while( fin >> ok)//一个字一个字读取
	{
		fout<<ok<<endl;
	} 

  	fout.precision(6);                    //精度恢复为6	
	fout<<0.123456789;
	
	fout<<ln;
	

	vector<string> good=split("let us see us lus ok"," ");
	int k=0;
	for(;k<good.size();k++)
		fout<<endl<<"Case #"<<k<<": "<<good[k];
	stone  all;
	all.aa=111;
	all.bb=222;
	 
	swap(all.aa,all.bb);	
	fout<<endl<<all.aa<<" "<<all.bb<<endl;

	*/

return 0;
}

//string str="12345";		2.aotl():  long int atol ( const char * str );   atof():  double atof ( const char * str );
//int b=atoi(str.c_str());

//这个函数交换二个正数
/*void swap(int * a, int *b)
{
	(*a)=(*a)^(*b);
	(*b)=(*b)^(*a);
	(*a)=(*a)^(*b);
}*/
void Swap(int &a, int &b)
{
a=a^b;
b=b^a;
a=a^b;
}
//按行读取的话有string 头文件里面的getline(fin, ok)
//C/C++中的Split函数是strtok()其函数原型如下:
//char * strtok (char * str, const char * delimiters); 
vector<string > split(const string src, string separate_character)
{         
	vector<string > strs;
           int separate_characterLen = separate_character.size();//分割字符串的长度,这样就可以支持如“,,”多字符串的分隔符
            int lastPosition = 0,index = -1;             
	while (-1 != (index = src.find(separate_character,lastPosition)))          
	{              
		strs.push_back(src.substr(lastPosition,index - lastPosition));             
		lastPosition = index + separate_characterLen;          
	}        
 	string lastString = src.substr(lastPosition);//截取最后一个分隔符后的内容             
	if (!lastString.empty())            
	strs.push_back(lastString);//如果最后一个分隔符后还有内容就入队             
return strs;    
}    
