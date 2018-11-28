#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int N, i, l, temp;
string last;
char* lastword =  new char[1010];


int main()
{
ifstream fin;
ofstream fout;
fin.open("test.txt");
fout.open("output.txt");
fin>>N;
temp = 0;
getline(fin, last);

while(temp<N)
{
getline(fin, last);

l = last.length();



lastword[0] = last[0];



for(i=0; i<l-1; i++)
{

if(last[i+1]>=lastword[i])
	{
	if(lastword[0]<=last[i+1])
	{
for(int j=i; j>=0; j--)
	{
		lastword[j+1]=lastword[j];
	}
lastword[0]=last[i+1];
}
else 
	lastword[i+1] = last[i+1];
}
	
else 
	lastword[i+1] = last[i+1];
	
}


fout<<"Case #"<<temp+1<<": ";
for(i=0; i<l; i++)
{
fout<<lastword[i];
}

fout<<"\n";
temp++;
 }

fin.close();
fout.close();
return 0;
}
