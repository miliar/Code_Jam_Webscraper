// A.cpp : Defines the entry point for the console application.
//
#include<iostream>
using namespace std;


int main(int argc, char* argv[])
{
    int T;
    int N;
    cin >> T;
    for(int t=1; t <= T; t++) {
        int res=0;
        cin >> N;
        int mul = 1;
        int currVal = 0;
        int lastVal = 0;
        while(res!=0x3ff) {
            if(mul++>100) {
                break;
            }
            currVal = lastVal + N;
            lastVal = currVal;
            while(currVal) {
                res |= (0x1 << (currVal%10));
                currVal = currVal/10;
            }
        }
        if(res==0x3ff) {
            cout << "case #" << t << ": " << lastVal << endl;
        } else {
            cout << "case #" << t << ": INSOMNIA" << endl;
        }
    }
	return 0;
}

