#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int puzzle_flip_invert(int *a,int n)
    {
    int i1,m,N=n,i,j; char b;
    // here print the input a[N]

    // solve the puzzle
    for (m=0;;m++)
        {
        // starting ones -> zeros
        if (a[0]==1)
            {
            for (i1=0;(i1<n-1)&&(a[i1+1]==1);i1++);
            if (i1==n-1) break; // solution found
            }
        // cut ending ones and then ending zeros -> ones
        else for (i1=n-1;(i1>=0)&&(a[i1]==1);i1--,n--);
        // flip and invert a[i] i=<0,i1>
        for (i=0,j=i1;i<=j;i++,j--)
            {
            b=1-a[i]; a[i]=1-a[j]; a[j]=b;
            }
        // here print partial solution a[N] and used range <1,i1+1>
        }
    // here print the result m
    return m;
    }
int main()
{
    
    int i;
    cin >> i;
    for(int y = 1; y<=i; y++)
    {
    std::string Num ;
    cin>>Num ;
    std::replace( Num.begin(), Num.end(), '+', '1'); // replace all '+' to '1'
    std::replace( Num.begin(), Num.end(), '-', '0'); 
    std::vector<int> ints;
    ints.reserve(Num.size()); 
    std::transform(std::begin(Num), std::end(Num), std::back_inserter(ints),
    [](char c) {
        return c - '0';
    } );
    int *a = &ints[0];
    int x;    
    x = puzzle_flip_invert(a,Num.length());
    cout << "\nCase #" << y << ": " << x;
    }
    
  
}