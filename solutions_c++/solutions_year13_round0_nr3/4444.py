#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
#include<map>
#include<queue>
#include<utility>
#include<string>
#include<sstream>
#include<cmath>

using namespace std;

#define tr(c, it) \
        for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

int check_palindrome(int num)
{
	ostringstream ost;
	ost << num;
	string s =  ost.str();

	int i = 0;
	int j = s.length()-1;

	while(i<=j){
		if(s[i] != s[j]) return 0;
		i++;
		j--;
	}

	return 1;		
}

int find_cnt(int s, int e){

	int cnt = 0;
	for(int i = s; i <= e; i++)
	{
		if(check_palindrome(i)){

			float val = sqrt(i);
			if(int(val) == val){
				
				if(check_palindrome(int(val))){
					cnt++;
				}
			}			

		}	
	}	

	return cnt;	

}

int main()
{	
	int N;
	cin >> N;

	for(int i = 0; i < N; i++){

		int s,e;
		cin >> s >> e;

		int count = find_cnt(s,e);	
	
		cout << "Case #" << i+1 << ": " << count << endl;

	}

	return 0;
}
