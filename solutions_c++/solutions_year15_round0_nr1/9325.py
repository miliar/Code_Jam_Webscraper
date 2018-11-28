#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <ctype.h>
#include <fstream>


using namespace std;

int calc(int m, string str){
	//init previous count = 0 
	int count = 0 ;
	//init added friends needed
	int needed = 0;
	//number of chars in string = m+1
	//loop over the chars and check if current index number is greater than previous count then add to needed the difference 
	// in each iteration increment count by current index 
	cout<<"============="<<endl;
	for (int i=0; i < m+1; i++){
		//cout<<"i="<<i<<endl;
		//cout<<"count="<<count<<endl;
		//cout<<"needed="<<needed<<endl;
		int new_needed = 0 ;
		if(i>count){
			needed = needed + ( i - count);
			new_needed = ( i - count);
		}
		//cout<<"str[i]"<<static_cast<int>(str[i] - '0')<<endl;
		count += static_cast<int>(str[i]  - '0');
		count += new_needed;
	}
	return needed;
}

int main(){
	string line;
	std::ifstream myfile ("A-large.in");
	int n ;
	int * output ; 
	if (myfile.is_open())
	{
		myfile>>n;
		//cout<<n<<endl;
		getline(myfile, line);
		output = new int[n];
		for(int i=0; i<n; i++){
			int m;
			string str;
			getline(myfile, line);
			stringstream ss(line);
			ss >>  m >> str ;
			//cout<< line<<endl;
			//cout<< m <<", "<<str<<endl;
			output[i] = calc(m,str);
			//cout<<output[i]<<endl;
		}
		myfile.close();
	}
	
	
	else cout << "Unable to open file"; 
	
	ofstream myfile2;
	myfile2.open ("A-large.out");
	for(int i=0; i<n; i++){
		myfile2 << "Case #"<<i+1<<": "<<output[i]<<"\n";
	}
	myfile2.close();
	

	return 0;
}