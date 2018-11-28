#include <iostream>
    #include <string>
    #include <stdlib.h>
    #include <fstream>
    #include <vector>
    #include <algorithm>
	#include <stdio.h>
	#include <stdlib.h>
	using namespace std;

	int main()
	{	
		int arr[5][5]={    {000,001,105,106,107},// 0 1 i j k
				/*1*/	   {001,001,105,106,107},
				/*i*/	   {105,105,-001,107,-106},
				/*j*/	   {106,106,-107,-001,105},
				/*k*/      {107,107,106,-105,-001}};
		//C-small-attempt0.in
		ifstream infile("C-small-attempt3.in");
		ofstream outfile("Asmall2.out");
		string temp;string::size_type sz=0;
		getline(infile,temp);
		int testcases ;
		testcases=stoi(temp,&sz,10);
		sz=0;		
		int cou=0;
		unsigned long long  L ,X; string letters;		
		long long variable=1;long long var1=1,var2=0;long long absovar=1;bool neg=false;
		bool ia=false,ja=false,ka=false;
		int countneg=0;
		while(cou<testcases)
		{
			var1=1;var2=1;variable=1;
				neg=false;
				countneg=0;
				ia=false,ja=false,ka=false;
			sz=0;
			getline(infile,temp);
			L=stoi(temp,&sz,10);
			temp=temp.substr(sz+1);
			X=stoi(temp,&sz,10);
			getline(infile,temp);
			letters=temp;
			if(letters.size()==1)
			{
				outfile<<"Case #"<<cou+1<<": "<<"NO"<<endl;
				cout<<"Case #"<<cou+1<<": "<<"NO"<<endl;
				cou++;
				continue;
			}
			for(unsigned long long i=1;i<X;i++)
			{
				letters+=temp;
			}
			if(letters.size()<3)
			{
				outfile<<"Case #"<<cou+1<<": "<<"NO"<<endl;
				cout<<"Case #"<<cou+1<<": "<<"NO"<<endl;
			}
			else if(letters.size()==3)
			{
				if(letters.at(0)=='i' && letters.at(1)=='j' && letters.at(2)=='k')
				{
					outfile<<"Case #"<<cou+1<<": "<<"YES"<<endl;
					cout<<"Case #"<<cou+1<<": "<<"YES"<<endl;
				}
				else
				{outfile<<"Case #"<<cou+1<<": "<<"NO"<<endl;cout<<"Case #"<<cou+1<<": "<<"NO"<<endl;}
			}
			
			else
			{
				var1=1;var2=1;variable=1;
				neg=false;
				countneg=0;
				variable=letters.at(0);
				if(variable==105){ia=true;letters=letters.substr(1);goto L1;variable=2;}else if(variable==106)variable=3;else if(variable==107)variable=4;
				for(unsigned long long i=1;i<letters.size();i++)
				{
					var2=0;
					var1=letters.at(i);
					if(var1==105)var1=2;else if(var1==106)var1=3;else if(var1==107)var1=4;					
					var2+=arr[variable][var1];					
					if(var2<0)
					{
						var2 = var2*-1;
						neg=true; countneg++;
					}
					if(var2==105)variable=2;else if(var2==106)variable=3;else if(var2==107)variable=4;else if(var2==1)variable=1;
					if(var2 == 105 && (countneg %2 == 0))
					{
						letters=letters.substr(i+1);
						ia=true;
						break;
					}
				}
			L1:	var1=1;var2=1;variable=1;
				neg=false;
				countneg=0;
				variable=letters.at(0);
				if(variable==105)variable=2;else if(variable==106){ja=true;letters=letters.substr(1);goto L2;variable=3;}else if(variable==107)variable=4;
				for(unsigned long long i=1;i<letters.size();i++)
				{
					var2=0;
					var1=letters.at(i);
					if(var1==105)var1=2;else if(var1==106)var1=3;else if(var1==107)var1=4;					
					var2+=arr[variable][var1];					
					if(var2<0)
					{
						var2 = var2*-1;
						neg=true; countneg++;
					}
					if(var2==105)variable=2;else if(var2==106)variable=3;else if(var2==107)variable=4;else if(var2==1)variable=1;
					if(var2 == 106 && (countneg %2 == 0))
					{
						letters=letters.substr(i+1);
						ja=true;
						break;
					}
				}
		L2:		var1=1;var2=1;variable=1;
				neg=false;
				countneg=0;
				variable=letters.at(0);
				if(variable==107  && letters.size()==1)
				{
					ka=true;
					goto L3;
				}
				if(variable==105)variable=2;else if(variable==106)variable=3;else if(variable==107)variable=4;
				for(unsigned long long i=1;i<letters.size();i++)
				{
					var2=0;
					var1=letters.at(i);
					if(var1==105)var1=2;else if(var1==106)var1=3;else if(var1==107)var1=4;					
					var2+=arr[variable][var1];					
					if(var2<0)
					{
						var2 = var2*-1;
						neg=true; countneg++;
					}
					if(var2==105)variable=2;else if(var2==106)variable=3;else if(var2==107)variable=4;else if(var2==1)variable=1;
					if(var2 == 107 && (countneg %2 == 0)&& (i==letters.size()-1))
					{						
						ka=true;					
					}
				}
			L3:	if(ia&&ja&&ka)
				{
					outfile<<"Case #"<<cou+1<<": "<<"YES"<<endl;
					cout<<"Case #"<<cou+1<<": "<<"YES"<<endl;
				}
				else
				{
					outfile<<"Case #"<<cou+1<<": "<<"NO"<<endl;
					cout<<"Case #"<<cou+1<<": "<<"NO"<<endl;
				}
			}			
			cou++;
		}
		cout<<letters.max_size()<<endl;
		system("pause");
		return 0;
	}