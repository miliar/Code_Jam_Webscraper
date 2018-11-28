/*
ID: bchen
PROG: consonants
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <climits>
#include <cctype>

using namespace std;

int pos = 0;
vector<char> str;

/*
int vect_find(char c, int position)
{
	for(unsigned i=position;i<str.size();i++)
	{
		if(str[i] == c)
		{
			return i;
		}
	}
	return INT_MAX;
}

int min(const vector<int>& vect)
{
	int mi = INT_MAX;
	for(unsigned i=0;i<vect.size();i++)
	{
		mi = (vect[i]<mi) ? str[i] : mi;
	}
	return mi;
}

bool next_vowel(int position)
{
	vector<int> nexts;
	nexts.push_back(pos);
	nexts.push_back(vect_find('a',pos+1));
	nexts.push_back(vect_find('e',pos+1));
	nexts.push_back(vect_find('i',pos+1));
	nexts.push_back(vect_find('o',pos+1));
	nexts.push_back(vect_find('u',pos+1));

	int mi = min(nexts);
	if(mi == pos || (unsigned)pos >= str.size())
	{
		return false;
	}
	else
	{
		pos = mi;
		return true;
	}
}
*/

int main()
{	
	ifstream fin("consonants.in");

	unsigned T;
	fin>>T;
	fin.unsetf(ios_base::skipws);
	ofstream fout("consonants.out");
	for(unsigned i=0;i<T;i++)
	{
		//cout<<"STARTING: "<<i+1<<endl;
		int n,n_value=0;
		while(true)
		{
			char ch;
			fin>>ch;
			if(ch == ' ')
			{
				break;
			}
			else if(isalpha(ch))
			{
				str.push_back(ch);
			}
		}
		fin>>n;
		//cout<<"GOTTEN"<<endl;

		vector<int> vowels;
		for(unsigned k=0;k<str.size();k++)
		{
			if(str[k] == 'a' || str[k] == 'e' || str[k] == 'i' || str[k] == 'o' || str[k] == 'u')
			{
				vowels.push_back(k);
			}
		}
		/*
		while(true)
		{
			bool bk;
			bk = next_vowel(pos);
			if(bk && (unsigned)pos < str.size())
			{
				vowels.push_back(pos);
				cout<<"VOWEL AT: "<<pos<<endl;
			}
			else
			{
				break;
			}
		}
		*/
		//cout<<vowels.size()<<" VOWELS FOUND"<<endl;

		int posit = n-1;

		if(str.size()-vowels.size() < (unsigned)n)
		{
			goto output;
		}

		//cout<<"REDUCING"<<endl;
		bool reduced[str.size()];
		for(unsigned k=0;k<str.size();k++)
		{
			reduced[k] = false;
		}
		for(unsigned k=0;k<vowels.size();k++)
		{
			reduced[vowels[k]] = true;
		}
		//cout<<"REDUCED"<<endl;

		/*
		int current[n];
		cout<<"GETTING FIRST CONSONANTS"<<endl;
		while((unsigned)posit < str.size() && cnt < n)
		{
			if(!reduced[posit])//If consonant
			{
				current[cnt] = posit;
				cout<<posit<<endl;
				cnt++;
			}
			posit++;
		}
		posit--;
		cout<<"GOTTEN"<<endl<<endl;
		*/

		while((unsigned)posit < str.size())
		{
			bool tr = true;
			for(int k=posit-n+1;k<=posit;k++)
			{
				if(reduced[k])
					tr = false;
			}
			if(tr)//If consonants
			{
				int x=1,ctr=1,ct=n;
				while(ctr <= posit-n+1)
				{
					if(reduced[posit-n+1-ctr])
					{
						x++;
						ct=0;
					}
					else
					{
						ct++;
						if(ct >= n)
						{
							break;
						}
						x++;
					}
					ctr++;
				}
				//cout<<"LETTERS BEFORE "<<posit-n+1<<": "<<x-1<<endl;
				//cout<<"LETTERS AFTER "<<posit<<": "<<str.size()-posit-1<<endl;
				n_value += x*(str.size() - posit);
			}
			posit++;
		}

		output:
		fout<<"Case #"<<i+1<<": "<<n_value<<endl;
		//cout<<"Case #"<<i+1<<": "<<n_value<<endl<<endl;
		pos = 0;
		str.clear();
	}
	
	return 0;
}
