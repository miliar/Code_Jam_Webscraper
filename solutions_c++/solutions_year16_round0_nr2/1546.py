// A.cpp : Defines the entry point for the console application.
//
#include<iostream>
using namespace std;

#define BLANK '-'
#define HAPPY '+'

void flip(char* arr, int lIdx) {
    for(int i=0;i<=lIdx/2;i++) {
        char tmp = arr[i];
        arr[i] = arr[lIdx-i]=='-'?'+':'-';
        arr[lIdx-i]= tmp=='-'?'+':'-';
    }
}

int getLast(char* arr, int idx, char chr) {
   while(idx >= 0 && arr[idx] != chr) {
       idx--;
   }
   return idx;
}

int main(int argc, char* argv[])
{
    int T;
    char S[101];
    cin >> T;
    for(int t=1; t <= T; t++) {
        int res=0;
        cin >> S;
        int strLen = strlen(S);
        int j = getLast(S, strLen-1, BLANK);
        while(j>=0) {
            if(S[0]=='+') {
                int h = getLast(S, j, HAPPY);
                flip(S, h);
            } else {
                flip(S, j);
                j = getLast(S, j, BLANK);
            }
            res++;
        }
        cout << "Case #" << t << ": " << res << endl;
    }
	return 0;
}

