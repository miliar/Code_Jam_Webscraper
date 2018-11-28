#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream infile("D-large.in");
    ofstream outfile("D-large.out");

    int T;
    infile >> T;

    int N;
    double arr1[1000]; //1000
    double arr2[1000]; //1000

    for(int t=0; t<T; t++)
    {
        infile >> N;
        for(int i=0; i<N; i++)
            infile >> arr1[i];
        for(int i=0; i<N; i++)
            infile >> arr2[i];

        sort(arr1,arr1+N);
        sort(arr2,arr2+N);
        int i=0, j=0;
        int decPoints=0;
        while(i<N && j<N)
        {
            if(arr1[i]<arr2[j])
                i++;
            else
            {
                decPoints++;
                i++;
                j++;
            }
        }

        int points=0;
        i=N-1;
        int j1=0, j2=N-1;

        while(i>=0)
        {
            if(arr1[i]>arr2[j2])
            {
                points++;
                j1++;
                i--;
            }
            else
            {
                j2--;
                i--;
            }
        }

        outfile << "Case #" << t+1 << ": " << decPoints << " " << points << endl;
    }
    return 0;
}
