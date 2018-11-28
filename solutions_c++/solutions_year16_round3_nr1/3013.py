#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

void generateSets(int n, vector<vector<int> > &sets)
{
	vector<int> arr(n);
	for(int i = 0; i < n; ++i)
		arr[i] = i+1;
	sets.push_back(arr);
	while(next_permutation(arr.begin(), arr.end())){
		sets.push_back(arr);
	}
	// for(int i = 0; i < sets.size(); ++i){
	// 	for(int j = 0; j < n; ++j)
	// 		cout << sets[i][j] << " ";
	// 	cout << endl;
	// }
}

int evacuate(int i, int j, vector<int> ppl, int n)
{
	ppl[i]--;
	if(j != -1)
		ppl[j]--;
	int sum = 0;
	for(int i = 0; i < ppl.size(); ++i)
		sum += ppl[i];
	for(int i = 0; i < ppl.size(); ++i)
	{
		if(ppl[i]*2 > sum)
			return 0;
	}
	return 1;
}

string getAns(int n, vector<vector<int> > &sets, vector<int> &ppl)
{
	vector<int> ppl2(ppl);
	for(int i = 1; i < ppl.size(); ++i)
		ppl2[i] += ppl2[i-1];
	// cout << "PPL2: ";
	// for(int i = 0; i < ppl2.size(); ++i)
	// 	cout << ppl2[i] << " ";
	// cout << endl;
	string lol;
	for(int i = 0; i < sets.size(); ++i){
		vector<int> &curr = sets[i], ppl3(ppl);
		// cout << "Current set: ";
		// for(int k = 0; k < curr.size(); ++k)
		// 	cout << curr[k] << " ";
		// cout << endl;
		int j = 0, flag = 1;
		string res;
		while(j < curr.size()){
			// cout << "Current PPL: ";
			// for(int k = 0; k < ppl3.size(); ++k)
			// 	cout << ppl3[k] << " ";
			// cout << endl;
			auto it1 = lower_bound(ppl2.begin(), ppl2.end(), curr[j]);
			// cout << "j=" << j << "  j = " << curr[j] << " it1 = " << it1 - ppl2.begin() << endl;
			auto it2 = ppl2.end();
			if(j != curr.size()-1){
				// cout << " j+1 = " << curr[j+1] <<endl;
				it2 = lower_bound(ppl2.begin(), ppl2.end(), curr[j+1]);
				// cout << " it2 = " << it2 - ppl2.begin() << endl;
			}
			if(j != curr.size()-1 && evacuate(it1-ppl2.begin(),it2-ppl2.begin(),ppl3,n)){		
				ppl3[it1-ppl2.begin()]--;
				ppl3[it2-ppl2.begin()]--;
				j += 2;
				char c1 = 'A' + (it1-ppl2.begin());
				// cout << "fnd = " << c1 ;
				char c2 = 'A' + (it2-ppl2.begin());
				// cout << " fnd = " << c2 << endl;
				res += c1;
				res += c2;
				res += ' ';
				// cout << res << endl;

			}
			else if(evacuate(it1-ppl2.begin(),-1,ppl3,n)){
				ppl3[it1-ppl2.begin()]--;
				++j;
				char c1 = 'A' + (it1-ppl2.begin());
				// cout << "fnd = " << c1 <<endl;
				res += c1;
				res += ' ';
				// cout << res << endl;
			}
			else{
				flag = 0;
				break;
			}
		}
		if(flag == 1){
			return res;
		}
	}
	return lol;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		int N;
		cin >> N;
		vector<int> ppl(N);
		int total = 0;
		for(int i = 0; i < N; ++i){
			cin >> ppl[i];
			total += ppl[i];
		}
		vector<vector<int> > sets;
		generateSets(total,sets);
		cout << "Case #" << t<< ": " << getAns(N,sets,ppl) << endl; 
	}
	return 0;
}