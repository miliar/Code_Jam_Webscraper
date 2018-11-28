#include <iostream>
#include <string>
#include <cmath>
#include <sstream>


//g++ -o a.exe a.cpp
//./a.exe < A-small-practice.in > A-small-practice.out

using namespace std;

string convertInt(unsigned long long int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

bool isPal(string num){
	int len=num.size();
	
	for (int i=0; i<len;i++)
	{
		if (num[i]!=num[len-1-i])
			{return false;}
		
	}
	return true;
}

int cases;
int main()
{
unsigned long long int a,b,square,ans;
string buf;
unsigned long long int buf1;
float art,brt;
	cin >> cases;
	
	isPal("12321");
	for (int c=1; c<=cases; c++)
	{
		ans=0;
		cin >> a >> b;
		art=sqrt(a);
		brt=sqrt(b);
		a= ceil(art);
		b=floor(brt);
		
		for (int i=a; i<=b; i++){
		buf = convertInt(i);	
			if (isPal(buf)){
				buf1=i*i;
				if (isPal(convertInt(buf1))){
					ans ++;
				}
			}
		}	
			
				cout << "Case #"<<c<<": "<< ans << endl;
			}
	return 0;
}