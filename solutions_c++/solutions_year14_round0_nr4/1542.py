#include <iostream>
#include <sstream>

using namespace std;

int main()
{
    int cases;
    int casenum = 1;
    int inputSize;
    int dec, war;

    cin >> cases;
    while (cases--)
    {
        cin >> inputSize;
        double naomi[inputSize];
        double ken[inputSize];
        for (int i = 0; i < inputSize; i++)
            cin >> naomi[i];

        for (int i = 0; i < inputSize; i++)
            cin >> ken[i];
        
        //create war arrays
        double wken[inputSize];
        double wnaomi[inputSize];
        for (int i = 0; i < inputSize; i++)
        {
            wken[i] = ken[i];
            wnaomi[i] = naomi[i];
        }

        double swap = 0;

        //sort war arrays.
        for (int i = 0; i < inputSize-1; i++)
            for (int j = 0; j < inputSize-i-1; j++)
            {
                if (wken[j] > wken[j+1])
                {
                    swap = wken[j];
                    wken[j] = wken[j+1];
                    wken[j+1] = swap;
                }
                if (wnaomi[j] > wnaomi[j+1])
                {
                    swap = wnaomi[j];
                    wnaomi[j] = wnaomi[j+1];
                    wnaomi[j+1] = swap;
                }

            }

        //Sort other arrays
        for (int i = 0; i < inputSize-1; i++)
            for (int j = 0; j < inputSize-i-1; j++)
            {
                if (ken[j] > ken[j+1])
                {
                    swap = ken[j];
                    ken[j] = ken[j+1];
                    ken[j+1] = swap;
                }
                if (naomi[j] > naomi[j+1])
                {
                    swap = naomi[j];
                    naomi[j] = naomi[j+1];
                    naomi[j+1] = swap;
                }

            }
        
        

        //Solve for Deceitful War!! (the hard part)
        
        //Fill array with n's and k's.
        int index = 0;
        int n = 0;
        int k = 0;
        bool wtf = true;

        stringstream s;

        //This works
        while (true)
        {
            if(n < inputSize)
            {
                if (naomi[n] < ken[k] || k == inputSize)
             {
                  s << "n";
                 n++;
             } else {
                 s << "k";
                 k++;
             }
            }else {
                s << "k";
                k++;
            }
            if (n == inputSize && k == inputSize)
                break;
        }
    

        //This block broken. Fix it.
        string dw = s.str();
        dec = inputSize;
        char c;
        n = 0;
        k = 0;
        int count = 0;
        for (int i = (inputSize*2)-1; i >= 0; i--)
        {
            c = dw.at(i);
            if (c == 'n')
            {
                n++;
            }
            if (c == 'k' && n > 0)
            {
                if (n > 0)
                {
                    count++;
                    n--;
                }
            }
        }
        
        dec = count;
        //Solve for WAR -- the easy part.
        war = 0;
        bool broken;
        for (int i = 0; i < inputSize; i++)
        {
            broken = false;
            double temp = wnaomi[i];
            for (int j = 0; j < inputSize; j++)
            {
                if (wken[j] > temp)
                {
                    wken[j] = 0;
                    broken = true;
                    break;
                }
            }
            if (broken)
                continue;
            war++;
    
        }
        
        cout << "Case #" << casenum++ << ": " << dec << " " << war << endl;

    }
    return 0;

}
