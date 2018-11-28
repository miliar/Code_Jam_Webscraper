#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>

using namespace std;

class node
{
public :
	char value;
	int sign;
	string getstring()
	{

	//	string x = +value
		///return
	}
	node(char x)
	{
		if(x!= 't' && x!='p')
		{
			sign = 1;
			value = x;
		}
		else if(x == 't')
		{
			sign = -1;
			value = '1';
		}
		else if(x == 'p')
		{
			sign = 1;
			value ='1';
		}
	}
	node()
	{}
	node operator*(node right)
	{
		node result;
		result.sign = sign * right.sign;
		if(value == '1' && right.value == '1')
		{
			result.sign= result.sign;
			result.value= '1';
		}
		else if(value == '1' && right.value == 'i')
		{
			result.sign= result.sign;
			result.value= 'i';
		}
		else if(value == '1' && right.value == 'j')
		{
			result.sign= result.sign;
			result.value= 'j';
		}
		else if(value == '1' && right.value == 'k')
		{
			result.sign= result.sign;
			result.value= 'k';
		}
		// 2nd op
		else if(value == 'i' && right.value == 'i')
		{
			result.sign= result.sign * -1;
			result.value= '1';
		}
		else if(value == 'i' && right.value == 'j')
		{
			result.sign= result.sign;
			result.value= 'k';
		}
		else if(value == 'i' && right.value == 'k')
		{
			result.sign= result.sign * -1;
			result.value= 'j';
		}
		else if(value == 'i' && right.value == '1')
		{
			result.sign= result.sign;
			result.value= 'i';
		}
		// 3rd op
		else if(value == 'j' && right.value == '1')
		{
			result.sign= result.sign;
			result.value= 'j';
		}
		else if(value == 'j' && right.value == 'i')
		{
			result.sign= result.sign * -1;
			result.value= 'k';
		}
		else if(value == 'j' && right.value == 'j')
		{
			result.sign= result.sign * -1;
			result.value= '1';
		}
		else if(value == 'j' && right.value == 'k')
		{
			result.sign= result.sign;
			result.value= 'i';
		}
		// asdsa 
		else if(value == 'k' && right.value == '1')
		{
			result.sign= result.sign;
			result.value= 'k';
		}
		else if(value == 'k' && right.value == 'i')
		{
			result.sign= result.sign;
			result.value= 'j';
		}
		else if(value == 'k' && right.value == 'j')
		{
			result.sign= result.sign * -1;
			result.value= 'i';
		}
		else if(value == 'k' && right.value == 'k')
		{
			result.sign= result.sign * -1;
			result.value= '1';
		}
		return result;
	}
};

string& simplify(string & x);

int countletters(string k);
void main()
{
	ifstream in("3.in");
//	streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	cin.rdbuf(in.rdbuf());//redirect std::cin to in.txt!

	ofstream out("3.out");
//    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf());
	priority_queue<int> x,y;
	
	int testcases;
	cin>>testcases;
	for(int i = 0 ; i< testcases ; i++)
	{
		int num,repeat;
		string x,pattern;
		cin>>num>>repeat;
		cin>>pattern;
		
		int l = countletters(pattern);
		if(l == 1 )
		{
			cout<<"Case #"<<i+1<<": No"<<endl;
			continue;
		}
		x = pattern;

		
		for(int j = 0 ; j < repeat -1;j++)
			x = x+pattern;
		//x = simplify(x);
		int chcount = x.size();
		bool foundi=false;
		bool foundj=false;
		bool foundk=false;
		bool finished=false;
		node totali;
		node totalj;
		node totalk;
		int lasti,firstk;
		int m,n,b;
		for(m = 0 ; m < chcount;m++)
		{
			node currenti(x[m]);
			totali = m==0?node(x[0]):totali*currenti;
			if(totali.sign == 1 && totali.value == 'i')
			{
				foundi = true;
				lasti=m;
				break;
			}
		}
		for(b = chcount-1 ; b>m ;b--)
		{
			node currentk(x[b]);
			totalk = b==chcount-1?node(x[b]):currentk*totalk;
			if(totalk.sign == 1 && totalk.value == 'k')
			{
				foundk = true;
				firstk=b;
				break;
			}

		}
		for(n = m+1 ; n<b ;n++)
		{
			node currentj(x[n]);
			totalj = n==m+1?node(x[n]):totalj*currentj;
			if(totalj.sign == 1 && totalj.value == 'j'&& n == b-1)
			{
				foundj = true;
			}
		}
		
		if(foundi && foundk && foundj)
			cout<<"Case #"<<i+1<<": Yes"<<endl;
		else
			cout<<"Case #"<<i+1<<": No"<<endl;

	}
}


string& simplify(string & x)
{
	
	bool nothinghappened = false;
	int state = 1;
	node curtotal('p');
	for(int i = 0;i<x.size();i++)
	{
		node current(x[i]);
		curtotal = curtotal * current;
		int iend,jend,kend,onestart;
		if(curtotal.value == 'i' && curtotal.sign == 1)
		{
			x[i] = 'i';
			x.erase(0,i-1);
			state = 2;
			i = 0;
			curtotal = node('p');
		}
		else if(state == 2 && (curtotal.value == '1'||curtotal.value == 'j' ) && curtotal.sign == 1)
		{

		}
		else if(state == 3)
		{

		}
		else if(state == 4)
		{

		}
		else if(state == 5)
		{

		}
	}

	return x;
}


int countletters(string k)
{
	int count = 0;
	map<char,int> m;
	for(int i = 0 ; i< k.size();i++)
	{
		m[k[i]]++;
	}
	return m.size();

}