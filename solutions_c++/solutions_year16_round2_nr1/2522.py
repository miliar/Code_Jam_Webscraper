#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

string s;
int len=0;
int cnt_arr[26];
int sec_arr[26];
int main()
{
	int t;
	scanf("%d",&t);
	int case1=1;
	while(t--)
	{
		cin>>s;
		len =s.length();
		//memset(cnt_arr,0,sizeof(cnt_arr[0])*25);
		cout<<"Case #"<<case1<<": ";
		case1++;
		for(int i=0;i<26;i++)
		{
			cnt_arr[i]=0;
			sec_arr[i]=0;
		}
		for(int i=0;i<len;i++)
		{
			cnt_arr[s[i]-'A']++;
		}
		for(int i=0;i<26;i++)
		{
			sec_arr[i]=cnt_arr[i];
		}
		//cout<<" o count "<<cnt_arr['O'-'A']<<endl;
		cnt_arr['O'-'A']-=(cnt_arr['W'-'A']+cnt_arr['U'-'A']+cnt_arr['Z'-'A']);
		//cout<<" recheck "<<cnt_arr['O'-'A']<<endl;
		cnt_arr['F'-'A']-=cnt_arr['U'-'A'];
		int temp3 = cnt_arr['S'-'A'] - cnt_arr['X'-'A'];
		int temp5 = cnt_arr['H'-'A']-cnt_arr['G'-'A'];
		int sum=0;
		for(int i=0;i<sec_arr['Z'-'A'];i++)
		{
			sum+=4;
			cout<<0;
		}
		for(int i=0;i<cnt_arr['O'-'A'];i++)
		{
			sum+=3;
			cout<<1;
		}
		for(int i=0;i<sec_arr['W'-'A'];i++)
		{
			sum+=3;
			cout<<2;
		}
		for(int i=0;i<temp5;i++)
		{
			sum+=5;
			cout<<3;
		}
		for(int i=0;i<sec_arr['U'-'A'];i++)
		{
			sum+=4;
			cout<<4;
		}
		for(int i=0;i<cnt_arr['F'-'A'];i++)
		{
			sum+=4;
			cout<<5;
		}
		for(int i=0;i<sec_arr['X'-'A'];i++)
		{
			sum+=3;
			cout<<6;
		}
		for(int i=0;i<temp3;i++)
		{
			sum+=5;
			cout<<7;
		}
		for(int i=0;i<sec_arr['G'-'A'];i++)
		{
			sum+=5;
			cout<<8;
		}
		int temp4 = (len -sum)/4;
		for(int i=0;i<temp4;i++)
		{
			cout<<9;
		}
		cout<<endl;
	}
}