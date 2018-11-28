/* 
 * File:   main.cpp
 * Author: Dayanand
 *
 * Created on 27 April 2013, 08:04
 */

#include <cstdlib>
#include <stdio.h>

using namespace std;

/*
 * 
 */
int FindSquare(int radius,int test)
{
    int num = 0;
   // int test = radius + k;
    num = (test * test) - (radius *radius);
    return num;
}
int main(int argc, char** argv) {
    int no_of_test_cases;
    freopen("paint.txt" ,"r+",stdin);
    freopen("paint_out.txt" ,"w+",stdout);
    scanf("%d\n",&no_of_test_cases);
    for(int i = 0;i<no_of_test_cases;i++)
    {
        int sum = 0;
        int j = 0;
        int k = 1;
        int radius = 0;
        int paint = 0;
        int count = 0;
        scanf("%d\t",&radius);
        scanf("%d\t",&paint);
        for(;;j++)
        {
         sum += FindSquare(radius + k -1,radius + k);
         if(sum > paint)
             break;
         k += 2;
        }  
        printf("Case #%d: %d",i+1,j);
        printf("\n");
    }
    return 0;
}

