//14/04/2013
//kizarae@gmail.com

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <sstream>

using namespace std;

//Messy, I know
//Using redirects to standard input and output
void fairsq(int min, int max);
char* reverse(char *string);
bool isPalindrome(char *string);
char* inttochar(int num);

int main ()
{
    int n;
    char* line = new char[256];
    char* st;
    int min, max;
    
    //Get number of cases
    cin.getline(line, 256);
    n = atoi(line);
    
    for (int z=0; z<n; z++) //For each case
    {
        cin.getline(line, 256);    
        st = strtok(line," ");
        min = atoi(st);
        st = strtok(NULL," ");
        max = atoi(st);
        
        cout << "Case #" << (z+1) << ": ";
        fairsq(min,max);
    }
    
    return 0;
}

void fairsq(int min, int max)
{
    char* num;
    int count = 0;
    for (int z=min; z<=max; z++)
    {
        num = inttochar(z);
        if (isPalindrome(num)) //If fair
        {
            double doub = sqrt(z);
            int in = doub;
            if (doub == in) //If a square
            {
                num = inttochar(in);
                if (isPalindrome(num)) //If fair and square
                {
                    count++;
                }
            }
        }
    }
    cout << count << endl;
}

char* reverse(char *string)
{
    //function to reverse string
    char *rear;
    int length;
    char *rString;
    rString = new char[100];

    length = strlen(string);
    rear = (string+length-1); //Create rear pointer, which points to the last character in the array

    for (int z=0; z<length; z++){
        rString[z] = *rear; //Copy last character into new array
        rear--; //Decrement the rear pointer so the loop copies the array in reverse order
    }
    
    rString[length] = '\0'; //Add null character to the end
    return rString;
}

bool isPalindrome(char *string)
{
    //check if palindrome
    char *rev = reverse(string);
    if (strcoll(string,rev))
    {
        return false;
    }
    else
    {
        return true;
    }
}

char* inttochar(int num)
{
    char* c = new char[100];
    string s;
    stringstream ss;
    
    ss << num;
    s = ss.str(); //Convert to string
    strcpy(c,s.c_str()); //Convert to char array
    
    return c;
}
