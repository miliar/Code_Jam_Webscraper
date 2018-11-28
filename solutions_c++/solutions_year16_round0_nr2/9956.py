#include <fstream.h>
#include <stdio.h>
#include <string.h>
int check(char []);
int main()
{
	ofstream fout("output2.txt");
	int i, j, t, k, l, count;
	char s[100], temp, first;
	cin>>t;
	for(i=0; i<t; i++)
	{
		count=0;
		gets(s);
		j=0;
		while(check(s)!=1)
		{
			count++;
			first=s[0];
			for(j=0; s[j]==first && s[j]!='\0'; j++);
			j--;
			for(l=0; l<=j; l++)
			{
				if(s[l]=='-')
					s[l]='+';
				else
					s[l]='-';
			}
			for(l=0, k=j; l<j/2; l++, k--)
			{
				temp=s[l];
				s[l]=s[k];
				s[k]=s[l];
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	fout.close();
	return 0;
}
int check(char s[])
{
	int flag=1;
	for(int i=0; s[i]!='\0'; i++)
		if(s[i]=='-')flag=0;
	return flag;
}