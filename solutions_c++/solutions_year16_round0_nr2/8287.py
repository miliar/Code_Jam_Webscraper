#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
    
	ifstream in("B-large.in" , ios::in);
    ofstream out("B-large.out");
    
	int x;
	string s;
    in>>x;
    
	for(int i = 0; i < x; i++)
    {
         in >> s; 
		 	int count = 0;
		 	if (s.length()==1)
		 	{
		 		if(s[0]=='-') count = 1;
				out<<"Case #"<<i+1<<": "<<count<<endl;
        		continue;
			 }
			 for (int j = 0; j < s.length() - 1; j++)
		 	{
		 		if(s[j] != s[j+1])  count++;
			 }
		 	
		 	if(s[s.length()-1] == '-') count++;
	     	out<<"Case #"<<i+1<<": "<<count<<endl;
        		}
    return 0;
}

