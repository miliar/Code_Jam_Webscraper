#include<string.h>
#include<map>
#include<iostream>
#include<utility>
#include<math.h>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#define DBG 0
using namespace std;



void process() {
    int ans1, ans2;
    int firstCardArrangement[5][5];
    int secondCardArrangement[5][5];
    int row = 4, col =4;
    //firstCard input
    cin>>ans1;
    ans1 = ans1 -1;
    for (int i=0;i<row; i++) {
        for (int j=0;j<col; j++) {
		cin>>firstCardArrangement[i][j];
	}
    }

    //secondCard input
    cin>>ans2;
    ans2= ans2-1;
    for (int i=0;i<row; i++) {
        for (int j=0;j<col; j++) {
		cin>>secondCardArrangement[i][j];
	}
    }

    int noOfMatch = 0;
    int cardNum=0;
    for (int i=0;i<col; i++) {
	
        for (int j=0;j<col; j++) {
	    if(firstCardArrangement[ans1][i] == secondCardArrangement[ans2][j]) {
		noOfMatch++;    
		cardNum = firstCardArrangement[ans1][i];
	    }	
	}
    }

    if(noOfMatch == 0) {
        cout<<"Volunteer cheated!";
    } else if(noOfMatch==1) {
	cout<< cardNum;   
    } else {
	cout<< "Bad magician!";    
    }
    


}

int main() {
    int T;
   int A, N;
    cin>>T;
   int count=0;
    while(T>0) {
        count++;
        T--;
        cout<<"Case #"<<count<<": ";
        process();
        cout<<"\n";
    }
    return 0;
}
