#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

bool resSign = 0;
bool aSign = 0;



void print(std::vector <char> *strng)
{
	for(int i=0; i<strng->size(); i++)
		cout<<strng->at(i);
}

char mul(char a, char b)
{
	if(a == '1')
		return b;
	else if(b == '1')
		return a;
	else if(a == b)
	{
		if(aSign == 1)
			aSign = 0;
		else
			aSign = 1;
		return '1';
	}
	else if(a == 'i')
	{
		if(b == 'j')
			return 'k';
		else
		{
			if(aSign == 1)
				aSign = 0;
			else
				aSign = 1;

			return 'j';
		}
	}
	else if(a == 'j')
	{
		if(b == 'i')
		{
			if(aSign == 1)
				aSign = 0;
			else
				aSign = 1;

			return 'k';
		}
		else
			return 'i';
	}
	else if(a == 'k')
	{
		if(b == 'i')
			return 'j';
		else
		{
			if(aSign == 1)
				aSign = 0;
			else
				aSign = 1;
			return 'i';
		}
	}
}

int main()
{
	ifstream in("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");	
	//ifstream in("problem1.in");
	//ofstream cout("problem1.out");	

	int T;
	in>>T;

	int i=0;
	while(i<T)
	{
		aSign = 0;
		std::vector <char> strng;
		int L, X;
		in>>L>>X;
		
		int j=0;
		char ch;
		while(j<L)
		{
			in>>ch;
			strng.push_back(ch);

			j++;
		}
		if(L == 1)
		{
			cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
			i++;
			continue;
		}
		strng.resize(L*X);
		j=0;
		while(j<X)
		{			
			std::copy(strng.begin(), strng.begin()+L, strng.begin()+j*L);
			j++;
		}
		//cout<<strng.size()<<endl;
		//print(&strng);

		j=0;
		int size = L*X;
		bool yesNo = false;
		char res1 = '1';
		
		while(j<size)
		{
			res1 = mul(res1, strng[j]);
			
			if(res1 == 'i' && aSign == 0)
			{
				break;
			}
			j++;
		}
		char res2 = '1';
		int k=j+1;

		while(k<size)
		{
			res2 = mul(res2, strng[k]);
					
			if(res2 == 'j' && aSign == 0)
			{				
				break;
			}
			k++;
		}
		char res3 = '1';
		int l = k+1;

		while(l<size)
		{				
			res3 = mul(res3, strng[l++]);							

			if(res3 == 'k' && l == size && aSign == 0)
			{
				cout<<"Case #"<<i+1<<": "<<"YES"<<endl;
				k=size;
				j=size;
				yesNo = true;
				break;
			}

		}

		if(!yesNo)
			cout<<"Case #"<<i+1<<": "<<"NO"<<endl;

		strng.clear();
		strng.empty();
		i++;
	}

	system("pause");
	return 0;
}