#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <deque>
using namespace std;
string S;
//set<string>words;
//void generate(int ind, string s);

int main()
{
	
	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	long long T, ans=0;
	
	cin>>T;
	for( long long i=1; i<=T; i++){
		cin>>S;
		cout<<"Case #"<<i<<": ";
		deque<char> last;
		deque<char>::iterator it;
		last.push_back(S[0]);

		for( int k=1; k<S.length(); k++){
			int s=S[k] , l=last.front();
			if (s >= l )
				last.push_front(S[k]);
			
			else 
				last.push_back(S[k]);
		}
	
		for ( it= last.begin(); it !=last.end(); it++)
			cout<< *it;
		cout<<endl;
	}

	return 0;
}

//void generate(int ind, string s){
//  
//
//}