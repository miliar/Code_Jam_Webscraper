#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cstdio>

using namespace std;

bool count_number(int num, long long & counter){
    if(num==0) return false;
    unordered_set<int> flag;
    for(int i=0; i<10; ++i) flag.insert(i);
    int i=1;
    while(flag.size()!=0){
        counter=num*(i++);
        long long tmp=counter;
        while(tmp && flag.size()!=0){
            int tt=tmp%10;
            if(flag.find(tt)!=flag.end()) flag.erase(tt);
            tmp/=10;
        }
    }
    return true;
}

int main()
{
    freopen("D://A-large.in", "r", stdin);
    freopen("D://A-large.out", "w", stdout);
    int numCase;
	cin >> numCase;
	for(int i=0; i<numCase; i++) {
		int num;
		long long counter;
		cin>>num;
		if(count_number(num,counter)){
            cout << "Case #" << (i+1) << ": " << counter << endl;
		}
        else{
            cout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
        }
	}
    return 0;
}
