//
//  main.cpp
//  Problem1
//
//  Created by Navneet Gandhi on 4/30/16.
//  Copyright (c) 2016 Navneet Gandhi. All rights reserved.
//


#include <iostream>
#include <vector>
#include <unordered_map>



using namespace std;


char digitStrings[][10] =
{
    "ZERO", //Z
    "ONE", //4: O
    "TWO", //W
    "THREE", //4: R
    "FOUR", // U
    "FIVE", //3: V
    "SIX", //X
    "SEVEN", //2: S
    "EIGHT", // 4:G
    "NINE" //4: I
};



void ProcessOut(int alphabetCounts[], char letter, int numberCounts[], int number)
{
    numberCounts[number] = alphabetCounts[letter - 'A'];
    
    int i=0;
    while(digitStrings[number][i] !='\0')
    {
        char c = digitStrings[number][i];
        alphabetCounts[c - 'A'] -= numberCounts[number];
        i++;
    }
}



int main(int argc, const char * argv[])
{
    int T;
    int i;
    
    cin >> T;
    
    char fullString[2001];
    int numberCounts[10] = {0};
    int alphabetCounts[26] = {0};
    
    for (int t = 1; t <= T; ++t)
    {
        cin >> fullString;
        
        i = 0;
        while(fullString[i] != '\0')
            alphabetCounts[fullString[i++] - 'A']++;
        
        ProcessOut(alphabetCounts, 'Z', numberCounts, 0);
        ProcessOut(alphabetCounts, 'W', numberCounts, 2);
        ProcessOut(alphabetCounts, 'U', numberCounts, 4);
        ProcessOut(alphabetCounts, 'X', numberCounts, 6);

        ProcessOut(alphabetCounts, 'S', numberCounts, 7);
        ProcessOut(alphabetCounts, 'V', numberCounts, 5);

        ProcessOut(alphabetCounts, 'O', numberCounts, 1);
        ProcessOut(alphabetCounts, 'R', numberCounts, 3);
        ProcessOut(alphabetCounts, 'G', numberCounts, 8);
        ProcessOut(alphabetCounts, 'I', numberCounts, 9);


        cout << "Case #" << t << ": ";

        for(int d=0; d<=9; d++)
        {
            for(int n=0; n< numberCounts[d]; n++)
                cout << d;
        }
        cout << endl;
        
    
     
    }

    
    
}

