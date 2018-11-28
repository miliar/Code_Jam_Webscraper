#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
int isPrime(unsigned long long number){

    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(unsigned long long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return i;
    }
    return 0;

}

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    unsigned long long num;
    int base,porc,count=0;
    string divisors;
    cout<<"Case #1:"<<endl;
    for(int i=0;i<pow(2,14);i++){
    	string bin=bitset<14>(i).to_string();
    	bin="1"+bin+"1";
    	
    	divisors=bin+" ";
    	for(base=2;base<=10;base++){
    		num=stoull(bin,0,base);
		porc=isPrime(num);
		if(porc==0){
			break;
		}
		else
			divisors=divisors+to_string(porc)+" ";
	}
	if(base==11){
		cout<<divisors<<endl;
		count++;
		if(count==50)
			break;
	}
    }   		       
    return 0;
}
