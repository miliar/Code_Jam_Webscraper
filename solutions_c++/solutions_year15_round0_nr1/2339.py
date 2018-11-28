#include<iostream>
#include<string.h>
using namespace std;
main()
{
    int t,len,i,j,count,testcase,invitefriends,totalfriends;
	int aint[1050];
	char achar[1050];
	cin>>t;
	testcase=1;
	while(t--)
	{
		invitefriends=0;
		totalfriends=0;
		cin>>len;
		len=len+1;
		cin>>achar;
		for(i=0;i<len;i++)
		{
			if(achar[i]=='0')
			aint[i]=0;
			else if(achar[i]=='1')
			aint[i]=1;
			else if(achar[i]=='2')
			aint[i]=2;
			else if(achar[i]=='3')
			aint[i]=3;
			else if(achar[i]=='4')
			aint[i]=4;
			else if(achar[i]=='5')
			aint[i]=5;
			else if(achar[i]=='6')
			aint[i]=6;
			else if(achar[i]=='7')
			aint[i]=7;
			else if(achar[i]=='8')
			aint[i]=8;
			else if(achar[i]=='9')
			aint[i]=9;
		}
		for(i=0;i<len;i++)
		{
			if(i==0 && aint[0]==0)
			{
				invitefriends++;
			}
			if(i>0)
			{
				totalfriends=0;
				for(j=0;j<i;j++)
				totalfriends=totalfriends+aint[j];
				totalfriends=totalfriends+invitefriends;
				if(totalfriends<i)
				invitefriends++;
			}
		}
		cout<<"Case #"<<testcase<<": "<<invitefriends<<endl;
		testcase++;
	}
}
		
