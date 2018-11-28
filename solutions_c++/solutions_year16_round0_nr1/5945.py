#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;
int freq[10];
string curr="INSOMNIA";
template <typename T>
string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
bool seen()
{
	for(int i=0;i<10;i++){
	if(freq[i]==0)
		return false;
	}
	return true;

}
void enter(string N)
{

	for(int l=0;N[l]!='\0';l++)
	{
		freq[(N[l] - '0')]++;
		
	}

}
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int tc;
	fin>>tc;
	string N;
	int cur=1;
	int con;
	
	for(int i=0;i<10;i++)
	{
		freq[i]=0;
	}
	for(int i=0;i<tc;i++)
	{
		fin>>N;
		curr=N;
		con=stoi(N);
		for(int j=0;j<10;j++)
		{
			freq[j]=0;
		}
		cur=0;
		while(!seen()&&stoi(N)!=0)
		{
			enter(curr);
			if(seen())
				break;
			cur++;
			curr=NumberToString(cur*con);
		
		}
		if(stoi(N)==0)
		{
		curr="INSOMNIA";
		}
		fout<<"Case #"<<i+1<<": "<<curr<<endl;
	}

return 0;
}