#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
char ch[1000];
int slno = -1;
string line;
cout<<"Input           Output ";
ifstream myfile ("//home//abhishek//Downloads//A-small-attempt1.in");
if (myfile.is_open())
{
  while ( getline (myfile,line) )
  {
	if(-1 == slno)
	{
		slno++;
		continue;
	}
	slno++;
	int size = 0;
	const char a = line[0];
	cout<<"\n"<<a<<" ";
	const char * l = &a;
	char cc = a;
	while('\0' != cc)
        {
                cc = line[size];
		if(size <= 1)
		{
			size++;
			continue;
		}
		ch[size-2] = cc;
		size++;
		cout<<cc;
        }
	int len = strlen(ch);
	int standing = 0;
	int friends = 0;
	for(int i = 0;i < len;i++)
	{
		int Si = i;
		int newFriends = 0, people = 0;
		if(0 == Si)
		{
			const char  c = ch[i];
			const char * g = &c;
			int j = atoi(g);
			standing = j;
			continue;
		}
		if(0 == standing)
		{
			newFriends = Si;
		}
		if(Si <= standing+newFriends)
		{
			const char c = ch[i];
			const char * g = &c;
			people = atoi(g);
			standing = standing+people+newFriends;
		}
		else
		{
			newFriends = Si-standing;
			const char c = ch[i];
			const char * g = &c;
			people = atoi(g);
			standing = standing + newFriends + people;
		}
		friends = friends + newFriends;
	}
	for(int k = 0;k <= (12-len);k++)
		cout<<" ";
	cout<<"  Case #"<<slno<<":"<<friends;
 }
}
return 0;
}
