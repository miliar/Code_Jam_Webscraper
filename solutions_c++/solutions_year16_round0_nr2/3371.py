#include <fstream>
#include <string>
using namespace std;

int main() {
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
	string s;
	int t,i;
	fin>>t;
	for(i=1;i<=t;i++)
	{
	    fin>>s;
	    int count=0,len=s.size();
	    if(s[len-1]=='-')
	    count=1;
	    for(int j=len-1;j>=0;j--)
	    {
	        while(j>0&&s[j]==s[j-1])
	        j--;
	        count++;
	    }
	    fout<<"Case #"<<i<<": "<<count-1<<endl;

	}
	return 0;
}
