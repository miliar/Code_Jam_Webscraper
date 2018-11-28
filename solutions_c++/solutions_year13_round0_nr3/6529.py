
#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <algorithm>
#include <math.h>
#define _SECURE_SCL 0
#define _HAS_ITERATOR_DEBUGGING 0
using namespace std;
int power(int a,int b)
{
	int temp = a;
	for(int g=0;g<b-1;g++)
		a*=temp;
	if(b==0)
		return 1;
	else 
		return a;
}
class number
{
public:
	vector<int> digits;
	vector<int> squareDig;
	bool isP;
	bool isSqP;
	void isPar()
	{
   isP = true;
		for(int g=0;g<digits.size()/2;g++)
		{
			if(digits[g]!=digits[digits.size()-g-1])
			{
				isP = false;
				break;
			}
		}
		
	isSqP = true;
		for(int g=0;g<squareDig.size()/2;g++)
		{
			if(squareDig[g]!=squareDig[squareDig.size()-g-1])
			{
				isSqP = false;
				break;
			}
		}
	
	}

	number(int a)
	{
		while(a>0)
		{
			digits.push_back(a%10);
			a/=10;
		}
		square();
	}
	number(string a)
	{
		digits.resize(a.size());
		for(int g=0;g<a.size();g++)
		{
			digits[a.size()-1-g]=(a[g]-48);
		}
		square();
	}
	void print()
	{
		cout<<"Digit : ";
		for(int g=digits.size()-1;g>=0;g--)
		{
			cout<<digits[g];
		}
		cout<<endl;
		cout<<"SquareDigit : ";
		for(int g=squareDig.size()-1;g>=0;g--)
		{
			cout<<squareDig[g];
		}
		cout<<endl;
   cout<<isP<<" "<<isSqP<<endl;
	}
	void square()
	{
		vector<int> res;
		vector<int> di2;
		di2 = digits;
		res.resize(di2.size(),0);
		for(int g=0;g<digits.size();g++)
		{
			for(int h=0;h<di2.size();h++)
			{
				int a = digits[g]*di2[h];
				try
				{
					res.at(g+h+1);
					res[g+h]+=a;
				}
				catch(...)
				{
					vector<int>::iterator it;
					it = res.end();
					res.insert(it,0);
					res[g+h]+=a;
				}
			}
      isPar();
		}
		for(int g=0;g<res.size()-1;g++)
		{
			res[g+1]+=res[g]/10;
			res[g]=res[g]%10;
		}
		if(res[res.size()-1]==0)
		{
			vector<int>::iterator it;
			it = res.end()-1;
			res.erase(it);
		}
		squareDig = res;
   isPar();
	}
	void addOne()
	{
		digits[0]+=1;
		digits.push_back(0);
		for(int g=0;g<digits.size()-1;g++)
		{
			digits[g+1]+=digits[g]/10;
			digits[g]=digits[g]%10;
		}
		if(digits[digits.size()-1]==0)
		{
			vector<int>::iterator it;
			it = digits.end()-1;
			digits.erase(it);
		}
		square();
	}
};
bool larger(number &l,number &r)
{
	if(l.digits.size()>r.digits.size())
	{
		return true;
	}
	else if(l.digits.size()==r.digits.size())
	{
		for(int g=l.digits.size()-1;g>=0;g--)
		{
			if(l.digits[g]>r.digits[g])
				return true;
			else if(l.digits[g]<r.digits[g])
				return false;
		}
		return true;// two number are equal
	}
}
bool Slarger(number &l,number &r)
{
	if(l.squareDig.size()>r.squareDig.size())
	{
		return true;
	}
	else if(l.squareDig.size()==r.squareDig.size())
	{
		for(int g=l.squareDig.size()-1;g>=0;g--)
		{
			if(l.squareDig[g]>r.squareDig[g])
				return true;
			else if(l.squareDig[g]<r.squareDig[g])
				return false;
		}
		return true;// two number are equal
	}
}
bool Mlarger(number &l,number &r)
{
	if(l.squareDig.size()>r.digits.size())
	{
		return true;
	}
	else if(l.squareDig.size()==r.digits.size())
	{
		for(int g=l.squareDig.size()-1;g>=0;g--)
		{
			if(l.squareDig[g]>r.digits[g])
				return true;
			else if(l.squareDig[g]<r.digits[g])
				return false;
		}
		return false;// two number are equal
	}
}

bool M1larger(number &l,number &r)
{
	if(l.squareDig.size()>r.digits.size())
	{
		return true;
	}
	else if(l.squareDig.size()==r.digits.size())
	{
		for(int g=l.squareDig.size()-1;g>=0;g--)
		{
			if(l.squareDig[g]>r.digits[g])
				return true;
			else if(l.squareDig[g]<r.digits[g])
				return false;
		}
		return true;// two number are equal
	}
}
int main(int argc, char* argv[])
{
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	int runs;
	in>>runs;
	for(int g=0;g<runs;g++)
	{
		string start;
		string end;
		in>>start;
		in>>end;
		number sN(start);
		number eN(end);
		number n(1);
		int num=0;
		while(!M1larger(n,sN))
		{
			n.addOne();
		}
		while(1)
		{

			if(n.isP&&n.isSqP)
			{
      	num++;
       }
			n.addOne();
      if(Mlarger(n,eN))
      break;    
		}
    

    
		out<<"Case #"<<g+1<<": "<<num<<endl;
	}

	//system("pause");
	return 0;
}

