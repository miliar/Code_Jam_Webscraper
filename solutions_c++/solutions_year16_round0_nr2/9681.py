#include<iostream>
#include<fstream>
using namespace std;

int main(){
    int tc;

    ifstream inputfile("B-large.in");
    ofstream outputfile("output.txt");
    inputfile>>tc;
    long long val;
    long long ans;
    int l;
    for(int index = 1; index <= tc; index++){

   		ans = 0;
   		string str;
        inputfile>>str;
		l=str.length();

		for(int i = 1;i < l; i++)
			if(str[i]!=str[i-1])
                ans++;
		if(str[l-1]=='-')
            ans++;
		outputfile<<"Case #"<<index<<": "<<ans<<endl;
    }
    inputfile.close();
    outputfile.close();
    return 0;
}

