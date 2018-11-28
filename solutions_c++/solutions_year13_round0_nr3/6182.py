#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>
#include <math.h>


using namespace std;
int a,b;

bool palindrome(int x){
	string s = std::to_string((long double)x);
	for(int i=0;i<s.size();i++){
		if(s[i]!=s[s.size()-i-1])
			return false;
	}
	return true;
}

void main()
{
	string line;
	std::freopen("output_C.txt", "w", stdout);
	ifstream file("C-small-attempt0.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	
	int count;
	file>>count;
		
	for(int i=0;i<count;i++)
	{	
		int count=0;
		printf("Case #%d: ",i+1);
		file>>a;
		file>>b;

		for(int j=a;j<=b;j++){
			if(palindrome(j)){
				float x=sqrt((float)j);
				if(x-(int)x==0){
					if(palindrome((int) x))
						count++;
				}
			}
		}
		
		cout<<count<<endl;
		
	}
	
}