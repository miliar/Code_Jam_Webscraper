#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>
#include <set>
#include "gsearch.hpp"

using namespace std;

#define LIMIT 21

vector<vector<int> > chestByKey;
vector<int> startKeys;
vector<int> T;
vector<int> keysLost;


int N;
vector<vector<int> > K;
class State{
public:
    vector<int> chestList;
    vector<int> keyList;
    vector<int> availableKeys;
    vector<int> neededKeys;
    void Initialize(const vector<int> &startKeys){
	neededKeys.clear();
	availableKeys.clear();
	keysLost.clear();
	neededKeys.resize(LIMIT);
	availableKeys.resize(LIMIT);
	keyList = startKeys;
	keysLost.resize(N);
	for(int i = 0; i < LIMIT; i++)
	    availableKeys[i]=neededKeys[0] = 0;
	for(int i = 0; i < N; i++){
	    neededKeys[T[i]]++;
	    for(int j = 0; j < K[i].size(); j++){
		availableKeys[K[i][j]]++;
	    }
	}
	for(int i = 0; i< startKeys.size(); i++)
	    availableKeys[startKeys[i]]++;
	for(int i =0 ; i < N; i++){
	    keysLost[i]=-1;
	    for(int j =0; j <K[i].size(); j++){
		if(K[i][j]==T[i])
		    keysLost[i]++;
	    }
	}
    }

    void print(){
	cout <<"State\n";
	cout << "Chest List : " << chestList.size() << ": ";
	for(int i =0 ; i < chestList.size(); i++){
	    cout << chestList[i]+1 << " ";
	}
	cout <<endl;
	cout << "Key List: " ;
	for(int i=0; i<keyList.size(); i++){
	    cout << keyList[i] << " ";
	}
	cout <<endl;
    }

    bool IsValid(){
        for(int i = 0; i < LIMIT; i++){
	    if(availableKeys[i]<neededKeys[i])
		return false;
	}
	return true;
    }
    
    void MakeChildren(Stack<State> &childrenList) const{
	State child;
	set<int> used;

	for(int i =0; i < chestList.size(); i++)
	    used.insert(chestList[i]);
	for(int i = 0; i < keyList.size(); i++){
	    for(int j = 0; j < chestByKey[keyList[i]].size(); j++){
		int tmp = chestByKey[keyList[i]][j];
		if(used.find(tmp)!=used.end()){
		    continue;
		}
		else
		    used.insert(tmp);
		// int cnt1 = 0;
		// for(int k = 0; k < keyList.size(); k++){
		//     if(keyList[k]== T[tmp])
		// 	cnt1++;
		// }
		// int  cnt2 = 0;
		// for(int k = 0; k < N; k++){
		//     if(T[k]==T[tmp] && used.find(k)==used.end()){
		// 	cnt2=1;
		// 	break;
		//     }
		// }
		// if(cnt1<=1 && cnt2==1 && keysLost[tmp]==-1 && j < chestByKey[keyList[i]].size()-1)
		//     continue;

		int cnt0=0, cnt1=0;
		
		for(int k = 0; k < keyList.size(); k++){
		     if(keyList[k]== T[tmp])
		 	cnt0++;
		}

		if(cnt0==1   &&neededKeys[T[tmp]]>1){
		    for(int k = 0; k < N; k++){
			if(used.find(k)==used.end() && T[k] == T[tmp]){
			    cnt1+=keysLost[k]+1;
			}
		    }
		    
		    if(cnt1==availableKeys[T[tmp]]-1){
//			getchar();
			continue;
		    }
		}

		child = *this;
		child.availableKeys[T[tmp]]--;
		child.neededKeys[T[tmp]]--;
		child.chestList.push_back(tmp);
		child.keyList.erase(child.keyList.begin()+i);
		for(int i = 0; i< K[tmp].size(); i++){
		    child.keyList.push_back(K[tmp][i]);
		    child.availableKeys[K[tmp][i]]++;
		}
		childrenList.push(child);
	    }
	    
	}
    }

    bool IsGoal(){
	return chestList.size()==N;
    }

    class CompareByState{
    public:
	bool operator()(const State &a, const State &b){
	    int m = min(a.chestList.size(), b.chestList.size());
	    int i;
	    for( i=0; i < m; i++){
		if(a.chestList[i]<b.chestList[i])
		    return true;
		else if(a.chestList[i]>b.chestList[i])
		    return false;
	    }
	    if(a.chestList.size()<b.chestList.size())
		return true;
	    else 
		return false;
	}
    };

    class CompareByCost{
    public:
	bool operator()(const State &a, const State &b){
	    int m = min(a.chestList.size(), b.chestList.size());
	    int i;
	    for( i=0; i < m; i++){
		if(a.chestList[i]<b.chestList[i])
		    return false;
		else if(a.chestList[i]>b.chestList[i])
		    return true;
	    }
	    if(a.chestList.size()<b.chestList.size())
		return false;
	    else 
		return true;
	}
    };


};

int main(int argc, char **argv){
    string inputFileName(argv[1]);
    string outputFileName(argv[2]);

    ifstream input(inputFileName.c_str());
    ofstream output(outputFileName.c_str());

    int numTest;
    input >> numTest;

    chestByKey.resize(LIMIT);
    for(int t = 0; t < numTest; t++){
	int numStartKeys;
	/* Input*/
	input >> numStartKeys;
	input >> N;
	startKeys.resize(numStartKeys);
	cout << numStartKeys << " " << N <<endl;
	T.resize(N);
	K.resize(N);
	for(int i =0; i < LIMIT; i++){
	    chestByKey[i].clear();
	}
	for(int i =0; i<numStartKeys; i++){

	    input >> startKeys[i];
	    cout << startKeys[i] << " ";
	}
	cout <<endl;
	for(int i =0; i<N; i++){
	    int tmp;
	    input >> T[i];
	    chestByKey[T[i]].push_back(i);
	    input >> tmp;
	    cout << T[i] << " " <<tmp << " ";
	    K[i].resize(tmp);
	    for(int j =0; j<tmp; j++){
		input >> K[i][j];
		cout << K[i][j] << " ";
	    }
	    cout <<endl;
	}

	State initial;
	initial.Initialize(startKeys);

	Stack<State> childrenList;
	initial.MakeChildren(childrenList);

	Gsearch<State, PQ<State, State::CompareByCost> > afs;
	afs.Type = ASTAR;
	State solution;
	if(initial.IsValid()){
	    solution = afs(initial);
	}
	else{
	    cout << " NOT valied " <<endl;
	}
	output << "Case #" << t+1<<": ";
	if(solution.chestList.empty())
	    output << "IMPOSSIBLE" <<endl;
	else{
	    for(int i =0; i<N; i++){
		output<<solution.chestList[i]+1;
		if(i<N-1)
		    output << " ";
	    }
	    output << endl;
	}
	cout << "-------------------------------------------" <<endl;
	cout <<endl;
    }
    
    return 0;
}
