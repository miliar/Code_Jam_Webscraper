// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

void sleephelper(unordered_map<int,int> mapping,int num,ofstream& writefile,int& k)
{
	int i = 0;
	int sheep;
	while(mapping.size()!=0)
	{
		sheep = (++i) * num;
		
		int tempSheep = sheep;
		while(tempSheep>0)
		{
			if(mapping.count(tempSheep%10)>0) mapping.erase(tempSheep%10);
			tempSheep/=10;
		}
	}
	writefile<<"Case #"<<k<<": "<<sheep<<endl;
}


void countSheep(vector<int>& num,ofstream& writefile)
{
	int T = num[0];
	unordered_map<int,int> templatemap;
	for(int i=0;i<=9;++i)
	{
		templatemap[i] = 1;
	}
		
	for(int i=1;i<=T;++i)
	{
		unordered_map<int,int> mapping(templatemap);
		if(num[i]==0) writefile<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
			sleephelper(mapping,num[i],writefile,i);
	}
		
}



int main ()
{
	vector<int> num;
	
  string line;
  ifstream myfile ("A-large.in.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      num.push_back(stoi(line));
    }
    myfile.close();
  }
  else cout << "Unable to open file"; 

	
  ofstream writefile ("output.txt");
  if (writefile.is_open())
  {
     countSheep(num,writefile);	
  }
	
  return 0;
}