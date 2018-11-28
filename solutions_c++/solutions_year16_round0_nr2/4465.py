#include<fstream>
#include<iostream>
#include<string>
using namespace std;
int getN(string myString)
{
	if(myString.size()==1)return myString[0]-'0';
	if(myString.size()==2){
		int a=myString[0]-'0';
		int b=myString[1]-'0';
		return a*10+b;
	}
		if(myString.size()==3){
		int a=myString[0]-'0';
		int b=myString[1]-'0';
		int c=myString[2]-'0';
		return a*100+b*10+c;
	}
	return 0;
	
}
int main()
{
	fstream fin("B-large.in"); //打开文件
	freopen("out.txt", "w", stdout);
	string ReadLine,nstring;
	int lineCount=1;
	int n,j;
    getline(fin,nstring);
    n=getN(nstring);
	for(j=1;j<=n;j++)
	{
		int i=0;
	    int count = 0;
	    getline(fin,ReadLine);
	    if (ReadLine[0] == '-')//jump the first '-' s
	    {
	    	while (ReadLine[i] == '-')i++;
		    count = 1;
	    }  
	    while (i<ReadLine.size())
    	{
		    int ok = 0;
	     	while (i < ReadLine.size() && ReadLine[i] == '+'){ i++; ok=1; }
		    while (i < ReadLine.size() && ReadLine[i] == '-'){ i++; ok=2; }
	    	if(ok==2)count += 2;
	    }
	    std::cout << "Case #" << lineCount++ << ": "<<count<<std::endl;
	}
	fin.close();
	return 0;
}
