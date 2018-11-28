#include<iostream>
#include<conio.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<array>
#include<fstream>
#include<sstream>

using namespace std;

ifstream myfilein;
ofstream myfileout;
string line;	
bool myfunction (long long i,long long j) { return (i>j); }

string Reverse(string s) 
{

string result=""; 

for (long long I=0; I<s.length() ; I++) 
{ 

result = s[ I ] + result ; 
}

return result;
}


void open()
  {
 	myfilein.open("test1.in");
	myfileout.open("test1.out");
  }

void open2()
  {
    freopen("test1.in", "rt", stdin);
    freopen("test1.out", "wt", stdout);
  }  
  
  
string getl()
  {
	getline(myfilein,line);
	return line;
  }

void writel()
 {
	 myfileout<<"Case #"<<": "<<endl;
 }

long long StrToInt( const std::string& s )
  {
  long long result;
  std::istringstream ss( s );
  ss >> result;
  if (!ss) throw std::invalid_argument( "StrToInt" );
  return result;
  }
  
string line1,line11;
string line2;
string line3;
int T;

long long A,B,C;
string fairs;
string square;
long long count1,digit;
double root;
std::stringstream out;

int isSquare(long long n) {
double root = sqrt(n);
if (n == (long long) n) return 1;
else return 0;
}

map<long long,int> check; 
long long res;


 void main()
	{ 
	open2();



	
	//cout<<Reverse(line); 
	cin>>T;
	for (int i = 1; i <= T; i++)
	{

		cin>>A;
		cin>>B;
		count1 = 0;
		
		check.clear();
		for (long long j = 1; j <=1000; j++)
		{
			res=j*j;
			if((res)>=A && (res)<=B)
			{
			std::stringstream out;
			out << res;
			line1 = out.str();
			line11 = string(line1.rbegin(),line1.rend());
			if (line1.compare(line11)==0)
			{
			 check.insert(pair<long long,int>(res,0));
			}
			
			}
		}


		cout<<"Case #"<<i<<": "<<check.size()<<endl;
	}


	//_getch();
	}