#include <iostream>
#include <fstream>
#include <conio.h>
#include <algorithm>

using namespace std;

int warSol(double naomi[], double ken[], int N)
{
    int i = 0, j = 0;
    for(; j < N; j++)
    {
        if(naomi[i] < ken[j])
             i++;
    }
    
    return (N - i);
}

int dwarSol(double naomi[], double ken[], int N)
{
    int count = 0;
    int M = N;
    int j = 0;
    for(int i = 0; i < N; i++)
    {    
        if(naomi[i] < ken[j])
        {
           M--;
        }
        else
        {
            count++;
            j++;
        }
    }
    return count;
}

int main()
{
    ifstream input("input.txt"); // Try to open a input file for reading 
    
    if(!input)
    {
           cout<<"Sorry !!!File named input.txt not opened\n";
           getch();     // Hold standard output terminal untill any key press
           return 0;
    }
    
    // Input file named input.txt opened for reading purpose
    
     ofstream output("output.txt");   // Try to open a output file for writing
     
     if(!output)
     {
           cout<<"Sorry !!!File named output.txt not opened\n";
           getch();     // Hold standard output terminal untill any key press 
           return 0;
     }
    
    // Output file named output.txt opened for writing purpose

    int T;
    input >> T;
    
    int M = T;
    
    while(T--)
    {
        int N;      
        input >> N;
        double naomi[N], ken[N];
        for(int i = 0; i < N; i++)
            input >> naomi[i];
        for(int i = 0; i < N; i++)
            input >> ken[i];
        sort(naomi, naomi + N);
        sort(ken, ken + N);
        int z = warSol(naomi, ken, N);
        int y = dwarSol(naomi, ken, N);
        output<<"Case #"<<M-T<<": "<<y<<" "<<z<<endl;  
    }    
        
    input.close();      // Close input stream of reading
   
    output.close();     // Close output stream of writing
    
    return 0;
}
