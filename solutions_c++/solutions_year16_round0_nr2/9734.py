// Pancake reverse - google code jam
// Ben Bradley April 9, 02016
// Borland C++ 5.5.1

#include <stdio.h>
#include <string.h>
#include <systypes.h>		//uint8, etc

#define MAX_PANCAKES 120

void flip (char flapstack[], uint32 number_to_flip)
{
    uint32 i;
    char mybuf [MAX_PANCAKES];
    for (i = 0; i < number_to_flip; i++)
        if (flapstack [i] == '+')
            mybuf [number_to_flip - i - 1] = '-';
         else
            mybuf [number_to_flip - i - 1] = '+';

    for (i = 0; i < number_to_flip; i++)
        flapstack [i] = mybuf [i];

} // void flip (char string[], uint32 number_to_flip)


uint32 scanhappy (char *p)
{
    while (*p == '+')
        p++;
    if (*p == '\0')
        return 1;
    return 0;

} // uint32 scanhappy (char *p)

uint32 count_transitions (char *p)
{
    uint32 transitions = 0;
    char first_in_string = *p;
//    printf ("In count_transitions first_in_string = %c ", first_in_string);
    while (*p != '\0')
    {
        while (*p == first_in_string)
        {
//            printf (" %02x", *p);
            p++;   
        }
//        printf (" T ");
        first_in_string = *p;
        transitions++;
    }
//    printf ("\n");
    transitions--; // remove count of end-of-string character.
    return transitions;
} // uint32 count_transitions (char *p)


void do_longest_flip (char p[])
{
    uint32 transitions;
    uint32 new_t;
    uint32 fliplength;
    char pcopy [MAX_PANCAKES];
    uint32 stack_heigth;

    transitions = count_transitions(p);
    stack_heigth = strlen (p) - 1;
    while (stack_heigth > 0)
    {
//        printf ("In do_longest_flip stack_heigth = %d\n", stack_heigth);
        strncpy (pcopy, p, MAX_PANCAKES);
        flip (pcopy, stack_heigth);
        if (count_transitions(pcopy) < transitions)
        {
            strncpy (p, pcopy, MAX_PANCAKES);        
            return;
        }
        stack_heigth--;
    }
    printf ("Error in do_longest_flip, no transitions.\n");
    return;

} // void do_longest_flip (char p[])



uint32 scanflips (char p[])
{
    uint32 transitions;
    uint32 flips = 0;
  
// this check not needed.  
//    if (count_transitions(p) == 0 && *p == '+')
//        return 0;


    while (count_transitions(p) > 0)
    {
        do_longest_flip (p);
        flips++;
    }
    if (*p != '+')
    {
        flip (p, strlen (p));
        flips++;
    }
    return flips;

} // uint32 scanflips (char p[])


void fix_input (char *p)
{
    while (*p == '+' || *p == '-')
        p++;
    *p = '\0';
    return;

} // void fix_input (char *p)


int main (void)
{
    uint32 i, number_of_input_cases;
    uint32 flips;
    uint32 last_value;
    char pancakes [MAX_PANCAKES];

    scanf ("%d\n", &number_of_input_cases);
//    printf ("number_of_input_cases = %d\n", number_of_input_cases);      
    for (i = 0; i < number_of_input_cases; i++)
    {
		gets (pancakes);
        fix_input (pancakes); // this will kill trailing spaces and such.
//        printf ("Input = %s\n", pancakes);
        flips = scanflips (pancakes);
        printf ("Case #%d: %d\n", i+1, flips);
    }
    

} // int main (void)

#ifdef __PLAYING_AROUND_
--+- 
+++- 2
+--- 4
---- 1
++++ 4

--+- 
-++- 3
+++- 1
+--- 4
---- 1
++++ 4

--+-
+-++ 4
--++ 1
++++ 2

--+-
++-+ 4
+--+ 3
---+ 1
++++ 3

--+-
+++- 2
---- 3
++++ 4

---+-
++++- 3
+---- 5
----- 1
+++++ 5

---+-
+-+++ 5
--+++ 1
+++++ 2

---+-
++++- 3
----- 4
+++++ 6


+--+- 
-++-- 4
+++-- 1
----- 3
+++++ 5




+--+-
+-++- 5
--++- 1
++++- 2
----- 4
+++++ 5

While number of transitions greater than zero
   Use longest flip that reduces number of transitions
check for - and if so, flip all


#endif //#ifdef __PLAYING_AROUND_




#ifdef __DOC_STUF_
//  10 points	
//  You must solve the small input first.
//  You have 8 minutes to solve 1 input file. (Judged after contest.)
//  Problem
//  
//  The Infinite House of Pancakes has just introduced a new kind of pancake! It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").
//  
//  You are the head waiter on duty, and the kitchen has just given you a stack of pancakes to serve to a customer. Like any good pancake server, you have X-ray pancake vision, and you can see whether each pancake in the stack has the happy side up or the blank side up. You think the customer will be happiest if every pancake is happy side up when you serve them.
//  
//  You know the following maneuver: carefully lift up some number of pancakes (possibly all of them) from the top of the stack, flip that entire group over, and then put the group back down on top of any pancakes that you did not lift up. When flipping a group of pancakes, you flip the entire group in one motion; you do not individually flip each pancake. Formally: if we number the pancakes 1, 2, ..., N from top to bottom, you choose the top i pancakes to flip. Then, after the flip, the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N. Pancakes 1, 2, ..., i now have the opposite side up, whereas pancakes i+1, i+2, ..., N have the same side up that they had up before.
//  
//  For example, let's denote the happy side as + and the blank side as -. Suppose that the stack, starting from the top, is --+-. One valid way to execute the maneuver would be to pick up the top three, flip the entire group, and put them back down on the remaining fourth pancake (which would stay where it is and remain unchanged). The new state of the stack would then be -++-. The other valid ways would be to pick up and flip the top one, the top two, or all four. It would not be valid to choose and flip the middle two or the bottom one, for example; you can only take some number off the top.
//  
//  You will not serve the customer until every pancake is happy side up, but you don't want the pancakes to get cold, so you have to act fast! What is the smallest number of times you will need to execute the maneuver to get all the pancakes happy side up, if you make optimal choices?
//  Input
//  
//  The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom.
//  Output
//  
//  For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of times you will need to execute the maneuver to get all the pancakes happy side up.
//  Limits
//  
//  1 = T = 100.
//  Every character in S is either + or -.
//  Small dataset
//  
//  1 = length of S = 10.
//  Large dataset
//  
//  1 = length of S = 100.
//  Sample
//  
//  Input
//  
//  5
//  -
//  -+
//  +-
//  +++
//  --+-
//  
//  Output
//  
//  Case #1: 1
//  Case #2: 1
//  Case #3: 2
//  Case #4: 0
//  Case #5: 3
//  
//  In Case #1, you only need to execute the maneuver once, flipping the first (and only) pancake.
//  
//  In Case #2, you only need to execute the maneuver once, flipping only the first pancake.
//  
//  In Case #3, you must execute the maneuver twice. One optimal solution is to flip only the first pancake, changing the stack to --, and then flip both pancakes, changing the stack to ++. Notice that you cannot just flip the bottom pancake individually to get a one-move solution; every time you execute the maneuver, you must select a stack starting from the top.
//  
//  In Case #4, all of the pancakes are already happy side up, so there is no need to do anything.
//  
//  In Case #5, one valid solution is to first flip the entire stack of pancakes to get +-++, then flip the top pancake to get --++, then finally flip the top two pancakes to get ++++.
#endif //#ifdef __DOC_STUF_

