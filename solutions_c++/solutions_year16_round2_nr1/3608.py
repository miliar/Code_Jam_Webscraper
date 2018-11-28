#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main()
{
	int t,k=1;
	cin>>t;
	while(t--)
	{
		unordered_map<char, int> hashtable;
		hashtable.emplace('Z', 0);
		hashtable.emplace('E', 0);
		hashtable.emplace('R', 0);
		hashtable.emplace('O', 0);
		hashtable.emplace('N', 0);
		hashtable.emplace('T', 0);
		hashtable.emplace('W', 0);
		hashtable.emplace('H', 0);
		hashtable.emplace('F', 0);
		hashtable.emplace('U', 0);
		hashtable.emplace('I', 0);
		hashtable.emplace('V', 0);
		hashtable.emplace('S', 0);
		hashtable.emplace('X', 0);
		hashtable.emplace('G', 0);
		string phone;
		cin>>phone;
		int i, j;
		int number[10];
		for(i=0;i<10;i++)
			number[i]=0;
		for(i=0;i<phone.size();i++)
		{
			hashtable[phone[i]]++;
		}
		while(hashtable['Z'])
		{
			number[0]++;
			hashtable['Z']--;
			hashtable['E']--;
			hashtable['R']--;
			hashtable['O']--;
		}
		while(hashtable['G'])
		{
			number[8]++;
			hashtable['E']--;
			hashtable['I']--;
			hashtable['G']--;
			hashtable['H']--;
			hashtable['T']--;
		}
		while(hashtable['X'])
		{
			number[6]++;
			hashtable['S']--;
			hashtable['I']--;
			hashtable['X']--;
		}
		while(hashtable['W'])
		{
			number[2]++;
			hashtable['T']--;
			hashtable['W']--;
			hashtable['O']--;
		}
		while(hashtable['S'])
		{
			number[7]++;
			hashtable['S']--;
			hashtable['E']--;
			hashtable['V']--;
			hashtable['E']--;
			hashtable['N']--;
		}
		while(hashtable['V'])
		{
			number[5]++;
			hashtable['F']--;
			hashtable['I']--;
			hashtable['V']--;
			hashtable['E']--;
		}
		while(hashtable['I'])
		{
			number[9]++;
			hashtable['N']--;
			hashtable['I']--;
			hashtable['N']--;
			hashtable['E']--;
		}
		while(hashtable['F'])
		{
			number[4]++;
			hashtable['F']--;
			hashtable['O']--;
			hashtable['U']--;
			hashtable['R']--;
		}
		while(hashtable['O'])
		{
			number[1]++;
			hashtable['O']--;
			hashtable['N']--;
			hashtable['E']--;
		}
		while(hashtable['T'])
		{
			number[3]++;
			hashtable['T']--;
			hashtable['H']--;
			hashtable['R']--;
			hashtable['E']--;
			hashtable['E']--;
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<10;i++)
		{
			for(j=0;j<number[i];j++)
				cout<<i;
		}
		cout <<endl;
		k++;
	}
	
	return 0;
}