#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int findMinFlip(vector<bool> cakes)
{
	int size = cakes.size();
	if(size == 0) return 0;
	bool same = cakes[0];
	int flipTimes = 0;
	for(int i=1;i<size;++i)
	{
		if(cakes[i]==same) continue;
		else
		{
			same = !same;
			flipTimes +=1;	
		}
	}
	if(same) return flipTimes;
	else return flipTimes+1;
}


int main ()
{
  vector< vector<bool> > cakes;

  int T;
  string line;

  ifstream myfile ("B-large.in.txt");
  if (myfile.is_open())
  {
	getline (myfile,line);
	T = stoi(line);
    while ( getline (myfile,line) )
    { // +-++
		int size = line.size();
		vector<bool> temp;
		for(int i=0;i<size;++i)
		{
			if(line[i]=='+')temp.push_back(1);
			else temp.push_back(0);
		}
		cakes.push_back(temp);
	}
    myfile.close();
  }
  else cout << "Unable to open file"; 

  ofstream writefile ("output.txt");
  if (writefile.is_open())
  {
	 for(int i=0;i<T;++i)
	 {
		writefile<<"Case #"<<i+1<<": "<<findMinFlip(cakes[i])<<endl;
	 }
  }
  return 0;
}