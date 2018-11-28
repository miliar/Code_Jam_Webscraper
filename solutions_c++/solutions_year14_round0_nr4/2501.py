#include <climits>
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm> 
using namespace std;

void  testcase(int casex){
	int N;
	cin>>N;
	vector<double> naomi(N,0);
	for(int i=0; i<N; i++)
		cin>>naomi[i];	
	vector<double> ken(N,0);
	for(int i=0; i<N; i++)
		cin>>ken[i];
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	int cheat =0, nocheat=0;
	int j=N-1;
	for (int i=N-1; i>=0; i--){
		if(naomi[i]>ken[j])nocheat++;
		else j--;
	}
	
	j=0;	
	for (int i=0; i<N; i++){
		if(naomi[i]>ken[j]){cheat++; j++;}
	}
	cout << "Case #"<<casex<<": ";
	cout <<cheat<< " " <<nocheat<<endl;

}

int main()
{
	ios_base::sync_with_stdio(false);
	int cases;
	cin >> cases;
	for(int i =1; i<=cases;i++){
		testcase(i);  
	}

  return 0;
}
