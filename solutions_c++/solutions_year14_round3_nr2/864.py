#include <climits>
#include <iostream>
#include <vector>

using namespace std;

long int fact(int k){
	int res =1;
	for (int i=1; i<=k; i++ )
		res =res* i%1000000007;
	return res;
}

void  testcase(long int casex){
	int N;
	cin >>N;
	
	vector<string> sets(N);
	for(int i=0; i<N; i++)
		cin >>sets[i];
	
	vector<pair <int, int> > begends(26, pair <int, int>(-1,-1));
	vector<vector<int> > ismadeof(26);
	bool hasToBeAlone[26];
	for(int i=0; i<26; i++) hasToBeAlone[i]= false;
	
	bool ok = true;
	for(int i=0; i<N; i++){
		bool same = true;
		int last = sets[i][0]-'a';
		for(int j=1; j<sets[i].length(); j++){
			int c = sets[i][j]-'a';
			if( c!= last){
				if (same == false){
					if(hasToBeAlone[last] || begends[last].first !=-1|| begends[last].second != -1 || ismadeof[last].size() !=0) ok = false;
					hasToBeAlone[last] = true;
				}
				same = false;
				last = c;
			}

		}
		if(same) ismadeof[last].push_back(i);
		else{
			if(begends[sets[i][0]-'a'].first !=-1) ok = false;
			else begends[sets[i][0]-'a'].first =i;
			if(begends[last].second !=-1) ok = false;
			else begends[last].second =i;
			if(sets[i][0]-'a' == last) ok = false;
		}
		
		//cout << begends[2].second<< endl;
	}
	if(!ok){	cout << "Case #"<<casex<<": 0"<<endl; return;}
	
	long int ways =1;
	int indep=0;
	for(int i=0; i<26; i++){
		if(begends[i].first == -1 && begends[i].second==-1 && ismadeof[i].size() == 0) continue;
		if(begends[i].second == -1) indep++;
		ways = ways*fact(ismadeof[i].size()) %1000000007;
		//cout << 	ismadeof[i].size()<< ' '<<ways <<endl;
	}
	ways = ways*fact(indep) %1000000007;
	//cout << indep <<endl;
	if(indep ==0){	cout << "Case #"<<casex<<": 0"<<endl; return;}
	else{
		cout << "Case #"<<casex<<": "<<ways<<endl; 
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	long int cases;
	cin >> cases;
	for(long int i =1; i<=cases;i++){
		testcase(i);  
	}

  return 0;
}
