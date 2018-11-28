#include<iostream>
#include<fstream>
#include<vector>
#include<cstdlib>
#include<ctime>
#include<algorithm>
using namespace std;

static const bool debug=true;
ifstream input;
ofstream output;

pair<int,int> wins(int N,bool random=false){
	bool played[N];
	double weight;
	int wCount;
	int dwCount;
	int wIndex=0;
	int dwIndex=0;

	vector<double> a;
	vector<double> b;


	//load the data from the file
	for(int i=0;i<N;++i){
		if(random)
			weight=((double)rand())/((double)RAND_MAX);
		else
			input>>weight;
		a.push_back(weight);

		played[i]=false;
	}
	for(int i=0;i<N;++i){
		if(random)
			weight=((double)rand())/((double)RAND_MAX);
		else
			input>>weight;
		b.push_back(weight);
	}

	sort(a.begin(),a.end());
	sort(b.begin(),b.end());

	if(debug)
		cout<<"weights generated\n";

	vector<double>::iterator aa=a.begin();
	dwCount=N;
	for(vector<double>::iterator bb=b.begin();bb!=b.end();++bb){
		while(aa!=a.end() && *aa<*bb){
			++aa;
			--dwCount;
		}
		if(aa==a.end())
			break;
		++aa;
	}


	//play war
	int bestMove=0;
	int lowestPlayable=0;
	double value;
	double maxValue=b[N-1];
	for(int i=0;i<N;++i){
		value=a[i];
		if(value>maxValue || bestMove==N) {
			while(played[lowestPlayable]){
				++lowestPlayable;
			}
			played[lowestPlayable]=true;
			++lowestPlayable;
			++wCount;
		} else {
			while(bestMove<N && b[bestMove]<value){
				++bestMove;
			}
			played[bestMove]=true;
			++bestMove;
		}
	}

	return make_pair(dwCount,wCount);
}

int main(){

	srand(time(0));

	input.open("4large.in");
	output.open("4large.out");

	int T;
	input>>T;

	int N;
	pair<int,int> result;

	for(int i=0;i<T;++i){
		input>>N;

		result=wins(N);

		if(debug)
			cout<<"result:\t"<<i<<"\t"<<result.first<<"\t"<<result.second<<"\n";

		output<<"Case #"<<(1+i)<<": "<<result.first<<" "<<result.second<<"\n";
	}


	input.close();
	output.close();
	return 0;


}
