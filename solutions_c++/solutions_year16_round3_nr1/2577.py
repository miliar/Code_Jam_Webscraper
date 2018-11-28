// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue> 

using namespace std;

struct Party
{
	int people; 
	char p; 
	Party(int num,char _p):people(num),p(_p){}
};

struct mycomparsion
{
        bool operator()(Party l,Party r)
        {
            return l.people < r.people;
        }
};

bool verify(vector<int>& p,int sum)
{
	for(int i = 0;i<p.size();++i)
	{
		if(p[i]>sum/2) return false;
	}
	return true;	
}

string escape(vector<int> p)
{
	priority_queue<Party,vector<Party>,mycomparsion> heap;
	
	int N = p.size(),sum = 0;
	for(int i=0;i<N;++i)
	{
		sum+= p[i];
		Party _p(p[i],i+'A');
		heap.push(_p);
	}
	
	string res; 
	while(heap.size()!=0)
	{
		string temp;
		temp.push_back(heap.top().p);
		
		Party first = heap.top();
		first.people -= 1; 
		p[first.p-'A'] -= 1;
		sum -= 1;
		
		if(first.people > 0)
		{
			heap.pop();
			heap.push(first);
		}
		else heap.pop();
		
		
		if(!verify(p,sum))
		{
			temp.push_back(heap.top().p);
			Party second = heap.top();
			second.people -= 1; 
			p[second.p-'A'] -= 1;
			sum -= 1;
					
			
			if(second.people != 0)
			{
				heap.pop();
				heap.push(second);
			}
			else heap.pop();
		}
		temp+=" ";
		res += temp;
	}
	//cout<<res<<endl;
	return res;
}


int main ()
{
 
  int T;
  vector<string> res;

  string line;
  ifstream myfile ("A-large.in.txt");
  if (myfile.is_open())
  {
	myfile>>T;
	
	int N;
	for(int i=0;i<T;++i)
	{
		myfile>>N;
		vector<int> p;
		for(int j=0;j<N;++j)
		{
			int num;
			myfile>>num;
			p.push_back(num);
		}
		res.push_back(escape(p));
		//cout<<escape(p)<<endl;
		//for(int x:p) cout<<x<<' ';
		//cout<<endl;
		
	}
    myfile.close();
  }
  else cout << "Unable to open file"; 

	
  ofstream writefile ("output.txt");
  if (writefile.is_open())
  {
    for(int i=0;i<T;++i)
	 {
		writefile<<"Case #"<<i+1<<": "<<res[i]<<endl;
	 }
  }
	
  return 0;
}