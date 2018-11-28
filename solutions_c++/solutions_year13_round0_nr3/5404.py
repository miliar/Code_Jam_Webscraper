#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

bool fairSquare(int start);
bool isPalindrome(int num);
int main(){
    ifstream in("input.in");
	cin.rdbuf(in.rdbuf());

	ofstream out("output.out");
    cout.rdbuf(out.rdbuf());
    //cout << "subhmahodaya";
    int testcases, low, high, i, count, start;

    cin >> testcases;

    for(i=0;i<testcases;i++){
            start=0;
        cin >> low;
        cin >> high;
        count = 0;
        start = ceil(sqrt(low));
        while(start*start <= high){
            if(fairSquare(start)){
                    //cout << start*start << endl;
                count++;
            }
            start++;
        }
        cout << "Case #" << i+1 <<": "<< count << endl;
    }
    cout << endl;
 }
 bool fairSquare(int start){
     if(isPalindrome(start) && isPalindrome(start*start)){
        return true;
     }
     return false;
 }
 bool isPalindrome(int num){
     int n, digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     if (n == rev)
        return true;
     else
        return false;
 }
