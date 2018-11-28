#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>


#define TASK   "A-small"


using namespace std;

void solve(){
	
	vector<int> tempVector;
	vector<int> first,second;

	int tempRowNo=0;
	int temp = 0;
	int result = 0;
	int answer=0;
	
	scanf("%d",&tempRowNo);

	for(int i=1; i<=4; i++){

		scanf("%d",&temp);		tempVector.push_back(temp);
		scanf("%d",&temp); 		tempVector.push_back(temp);
		scanf("%d",&temp); 		tempVector.push_back(temp);
		scanf("%d",&temp);		tempVector.push_back(temp);

		if ( i != tempRowNo){
			tempVector.clear();
		}
		else{
			first.assign(tempVector.begin(),tempVector.end());
			tempVector.clear();			
		}
		
	}
	
	scanf("%d",&tempRowNo);
	
	for(int i=1; i<=4; i++){

		scanf("%d",&temp);		tempVector.push_back(temp);
		scanf("%d",&temp); 		tempVector.push_back(temp);
		scanf("%d",&temp); 		tempVector.push_back(temp);
		scanf("%d",&temp);		tempVector.push_back(temp);

		if ( i != tempRowNo){
			tempVector.clear();
		}else{
			second.assign(tempVector.begin(),tempVector.end());
			tempVector.clear();			
		}

	}
		
	for(int i=0; i<4; i++){
		if (first[i] == second[0]){
				result++;	answer = first[i]; 
		}
		else if(first[i] == second[1]){
				result++;	answer = first[i];
		}
		else if(first[i] == second[2]){
				result++;	answer = first[i];
		}
		else if(first[i] == second[3]){
				result++;	answer = first[i];
		}
	}

		switch (result)
		{
			case 0:
				printf("%s\n","Volunteer cheated!");
			break;
			
			case 1:
				printf("%d\n",answer);
			break;
			
			default:
				printf("%s\n","Bad magician!");
		
		}
		
}



int main(int argc, char **argv)
{
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
		
	char buf[1000];
	int testNum;
	gets(buf);
	sscanf(buf,"%d",&testNum);

	for (int testId = 1; testId <= testNum; testId++){
		
		printf("Case #%d: ",testId);
		solve();
		
	}	
	
	return 0;
}
