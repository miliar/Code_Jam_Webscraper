#include<stdio.h>
#include<math.h>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;

bool isPalindrome(int val) {
    if (val < 0) return false;
    int div = 1;
    while (val / div >= 10) {
        div = div * 10;
    }        
    while (val != 0) {
        int l = val / div;
        int r = val % 10;
        if (l != r) return false;
        val = (val % div) / 10;
        div /= 100;
    }
    return true;
}

int findnearestnumber(int max) {
        
    return (int)sqrt(max);
}

void allfairsquares(int high, std::vector<int> &copy) {
    std::set<int> cont;
    for(int j= 1; j <= high; j++) {

        if(isPalindrome(j)) {
            int x = j*j;

            if(isPalindrome(x)) {
                printf("number: %d square: %d\n", j, x);
                cont.insert(x);
            }

        }
    }
   std::insert_iterator< std::vector<int> > ri(copy, copy.end());
   std::copy(cont.begin(),cont.end(),ri);
}

int findtotal(int low, int high, std::vector<int> &copy) {

 int first = -1, last = -1;
 int i=0 , length = copy.size() - 1;
 for(int j= 0 ; j<= length ; j++ ) {

        if( first == -1 && copy[j] >= low ) {
           first = j;
        } 
        if(last == -1 && copy[length - j] <= high){
                last = length - j;
        }
        if(last != -1 && first != -1 ) {

        break;
        }

 }

/*printf("%d %d\n", low , high);


 for(int j= 0 ; j<= length ; j++ ) {

        printf("vector: %d ", copy[j] );
 }

printf("\n%d %d\n", first , last); */
//printf("\n%d %d\n", first , last); 
if((last == -1 || first == -1) ||  (last < first ) ) return 0;
return (last - first) + 1;

}

int main() {
FILE *fp = fopen("input.txt", "r");
int count;
char newline;
fscanf(fp, "%d", &count);
fscanf(fp, "%c", &newline);

std::vector<int> fairsquare;
int high = findnearestnumber(1000);
allfairsquares(high, fairsquare);
int round = 0;
while( round++ < count) {
    int low, max;
    fscanf(fp, "%d", &low); 
    fscanf(fp, "%d", &max); 
    fscanf(fp, "%c", &newline);
        
    int total = findtotal(low, max, fairsquare);     

    //int high = findnearestnumber(max);
  
    //printf("low: %d max:  %d high: %d\n", low, max, high);
    /*int total = 0;
    for(int j= 1; j <= high; j++) {

        if(isPalindrome(j)) {
            int x = j*j;

            if( (x >= low) && isPalindrome(x)) {
                total++;  
                printf("number: %d square: %d\n", j, x);
            }
        }
    }*/

    printf("Case #%d: %d\n", round, total);

}

}
