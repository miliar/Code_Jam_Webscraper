// Sheep - google code jam
// Ben Bradley 7:30PM EDT April 8, 02016

#include <stdio.h>
#include <systypes.h>		//uint8, etc

#define MAXDIGITS 10

#define MAX32 ((uint32)((2^32)-1))


uint32 decompose (uint32 n, uint32 d[])
{
    uint32 number_of_digits = 0;
	uint32 i;
    uint32 j = n;
	for (i = 0; i < MAXDIGITS; i++)
	{
        if (j != 0)
            number_of_digits = i + 1;
		d [i] = j % 10;				// get lowest digit
//        printf ("In decompose, d [%d] = %d\n", i, d [i]);
		j /= 10;					// divide by 10 to get rid of it
	}
//    printf ("In decompose, %u has %u digits.\n", n, number_of_digits);
    return number_of_digits;

} // uint32 decompose (uint32 n, uint32 d[])


uint32 count_digits (uint32 digits [], uint32 used_digits [], uint32 ndigits)
{

    uint32 i;
    uint32 used_digit_count = 0;
    uint32 j;
    
    for (i = 0; i < ndigits; i++)
    {
//        printf ("in count_digits, digits [%d] is %d ", i, digits [i]);
        used_digits [digits [i]] = 1;
//        printf ("\n");
//        for (j = 0; j < 10; j++)
//            printf ("j, digits, used_digits = %d %d %d\n", j, digits [j], used_digits [j]);
    }
//    printf ("\n");

    for (i = 0; i < 10; i++)
        if (used_digits [i])
        {
//            printf ("used-digits [%d] is 1.\n", i);
            used_digit_count++;
        }
//    printf ("\n");
    return used_digit_count;
    
            
} // uint32 count_digits (uint32 used_digits [], digits [])


#define MAX_COUNT 100000000

// return -1 for infinite
int32 countsheep (uint32 startcount)
{
    uint32 i;
    uint32 j;
    uint32 count = 0;
    uint32 lastcount = 0;
    uint32 ndigits;
    uint32 udigits = 0;
    uint32 digits [20];
    uint32 used_digits [20];
    
    for (i = 0; i < 10; i++)
        used_digits [i] = 0;
    
   
    for (i = 1; i < 400000000 && udigits < 10; i++)
    {
        count += startcount;            // Do first or i'th count.
        if (count < lastcount)          // If this is true, count wrapped around and we're done.
            return MAX32;
        ndigits = decompose (count, digits);
        if (ndigits == 0)
            return MAX32;
//        printf ("In countsheep, digits are:\n");
//        for (j = 0; j < 10; j++)
//            printf (" %d", digits [j]);
//        printf ("\n");
        udigits = count_digits (digits, used_digits, ndigits);
//        printf ("In countsheep2, digits are:\n");
//        for (j = 0; j < 10; j++)
//            printf (" %d", digits [j]);
//        printf ("\n");
//        printf ("In countsheep, used_digits are:\n");
//        for (j = 0; j < 10; j++)
//            printf (" %d", used_digits [j]);
//        printf ("\n");
        
    } // while (udigits < 10) && loopcount++ < 1000)
    if (i >= MAX_COUNT - 1)
        return MAX32;
    return count;

} // int32 countsheep (uint32 startcount)



int main (void)
{
    uint32 i, number_of_input_cases;
    uint32 startnumber;
    uint32 last_value;
    
    scanf ("%d\n", &number_of_input_cases);
//    printf ("number_of_input_cases = %d\n", number_of_input_cases);      
    for (i = 0; i < number_of_input_cases; i++)
    {
        scanf ("%d\n", &startnumber);
//        printf ("case %d, startnumber = %d\n", i + 1,  startnumber);        
        last_value = countsheep (startnumber);
        if (last_value == MAX32)
            printf ("Case #%d: INSOMNIA\n", i + 1);
        else
            printf ("case #%d: %u\n", i + 1,  last_value);        
//        printf ("last_value = %d\n", last_value);
    }
    

} // int main (void)




#ifdef __DOC_STUF_
Problem

Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    3N = 5076. Now she has seen all ten digits, and falls asleep.

What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a single number N, the number Bleatrix has chosen.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.
Limits

1 = T = 100.
Small dataset

0 = N = 200.
Large dataset

0 = N = 106.
Sample

Input
  	
Output
 

5
0
1
2
11
1692

	

Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076


In Case #1, since 2 × 0 = 0, 3 × 0 = 0, and so on, Bleatrix will never see any digit other than 0, and so she will count forever and never fall asleep. Poor sheep!

In Case #2, Bleatrix will name 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. The 0 will be the last digit needed, and so she will fall asleep after 10.

In Case #3, Bleatrix will name 2, 4, 6... and so on. She will not see the digit 9 in any number until 90, at which point she will fall asleep. By that point, she will have already seen the digits 0, 1, 2, 3, 4, 5, 6, 7, and 8, which will have appeared for the first time in the numbers 10, 10, 2, 30, 4, 50, 6, 70, and 8, respectively.

In Case #4, Bleatrix will name 11, 22, 33, 44, 55, 66, 77, 88, 99, 110 and then fall asleep.

Case #5 is the one described in the problem statement. Note that it would only show up in the Large dataset, and not in the Small dataset.

#endif //#ifdef __DOC_STUF_
