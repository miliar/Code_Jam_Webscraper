#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define DEBUG 0

int letter_freq (int freq[26], char letter)
{
	return freq[letter-'A'];
}

/*
int string_freq (int freq[26], string str)
{
	int str_freq=letter_freq(freq,str[0]);
	for (int i=1; i<str.length(); i++)
	{
		str_freq=min(str_freq, letter_freq(freq,str[i]));
	}
	for (int i=0; i<str.length(); i++)
	{
		freq[str[i]-'A']-=str_freq;
	}
	return str_freq;
}
*/

int string_freq (int freq[26], string str)
{
	int freq_copy[26];
	for (int i=0; i<26;i++)
		freq_copy[i]=freq[i];
	int count = 0;
	bool flag=true;
	while (flag)
	{
		for (int i=0; i<str.length(); i++)
		{
			freq_copy[str[i]-'A']--;
			if (freq_copy[str[i]-'A']<0)
			{
				flag=false;
				count--;
				break;
			}
		}
		count++;
	}
	for (int i=0; i<str.length(); i++)
	{
		freq[str[i]-'A']-=count;
	}
	//cout << count << " " << str << endl;
	return count;
}

int find_digit (int freq[26], char digit)
{
	/*
	for (int i=0; i<26; i++)
		cout << (char)(i+'A') << ": " << freq[i] << endl;
	*/

	int digit_freq;
	switch (digit)
	{
		case '0': digit_freq=string_freq(freq,"ZERO"); break;
                case '2': digit_freq=string_freq(freq,"TWO"); break;
                case '4': digit_freq=string_freq(freq,"FOUR"); break;
                case '6': digit_freq=string_freq(freq,"SIX"); break;
                case '8': digit_freq=string_freq(freq,"EIGHT"); break;

                case '1': digit_freq=string_freq(freq,"ONE"); break;
                case '3': digit_freq=string_freq(freq,"THREE"); break;
                case '5': digit_freq=string_freq(freq,"FIVE"); break;
                case '7': digit_freq=string_freq(freq,"SEVEN"); break;
                case '9': digit_freq=string_freq(freq,"NINE"); break;
	}
	return digit_freq;
}

string find_numbers (string s, char start)
{
        int freq[26]={0};
        for (int i=0; i<s.length(); i++)
        {
                int index=s[i]-'A';
                if (index>=0 && index<=25)
                        freq[index]++;
        }

	string answer;
	for (char i='0'; i<='8'; i+=2)
	{
		//if (i!=start)
		//{
		int digit_freq=find_digit(freq,i);
		for (int j=0; j<digit_freq; j++)
			answer+=i;
		//}
	}
	for (char i='1'; i<='9'; i+=2)
	{
		int digit_freq=find_digit(freq,i);
                for (int j=0; j<digit_freq; j++)
                        answer+=i;
	}
	return answer;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; i++)
	{
		string s;
		cin >> s;
		printf ("Case #%d: ", i+1);
		string ss=find_numbers(s,i).c_str();
		sort(ss.begin(),ss.end());
		printf ("%s\n", ss.c_str());
		/*	
		string ss;	
		for (char k='/'; k<='9'; k++)
		{
		ss=find_numbers(s,k);	
		string sss;
		for (int j=0; j<ss.length(); j++)
		{
			switch(ss[j])
			{
				case '0': sss+="ZERO"; break;
                                case '1': sss+="ONE"; break;
                                case '2': sss+="TWO"; break;
                                case '3': sss+="THREE"; break;
                                case '4': sss+="FOUR"; break;
                                case '5': sss+="FIVE"; break;
                                case '6': sss+="SIX"; break;
                                case '7': sss+="SEVEN"; break;
                                case '8': sss+="EIGHT"; break;
                                case '9': sss+="NINE"; break;

			}
		}
		//sort(sss.begin(), sss.end());
		//cout << s.length() << " " << sss.length() << endl;
		if (s.length()==sss.length())
			break;
		}
		printf ("%s\n", ss.c_str());
		*/
	}
}
