#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

string board[60];

void main2(void){
   //int hsh[1000];
   int A,B,K;
   scanf("%d%d%d",&A,&B,&K);
   //REP(i,A)scanf("%d",&a[i]);
   
   int cnt=0;
   for(int i=0;i<A;i++)
    for(int j=0;j<B;j++)
    {
    //printf("%d\n",i&j);
        if((i&j)<K)
        cnt++;
}    
   // printf("%d",cnt);
    gout<<cnt<<endl;
	
}

int main(void){
	int number_of_test_cases,k;
	scanf("%d",&number_of_test_cases);
    REP(k,number_of_test_cases)main2();
	return 0;
}
