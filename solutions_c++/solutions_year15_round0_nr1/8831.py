#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <string>
#define forall(i,a,b) for(int i=a;i<b;i++)
#define scan(N) scanf("%d",&N); 
using namespace std;

vector<int> people;


int test_cases;
int max_shyness;
int numb_people;
int result;
char audience[200];


int main(){
	scan(test_cases);
	forall(i,0,test_cases){
		scanf("%d %[^\n]",&max_shyness,audience);
		numb_people=0;
		result=0;
		forall(j,0,max_shyness+1){
			//printf("j=%d numb_people=%d\n",j,numb_people);
			if(j>numb_people && (int)(audience[j]-48)>0){
				result+=j-numb_people;
				numb_people+=j-numb_people;
			}
			numb_people+=(int)(audience[j]-48);
			//printf("result=%d\n",result);

		}
		printf("Case #%d: %d\n",i+1,result);
	}

}