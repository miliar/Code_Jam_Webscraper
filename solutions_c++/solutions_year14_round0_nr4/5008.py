/*
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <fstream>//for writing in files
#include <cctype>
#include <stdlib.h>
#include <iomanip>

using namespace std;


string NumberToString (int Number)
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
int StringToNumber (string Text)
{                              
	stringstream ss(Text);
	int result;
	return ss >> result ? result : 0;
}
bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}
bool isPalindrom(unsigned long long n)
{
	string number=NumberToString(n);
	int lenght=number.size();
	bool check=true;
	for(int i=0;i<lenght;i++)
	{
		if(number[i]==number[lenght-i-1] && check==true)
		{
			check=true;
		}
		else
		{
			check=false;
		}
	}
	return check;
}
int main()
{
	//freopen("B-large.in","r",stdin); // For reading input
    //freopen("solution.out","w",stdout);
	int n;
	double F;double c,f,x,t1,t2,time,cookies;bool finish=false;
	time=0;t2=0;t1=0;cookies=0;F=2.00000;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		finish=false;
		time=0.00000;t2=0.00000;t1=0.00000;cookies=0;F=2.00000;
		cin>>c>>f>>x;
	//	cout<<c<<" "<<f<<" "<<x<<endl;
		while(!finish)
		{
			t1=x/F;
			t2=(c/F)+(x/(F+f));
			if(t1>t2)
			{
				time+=c/F;
				F+=f;
			}
			else
			{
				time+=t1;
				finish=true;
			}
		}
		cout<<"Case #"<<i+1<<": "<< std::fixed << std::setprecision(7)<<time<<endl;
		//std::cout << std::fixed << std::setprecision(7) << a;
	}
	
	return 0;
}
*/

#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <fstream>//for writing in files
#include <cctype>
#include <stdlib.h>
#include <iomanip>
#include <algorithm>

using namespace std;


string NumberToString (int Number)
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
int StringToNumber (string Text)
{                              
	stringstream ss(Text);
	int result;
	return ss >> result ? result : 0;
}
bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}
bool isPalindrom(unsigned long long n)
{
	string number=NumberToString(n);
	int lenght=number.size();
	bool check=true;
	for(int i=0;i<lenght;i++)
	{
		if(number[i]==number[lenght-i-1] && check==true)
		{
			check=true;
		}
		else
		{
			check=false;
		}
	}
	return check;
}
int min(double n,vector<double> A)
{
	int num=0;int index=100;
	for(int i=0;i<A.size();i++)
	{
		if(n>A[i])
		{
			if(A[i]>num){num=A[i];index=i;}
		}
	}
	return index;
}
int solve(vector<double> A,vector<double> B,int n,int Score)
		{
			if(!A.empty())
			{
				for(int z=0;z<n;z++)
				{
					for(int m=0;m<n;m++)
					{
						if(B[z]>A[m])
						{
							Score++;
							//for(int i=0;i<A.size();i++)
							//{
							//	cout<<A[i]<<"  "<<B[i]<<endl;
							//}
						//	cout<<"_______"<<endl;
							A.erase(A.begin()+m);
							B.erase(B.begin()+z);
							n--;
							sort(A.begin(), A.end());
							sort(B.begin(), B.end());
							return solve(A,B,n,Score);
						}
						
					}
			
				}
				return Score;
			}
			else{return Score;}
			
		}
int cheat(vector<double> A,vector<double> B,int n,int Score)
		{
			if(!A.empty())
			{
				
				for(int z=0;z<n;z++)
				{
					//cout<<Score<<endl;
						if(min(A[z],B)!=100)
						{
							
							int m=min(A[z],B);
							Score++;
							//for(int i=0;i<A.size();i++)
							//{
							//	cout<<A[i]<<"  "<<B[i]<<endl;
							//}
							//cout<<"_______"<<endl;
							B.erase(B.begin()+m);
							A.erase(A.begin()+z);
							n--;
							sort(A.begin(), A.end());
							sort(B.rbegin(), B.rend());
							return cheat(A,B,n,Score);

						}
			
				}
				
				return Score;
			}
			else{return Score;}
			
		}
int main()
{
	freopen("D-small-attempt1.in","r",stdin); // For reading input
    freopen("solution.out","w",stdout);
	int n,nScore,kScore,nCheatScore,fs;
	int Stones;
	double naomi,ken;
	vector<double> N,K;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		nScore=0;
		kScore=0;
		Stones=0;
		N.clear();
		K.clear();
		cin>>Stones;
		fs=Stones;
		for(int s=0;s<Stones;s++)
		{
			cin>>naomi;
			N.push_back(naomi);
		}
		for(int s=0;s<Stones;s++)
		{
			cin>>ken;
			K.push_back(ken);
		}
		sort(N.begin(), N.end());
		sort(K.begin(), K.end());
		nScore=Stones-solve(N,K,fs,kScore);
		//sort(N.rbegin(), N.rend());
		sort(N.rbegin(), N.rend());
		nCheatScore=cheat(N,K,fs,0);
		cout<<"Case #"<<i+1<<": "<<nCheatScore<<" "<<nScore<<endl;
	}

	
	
    

    
	return 0;
}
