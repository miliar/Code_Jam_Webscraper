#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <math.h>
#include <algorithm>
using namespace std;

vector <long long int> non_tri;
long long int change_base(string jac,long long int base)
{
	long long int in_dec = 0;
	stringstream s3;
	long long int temp;
	reverse(jac.begin(), jac.end());
	for(int i = 0; i < jac.size(); ++i)
	{
		s3<<jac[i];
		s3>>temp;

		in_dec+=(temp*pow(base,i));

		s3.str("");
		s3.clear();
	}
	return in_dec;
}

string dec2two(long long int decnum)
{
	string tore;
	string retu_final;
	string temp;
	stringstream ss;
	long long int tmp = decnum;
	while(decnum>0) 
	{ 
		ss<<decnum%2; 
		ss>>temp;
		tore+=temp;
		decnum=decnum/2; 
		ss.str("");
		ss.clear();
	} 
	reverse(tore.begin(), tore.end());
	return tore;
}
long long int prime(long long int num)
{
	for(int i = 2; i < sqrt(num); ++i)
	{
		if(num%i==0)
		{
			return num/i;
		}
	}
	return 0;
}
int main(int argc, char* argv[])
{
	string input;
	fstream fin;
	fin.open(argv[1], ios::in);
	getline(fin, input);

	int Ncase, length;
	string jac;
	string jac_ini;
	int count_casenum = 0;
	int input_counter = 0;
	long long int initial_dec;
	int base_count = 0;
	long long int temp;
	long long int prime_temp;
	while(getline(fin, input))
	{
		++input_counter;
		cout<<"Case #"<<input_counter<<":"<<endl;
		count_casenum = 0;
		istringstream ss(input);
		ss>>length>>Ncase;	
		jac[0] = '1';
		jac[length-1] = '1';
		for(int i = 1; i < (length-1); ++i )
		{
			jac[i]='0';
		}
		for(int i = 0; i < length; ++i)///1000...1
		{
			jac_ini+=jac[i];
		}
		initial_dec = change_base(jac_ini, 2);

		while(count_casenum < Ncase)
		{
			base_count = 0;
			non_tri.clear();
			jac_ini = dec2two(initial_dec);
			if(jac_ini[jac_ini.size()-1]=='0')
				jac_ini = dec2two(++initial_dec);
	//		cout<<"count_casenum: "<<count_casenum<<", jac_ini: "<<jac_ini<<endl;
			for(int i = 2; i <= 10; ++i)
			{
				temp = change_base(jac_ini, i);
				prime_temp = prime(temp);
	//			cout<<", jac_ini: "<<jac_ini<<", base: "<<i<<"prime_temp: "<<prime_temp<<endl;
				if(prime_temp==0)
				{
					++initial_dec;
					i=11;
				}
				else{
					non_tri.push_back(prime_temp);
					++base_count;
					++initial_dec;
				}
			}
			if(base_count == 9)
			{
				count_casenum++;
				cout<<jac_ini<<" ";
				for(int i = 0; i < non_tri.size(); ++i)
					cout<<non_tri[i]<<" ";
				cout<<endl;
				++initial_dec;
			}
		}
		
	}
	return 0;
}
