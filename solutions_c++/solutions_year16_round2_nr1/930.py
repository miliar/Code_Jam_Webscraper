#include <iostream>
using namespace std;
int inWord[30];
int wynik[30];
void process(string s);
int getInWord(char c);
void removeString(string s, int times);
int main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cout<<"Case #"<<aa+1<<": ";
		
		string s;
		cin>>s;
		process(s);
		
	}
}
void process(string s)
{
	for(int i=0; i<30; i++)
	{
		inWord[i]=0;
		wynik[i]=0;
	}
	for(int i=0; i<s.size(); i++)
	{
		inWord[s[i]-'A']++;
	}
	wynik[0]=getInWord('Z');
	removeString("ZERO", wynik[0]);
	wynik[2]=getInWord('W');
	removeString("TWO", wynik[2]);
	wynik[4]=getInWord('U');
	removeString("FOUR", wynik[4]);
	wynik[6]=getInWord('X');
	removeString("SIX", wynik[6]);
	wynik[8]=getInWord('G');
	removeString("EIGHT", wynik[8]);
	wynik[3]=getInWord('H');
	removeString("THREE", wynik[3]);
	wynik[1]=getInWord('O');
	removeString("ONE", wynik[1]);
	wynik[5]=getInWord('F');
	removeString("FIVE", wynik[5]);
	wynik[7]=getInWord('V');
	removeString("SEVEN", wynik[7]);
	wynik[9]=getInWord('I');
	removeString("NINE", wynik[9]);

	string res="";
	for(int i=0; i<10; i++)
	{
		for(int k=0; k<wynik[i]; k++)
		{
			res+=('0'+i);
		}
	}
	cout<<res<<endl;
}
int getInWord(char c)
{
	return inWord[c-'A'];
}
void removeString(string s, int times)
{
	for(int i=0; i<s.size(); i++)
	{
		inWord[s[i]-'A']-=times;
	}
}
