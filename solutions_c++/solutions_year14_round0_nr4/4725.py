
#include <iostream>
#include <algorithm>
using namespace std;
float  klist[1000];
float mylist[1000];

int greedy(int N){
int score=0;	
std::sort(klist, klist + N);
std::sort(mylist, mylist + N);
	
for(int i=0;i<N;i++){
	float x=mylist[i];
	//iterate over the list klist and find the lowest item 
	int found = -1;
	for(int j=0;j<N;j++){
		if(klist[j]>x) {found =j; break;}
	}
	if(found>=0){
		klist[found]=-klist[found];
	} else {
		score++;
	}

}
return score;
}

int cheat_greedy(int N){
int score=0;	
for(int i=0;i<N;i++){
if( mylist[i] < 0)mylist[i]=-mylist[i];
if( klist[i] < 0)klist[i]=-klist[i];
}

std::sort(klist, klist + N, std::greater<float>());
std::sort(mylist, mylist + N);

for(int i=0;i<N;i++){
	float x=klist[i];
	//iterate over the list mylist and find the lowest item greater than it 
	// if 
	int found = -1;
	for(int j=0;j<N;j++){
		if(mylist[j]>x) {found =j; break;}
	}
	if(found>=0){
		mylist[found]=-mylist[found];
		score++;
	} else {
		
	}

}

return score;

}
void test(int l){
	int N;
	cin >>N;
	for(int i=0;i<N;i++) cin >> mylist[i];
	for(int i=0;i<N;i++) cin >> klist[i];
	cout << "Case #" << l << ":" << " "<<cheat_greedy(N) << " " <<greedy(N) << endl;

}
int main(int argc, char* argv[])
{
	int testcases;
	cin >>testcases;
		
	for(int i=0;i<testcases;i++){
		test(i+1);
	}

	return 0;
}

