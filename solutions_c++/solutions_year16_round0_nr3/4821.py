#include<iostream>
#include<string>
#include<fstream>
#include<stack>
#include<sstream>
#include <math.h>
#include <cmath>
#include <algorithm>

using namespace std;
int act_no=0;
string S;
string divs;
unsigned long long int  PrintAsBase(int num,int out_base)
{
	string digits("0123456789ABCDEF");
	bool is_neg = num < 0;
	string result;
	int in_num = num;
	int in_base = out_base;

	for (; in_num; in_num /= in_base)
	{
		result.insert(result.begin(), digits[abs(in_num % in_base)]);
	}

	if (is_neg)
	{
		result.insert(result.begin(), '-');
	}
	unsigned long long int r;
	for(int i=result.size();result[i]!='\0';i++)
	r=(result[0]-'0');
	cout << result << '\n';
	return r;
}
void convetsd(int n)
{
	string sec;
	stringstream ss;
	ss <<n;
	sec.append(ss.str());
	divs.insert(0,sec);
}
bool isPrime (unsigned long long int num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return true;
    else if (num % 2 == 0){
		convetsd(2);
		return false;
	}
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0){
				prime = false;
				convetsd(divisor);
				return prime;
			}
            divisor +=2;
        }
        return prime;
    }
}

void convets(int n)
{
	string sec;
	stringstream ss;
	ss <<n;
	sec.append(ss.str());
	S.insert(0,sec);
}
void convert10tob(int N, int b)
{
     if (N == 0)
        return;
     int x = N % b;
     N /= b;
     if (x < 0)
        N += 1; 
     convert10tob(N, b);
	 convets((x < 0 ? x + (b * -1) : x));
     return;
}
bool checkforz(char z)
{
	if(z!='0')
		return false;
	return true;

}
bool checkforo(char z)
{
	if(z!='1')
		return false;
	return true;

}
bool checkforpartjam(string ser,int len)
{
	int s1=ser.size();
	bool flag=false;
	for(int i=0;i<(ser.size()-1);i++)
	{
		if(!checkforo(ser[i]))
		{
			if(!checkforz(ser[i]))
			return false;
		}
	}
	if(ser[0]=='1')
	{
		if((s1)==len){
		if(ser[s1-1]=='1')
			
			return true;}
	}
		
	return false;
}
void reverse()
{

char arr[100];
//rev[0]=S[S.size()-1];
for(int i=S.size()-1,j=0;i>=0;i--)
{
	if(S[i]!='\0'){
		arr[j]=S[i];
		j++;
	arr[j]='\0';
	}
}

string rev(arr);
S=rev;
}
void reversed()
{

char arr[100];
//rev[0]=S[S.size()-1];
for(int i=divs.size()-1,j=0;i>=0;i--)
{
	if(divs[i]!='\0'){
		arr[j]=S[i];
		j++;
	arr[j]='\0';
	}
}

string rev(arr);
divs=rev;
}
unsigned long long int stoi(int in,const string& _Str, size_t *_Idx = 0,int _Base = 10)
	{	// convert string to int
	const char *_Ptr = _Str.c_str();
	char *_Eptr;
	errno = 0;
	unsigned long long int _Ans =  stoull(_Ptr, _Idx, _Base);
	strtoul(_Ptr, &_Eptr, _Base);
	if (_Ptr == _Eptr)
	_Xinvalid_argument("invalid stoi argument");
	if (errno == ERANGE || _Ans < INT_MIN != INT_MAX < _Ans)
		//Xout_of_range("stoi argument out of range");
	if (_Idx != 0)
		*_Idx = (size_t)(_Eptr - _Ptr);
	return ((unsigned long long int)_Ans);
	}
void main()
{
		int tc;
		int J,N;
		ifstream fin("C-small-attempt3.in");
		ofstream fout("output.txt");
		fout<<"Case #1"<<": "<<endl;
		fin>>tc;
		fin>>N;//length
		fin>>J;//
		string s="1";
		char *arr=new char[N+1];
		for(int i=1;i<=N;i++){
			arr[i]='0';
		}
		arr[0]=arr[N-1]='1';
		arr[N]='\0';
		string sero(arr);
		unsigned long long int no=stoi(sero,0,2);
		bool checkpart2=false;
		bool prime;
		unsigned long long int div[9];
		bool flag=true;
		//S=sero;
		for(int i=0;i<tc;i++){
			for(int j=0;j<J&&sero.size()<=N;){
				flag=true;
				sero=to_string(no);
				convert10tob(no,2);
				reverse();
				sero=S;
					if(checkforpartjam(sero,N))
					{
						for(int b=2;b<=10;b++){
							
							divs='\0';
							unsigned long long int nos=stoi(0,sero,0,b);
							cout<<sero<<endl;
							if(isPrime(nos))
							{
								flag=false;
								break;
							}
							else{
								div[b-2]=stoi(0,divs,0,10);
							}
						}
						if(flag)
						{
							S='\0';
							j++;
							fout<<sero<<" ";
							for(int z=0;z<9;z++)
								fout<<div[z]<<" ";
							fout<<endl;
							cout<<"1"<<endl;
						}
						
						no++;
						S='\0';
					}
					else{
						S='\0';
						no++;
					}
				
				
			}
		}
		
		}
