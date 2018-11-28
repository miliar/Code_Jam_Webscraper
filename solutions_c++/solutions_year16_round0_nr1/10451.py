#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include <string>
#include<fstream>
using namespace std;
bool all_present(vector<int> & a)
{
   for(int i=0;i<10;i++)
   {
   	if(!(find(a.begin(), a.end(), i) != a.end()))
   		return false;
   }
   return true;
}
void disection(vector<int> &a,long long int num)
{
   stringstream ss;
   string temp;
   ss<<num;
   temp = ss.str();
   ss.clear();
   int x;
   int size=temp.size();
  // cout<<"SIZE--"<<size<<endl;
 //  cout<<"temp--"<<temp<<endl;;
   for(int i=0;i<size;i++)
   {
    stringstream ss;
    ss<<temp[i];
    ss>>x;
    //cout<<x<<"%%%%%%%%%%%%%%%%"<<endl;
    a.push_back(x);
    ss.clear();
   }
}
int main()
{   ofstream outfile;
    ifstream infile;
    infile.open("A-large.in");
    outfile.open("output1.txt");
	long int test;
	infile >> test;
	for(int k=1;k<=test;k++)
	{
	long long int num;
    vector<int> a;
	infile >> num;
	if(num!=0)
	{
	int i=2;
	disection(a,num);
    while(!(all_present(a)))
    {
    //num=num*i;
       disection(a,(num*i));
       i++;
    }
      
      outfile<<"Case #"<<k<<": "<<(num*(i-1))<<endl;
	}
	else
	{
		outfile<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
	}
	}
	infile.close();
    outfile.close();
  return 0;
}