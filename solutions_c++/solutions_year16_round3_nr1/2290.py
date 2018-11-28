#include<queue>
#include<map>
#include<iostream>

using namespace std;

bool comp(const pair<int, int> &a, const pair<int, int> &b){
	return a.first - b.first;
}

int main(void) {
    /* number of test cases */
    unsigned int t;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
	priority_queue<pair<int, int> > collection;
	int n,sum=0;
	cin>>n;
	for(int j=0;j<n;j++){
		int k;
		cin>>k;
		sum += k;
		collection.push(pair<int, int>(k, j));
	}
	
	cout << "Case #" << i << ": ";
	while(sum > 0){
		pair<int, int> current = collection.top();
		char ch = current.second + 'A';
		cout<<ch;
		collection.pop();
		current.first--;
		collection.push(current);
		sum--;

		current = collection.top();
		collection.pop();
		if(current.first * 2 > sum || collection.top().first * 2 <= (sum - 1)){
			ch = current.second + 'A';
			cout<<ch;
			current.first--;
			sum--;
		}
		collection.push(current);

		cout<<" ";
	}
	cout<<"\n";
    }

    return 0;
}