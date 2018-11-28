#include <iostream>
#include <stdio.h>
#define MAX_TAB_SIZE 39
using namespace std;



int main() {
int testNum ;
int isSolved;
int num_low, num_high;
long long unsigned int tab[MAX_TAB_SIZE] =
{1              ,
 4              ,
 9              ,
 121            ,
 484            ,
 10201          ,
 12321          ,
 14641          ,
 40804          ,
 44944          ,
 1002001        ,
 1234321        ,
 4008004        ,
 100020001      ,
 102030201      ,
 104060401      ,
 121242121      ,
 123454321      ,
 125686521      ,
 400080004      ,
 404090404      ,
 10000200001    ,
 10221412201    ,
 12102420121    ,
 12345654321    ,
 40000800004    ,
 1000002000001  ,
 1002003002001  ,
 1004006004001  ,
 1022325232201  ,
 1232346432321  ,
 1234567654321  ,
 4000008000004  ,
 4004009004004  ,
 100000020000001,
 100220141022001,
 123456787654321,
 100220141022001,
 121242363242121
};

int j = -1;

cin >> testNum;
for(int i = 1;i<=testNum;i++){

    cin >> num_low >> num_high;
    int idxFirstBiggerThenLow;
    int idxFirstBiggerThenHigh;

    idxFirstBiggerThenLow = 0;
    for(int j=0; num_low>tab[j];j++){
        idxFirstBiggerThenLow = j+1;
    }

    idxFirstBiggerThenHigh = MAX_TAB_SIZE-1;
    for(int j=MAX_TAB_SIZE; num_high<tab[j];j--){
        idxFirstBiggerThenHigh = j-1;
    }



      cout <<"Case #" << i<< ": " << (idxFirstBiggerThenHigh-idxFirstBiggerThenLow+1) <<  endl;

}


return 0;
}
