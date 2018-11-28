#include <iostream>
#include <string>
#include<stdio.h>
#include<set>


#define MAXN 2
using namespace std;

int main()
{
    int round;
    int count;
    int n;

    count = 1;
    int i, j;
    string input[MAXN];
    int moves;
    
    set<char> a[MAXN];

    cin >> round;
    while(count <= round)
    {
        cin >> n;
        moves  = 0;
        for(i=0; i<n; i++)
            a[i].clear();
        for (i=0; i< n; i++)
        {
            cin >> input[i]; 
        }

        for(i=0; i<n; i++)
        {
            for(j=0; j<input[i].length(); j++)
            {
                a[i].insert(input[i][j]);
            }
        }

        for(i=0; i<n-1; i++)
        {
            if(a[i] != a[i+1])
            {
                //cout << "Alphabet issue!" << endl;
                moves = -1;
                break;
            }
        }

        // same alphabet set
        if(i == (n-1))
        {
            int pos_i, pos_j;
            pos_i = 0;
            pos_j = 0;
            int len_i = input[0].length();
            int len_j = input[1].length();
            while((pos_i <= len_i) || (pos_j <= len_j))
            {
                if((pos_i == len_i) && (pos_j == len_j))
                {
                    break;
                }

                if(pos_i == len_i)
                {
                    if(input[1][pos_j] == input[1][pos_j-1])
                    {
                        pos_j++;
                        moves++;
                        continue;
                    }
                    else
                    {
                        //cout << "pos_i: " << pos_i << "pos_j: " << pos_j <<  " moves = -1" << endl; 
                        moves = -1;
                        break;
                    }
                }

                if(pos_j == len_j)
                {
                    if(input[0][pos_i] == input[0][pos_i-1])
                    {
                        pos_i++;
                        moves++;
                        continue;
                    }
                    else
                    {
                        //cout << "pos_i: " << pos_i << "pos_j: " << pos_j <<  " moves = -1" << endl; 
                        moves = -1;
                        break;
                    }
                }

                if(input[0][pos_i] == input[1][pos_j])
                {
                    pos_i++;
                    pos_j++;
                }

                else if(input[0][pos_i] != input[1][pos_j])
                {
                    if(input[0][pos_i] == input[0][pos_i-1])
                    {
                        //cout << "pos_i: " << pos_i << "pos_j: " << pos_j <<  "next step: pos_i++; moves++;" << endl; 
                        pos_i++;
                        moves++;
                        continue;
                    }
                    else if(input[1][pos_j] == input[1][pos_j-1])
                    {
                        pos_j++;
                        moves++;
                        continue;
                    }
                    else
                    {
                        //cout << "pos_i: " << pos_i << "pos_j: " << pos_j <<  " moves = -1" << endl; 
                        moves = -1;
                        break;
                    }
                }
            }
        }

        if(moves < 0)
            cout << "Case #" << count << ": " << "Fegla Won" <<endl;
        else
            cout << "Case #" << count << ": " << moves  <<endl;
        count++;
    }
    return 0;
}
