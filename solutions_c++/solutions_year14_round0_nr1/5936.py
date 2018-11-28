//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Phoom on 10/4/14.
//

#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

void think()
{
    int ch1,ch2,q2,count=0,card=0;
    int r1[4][4];
    cin >> ch1;
    for(int i = 0; i < 4;i++){
        for(int j = 0; j < 4;j++){
            cin >> r1[i][j];
        }
    }
    cin >> ch2;
    for(int i = 0; i < 4;i++){
        for(int j = 0; j < 4;j++){
            cin >> q2;
            if (ch2 == i+1) {
                if (q2==r1[ch1-1][0]) {
                    count++;
                    card=r1[ch1-1][0];
                }
                if (q2==r1[ch1-1][1]) {
                    count++;
                    card=r1[ch1-1][1];
                }
                if (q2==r1[ch1-1][2]) {
                    count++;
                    card=r1[ch1-1][2];
                }
                if (q2==r1[ch1-1][3]) {
                    count++;
                    card=r1[ch1-1][3];
                }
            }
        }
    }
    if (count>1) {
        cout << "Bad magician!";
    }else if (count<1){
        cout << "Volunteer cheated!";
    }else if (count==1){
        cout << card;
    }
    cout << endl;
}

int main()
{
    
	freopen("B-small-practice.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TestCase = 0;
	cin >> TestCase;
    
	for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
		cout << "Case #" << CaseID << ": ";
		think();
	}

    return 0;
}
