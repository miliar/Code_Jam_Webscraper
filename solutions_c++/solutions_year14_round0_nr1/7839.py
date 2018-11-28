#include <stdlib.h>
#include <stdio.h>
#include<iostream>

using namespace std;

int main()
{
    int T = 0; //number of test cases
    int answer1 = 0, answer2 = 0;
    int arr1[4][4], arr2[4][4];
    int flag = 0;
    int card;
    
    scanf("%d", &T);
    
    if (T >= 1 ) //&& T <= 100)
    {
        for(int count = 1; count <= T; count++)
        {
            scanf("%d", &answer1);

            for(int i = 1; i <= 4; i++)
            {
                for(int j = 1; j <= 4; j++)
                {

                    scanf("%d", &arr1[i][j]);
                }

            }

            scanf("%d", &answer2);

            for(int i = 1; i <= 4; i++)
            {
                for(int j = 1; j <= 4; j++)
                {

                    scanf("%d", &arr2[i][j]);
                }

            }

            for(int i = 1; i <= 4; i++)
            {
                for(int j = 1; j <= 4; j++)
                {
                    if(arr1[answer1][i] == arr2[answer2][j])
                    {
                        if (flag == 1)
                        {
                            flag = 2;
                        }

                        else if(flag == 0)
                        {
                            card = arr1[answer1][i];
                            flag = 1;
                        }


                    }
                }
            }

            switch(flag)
            {
            case 0 : cout << "Case #" << count << ":" << " Volunteer cheated!" << endl ;
                break;
            case 1 : cout << "Case #" << count << ":" << " " << card << endl ;
                break;
            case 2 : cout << "Case #" << count << ":" << " Bad magician!" << endl ;
                break;
            }

            flag = 0;
            card = 0;
        }

        return 0;
    }
    else cout << "Wrong number of test cases" << endl;
    return 0;
}









