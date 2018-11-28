#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <list>
#include <ctime>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define  epsilon 1e-7

using namespace std;

int main()
{
    ofstream out("out.txt");
    int testcase;
    cin >> testcase;
    int Dwar[testcase];
    int War[testcase];
    for(int k = 0; k < testcase; k++)
    {
        int n;
        cin >> n;
      double naomi[n], ken[n];
      for(int i = 0; i < n; i++)cin >> naomi[i];
      for(int i = 0; i < n; i++)cin >> ken[i];

        sort(naomi, naomi + n);
        sort(ken, ken + n);

        int naomi_start = 0;
        int ken_start = 0;
        int Dwar_count = 0;
        while(naomi_start < n)
        {
            if(naomi[naomi_start] < ken[ken_start])
            {
                naomi_start++;
            }
            else if(naomi[naomi_start] > ken[ken_start])
            {
                naomi_start++;
                ken_start++;
                Dwar_count++;
            }
            else{
                    naomi_start++;
                    ken_start++;
                }
        }

        Dwar[k] = Dwar_count;
        int naomi_end = n - 1;
        int ken_end = n - 1;
        ken_start = 0;   ///using variable alredy defined
        int war_count = 0;
        while(naomi_end >= 0)
        {
            if(naomi[naomi_end] > ken[ken_end])
            {
                ken_start++;
                naomi_end--;
                war_count++;
            }
            else
            {
                naomi_end--;
                ken_end--;
            }

        }

        War[k] = war_count;
    }
    for(int i = 0; i < testcase; i++)
        out << "Case #" << (i + 1) << ": " << Dwar[i] << " " << War[i] << endl;
}

