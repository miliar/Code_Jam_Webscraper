#include <iostream>
#include <string.h>
#include <fstream>
int card[17];
using namespace std;

int main()
{
    int t,l1,l2,n,num;
    fstream fs;
    fstream fso;
    fs.open("C:\\A-small-attempt2.in");
    fso.open("C:\\A-small-attempt0.out");
    fs >> t;
    for(int c = 1; c <= t ; c++)
    {
        for(int i = 0 ; i < 17 ; i++)card[i]=0;
        fs >> l1;
        for(int i = 0 ; i < 16 ; i++)
        {
            fs >> num;
            if(i >= 4*(l1-1) && i < 4*l1)card[num]++;
        }

        fs >> l2;
        for(int i = 0 ; i < 16 ; i++)
        {
            fs >> num;
            if(i >= 4*(l2-1) && i < 4*l2)card[num]++;
        }

        int ans = -1;
        bool f = 1;
        for(int i = 1; i <= 16; i++)
        {
            if(ans != -1 && card[i] == 2){fso << "Case #" << c << ": Bad magician!"<< endl;f = 0;break;}
            else if(card[i] == 2)ans = i;
        }
        if(f)
        {
            if(ans != -1){fso << "Case #" << c << ": "<< ans<< endl;}
            else{fso << "Case #" << c << ": Volunteer cheated!"<< endl;}
        }
    }
    return 0;
}
